import { assertNever, isPlainObject } from "@fern-api/core-utils";
import {
    DeclaredTypeName,
    ExampleContainer,
    ExampleObjectProperty,
    ExamplePrimitive,
    ExampleSingleUnionType,
    ExampleSingleUnionTypeProperties,
    ExampleTypeReference,
    ExampleTypeReferenceShape,
    ExampleTypeShape,
    PrimitiveType
} from "@fern-api/ir-sdk";
import { FernWorkspace } from "@fern-api/workspace-loader";
import {
    isRawObjectDefinition,
    RawSchemas,
    visitRawTypeDeclaration,
    visitRawTypeReference
} from "@fern-api/yaml-schema";
import { validateTypeReferenceExample } from "../../examples/validateTypeReferenceExample";
import { FernFileContext } from "../../FernFileContext";
import { IdGenerator } from "../../IdGenerator";
import { ExampleResolver } from "../../resolvers/ExampleResolver";
import { TypeResolver } from "../../resolvers/TypeResolver";
import {
    getSingleUnionTypeName,
    getSingleUnionTypeProperties,
    getUnionDiscriminant,
    getUnionDiscriminantName
} from "./convertDiscriminatedUnionTypeDeclaration";
import { getEnumNameFromEnumValue } from "./convertEnumTypeDeclaration";
import { getPropertyName } from "./convertObjectTypeDeclaration";

export function convertTypeExample({
    typeName,
    typeDeclaration,
    example,
    typeResolver,
    exampleResolver,
    fileContainingType,
    fileContainingExample,
    workspace
}: {
    typeName: DeclaredTypeName;
    typeDeclaration: RawSchemas.TypeDeclarationSchema;
    example: RawSchemas.ExampleTypeValueSchema;
    typeResolver: TypeResolver;
    exampleResolver: ExampleResolver;
    fileContainingType: FernFileContext;
    fileContainingExample: FernFileContext;
    workspace: FernWorkspace;
}): ExampleTypeShape {
    return visitRawTypeDeclaration<ExampleTypeShape>(typeDeclaration, {
        alias: (rawAlias) => {
            return ExampleTypeShape.alias({
                value: convertTypeReferenceExample({
                    example,
                    rawTypeBeingExemplified: typeof rawAlias === "string" ? rawAlias : rawAlias.type,
                    fileContainingRawTypeReference: fileContainingType,
                    fileContainingExample,
                    typeResolver,
                    exampleResolver,
                    workspace
                })
            });
        },
        object: (rawObject) => {
            return convertObject({
                typeName,
                rawObject,
                example,
                fileContainingType,
                fileContainingExample,
                typeResolver,
                exampleResolver,
                workspace
            });
        },
        discriminatedUnion: (rawUnion) => {
            const discriminant = getUnionDiscriminant(rawUnion);
            if (!isPlainObject(example)) {
                throw new Error("Example is not an object");
            }
            const discriminantValueForExample = example[discriminant];
            if (discriminantValueForExample == null) {
                throw new Error("Example is missing discriminant: " + discriminant);
            }
            if (typeof discriminantValueForExample !== "string") {
                throw new Error("Discriminant value is not a string");
            }

            const rawSingleUnionType = rawUnion.union[discriminantValueForExample];
            if (rawSingleUnionType == null) {
                throw new Error(`${discriminantValueForExample} is not one of the specified discriminant values.`);
            }

            const rawValueType =
                typeof rawSingleUnionType === "string"
                    ? rawSingleUnionType
                    : typeof rawSingleUnionType.type === "string"
                    ? rawSingleUnionType.type
                    : undefined;

            return ExampleTypeShape.union({
                discriminant: fileContainingExample.casingsGenerator.generateNameAndWireValue({
                    name: getUnionDiscriminantName(rawUnion).name,
                    wireValue: discriminant
                }),
                singleUnionType: convertSingleUnionType({
                    rawValueType,
                    rawSingleUnionType,
                    fileContainingType,
                    fileContainingExample,
                    typeResolver,
                    exampleResolver,
                    example,
                    discriminant,
                    discriminantValueForExample,
                    workspace
                })
            });
        },
        enum: (rawEnum) => {
            if (typeof example !== "string") {
                throw new Error("Enum example is not a string");
            }
            return ExampleTypeShape.enum({
                value: fileContainingExample.casingsGenerator.generateNameAndWireValue({
                    name: getEnumNameFromEnumValue(example, rawEnum).name,
                    wireValue: example
                })
            });
        },
        undiscriminatedUnion: (undiscriminatedUnion) => {
            for (const [index, variant] of undiscriminatedUnion.union.entries()) {
                const violationsForMember = validateTypeReferenceExample({
                    rawTypeReference: typeof variant === "string" ? variant : variant.type,
                    example,
                    typeResolver,
                    exampleResolver,
                    file: fileContainingExample,
                    workspace
                });
                if (violationsForMember.length === 0) {
                    return ExampleTypeShape.undiscriminatedUnion({
                        index,
                        singleUnionType: convertTypeReferenceExample({
                            example,
                            rawTypeBeingExemplified: typeof variant === "string" ? variant : variant.type,
                            fileContainingRawTypeReference: fileContainingType,
                            fileContainingExample,
                            typeResolver,
                            exampleResolver,
                            workspace
                        })
                    });
                }
            }
            throw new Error("Example doesn't match any of the undiscriminated unions");
        }
    });
}

export function convertTypeReferenceExample({
    example,
    fileContainingExample,
    rawTypeBeingExemplified,
    fileContainingRawTypeReference,
    typeResolver,
    exampleResolver,
    workspace
}: {
    example: RawSchemas.ExampleTypeReferenceSchema;
    fileContainingExample: FernFileContext;
    rawTypeBeingExemplified: string;
    fileContainingRawTypeReference: FernFileContext;
    typeResolver: TypeResolver;
    exampleResolver: ExampleResolver;
    workspace: FernWorkspace;
}): ExampleTypeReference {
    const { resolvedExample, file: fileContainingResolvedExample } = exampleResolver.resolveExampleOrThrow({
        example,
        file: fileContainingExample
    });
    const jsonExample = exampleResolver.resolveAllReferencesInExampleOrThrow({
        example,
        file: fileContainingExample
    }).resolvedExample;

    const shape = visitRawTypeReference<ExampleTypeReferenceShape>(rawTypeBeingExemplified, {
        primitive: (primitive) => {
            return convertPrimitiveExample({
                example: resolvedExample,
                typeBeingExemplified: primitive
            });
        },
        map: ({ keyType, valueType }) => {
            if (!isPlainObject(resolvedExample)) {
                throw new Error("Example is not an object");
            }
            return ExampleTypeReferenceShape.container(
                ExampleContainer.map(
                    Object.entries(resolvedExample).map(([key, value]) => ({
                        key: convertTypeReferenceExample({
                            example: key,
                            fileContainingExample: fileContainingResolvedExample,
                            rawTypeBeingExemplified: keyType,
                            fileContainingRawTypeReference,
                            typeResolver,
                            exampleResolver,
                            workspace
                        }),
                        value: convertTypeReferenceExample({
                            example: value,
                            fileContainingExample: fileContainingResolvedExample,
                            rawTypeBeingExemplified: valueType,
                            fileContainingRawTypeReference,
                            typeResolver,
                            exampleResolver,
                            workspace
                        })
                    }))
                )
            );
        },
        list: (itemType) => {
            if (!Array.isArray(resolvedExample)) {
                throw new Error("Example is not a list");
            }
            return ExampleTypeReferenceShape.container(
                ExampleContainer.list(
                    resolvedExample.map((exampleItem) =>
                        convertTypeReferenceExample({
                            example: exampleItem,
                            fileContainingExample: fileContainingResolvedExample,
                            rawTypeBeingExemplified: itemType,
                            fileContainingRawTypeReference,
                            typeResolver,
                            exampleResolver,
                            workspace
                        })
                    )
                )
            );
        },
        set: (itemType) => {
            if (!Array.isArray(resolvedExample)) {
                throw new Error("Example is not a list");
            }
            return ExampleTypeReferenceShape.container(
                ExampleContainer.set(
                    resolvedExample.map((exampleItem) =>
                        convertTypeReferenceExample({
                            example: exampleItem,
                            fileContainingExample: fileContainingResolvedExample,
                            rawTypeBeingExemplified: itemType,
                            fileContainingRawTypeReference,
                            typeResolver,
                            exampleResolver,
                            workspace
                        })
                    )
                )
            );
        },
        optional: (itemType) => {
            return ExampleTypeReferenceShape.container(
                ExampleContainer.optional(
                    resolvedExample != null
                        ? convertTypeReferenceExample({
                              example: resolvedExample,
                              fileContainingExample: fileContainingResolvedExample,
                              rawTypeBeingExemplified: itemType,
                              fileContainingRawTypeReference,
                              typeResolver,
                              exampleResolver,
                              workspace
                          })
                        : undefined
                )
            );
        },
        literal: (literal) => {
            switch (literal.type) {
                case "boolean":
                    return ExampleTypeReferenceShape.primitive(ExamplePrimitive.boolean(literal.boolean));
                case "string":
                    return ExampleTypeReferenceShape.primitive(
                        ExamplePrimitive.string({
                            original: literal.string
                        })
                    );
                default:
                    assertNever(literal);
            }
        },
        named: (named) => {
            const typeDeclaration = typeResolver.getDeclarationOfNamedTypeOrThrow({
                referenceToNamedType: rawTypeBeingExemplified,
                file: fileContainingRawTypeReference
            });
            const parsedReferenceToNamedType = fileContainingRawTypeReference.parseTypeReference(named);
            if (parsedReferenceToNamedType.type !== "named") {
                throw new Error("Type reference is not to a named type.");
            }
            const typeName: DeclaredTypeName = {
                typeId: parsedReferenceToNamedType.typeId,
                fernFilepath: parsedReferenceToNamedType.fernFilepath,
                name: parsedReferenceToNamedType.name
            };
            return ExampleTypeReferenceShape.named({
                typeName,
                shape: convertTypeExample({
                    typeName,
                    typeDeclaration: typeDeclaration.declaration,
                    fileContainingType: typeDeclaration.file,
                    fileContainingExample: fileContainingResolvedExample,
                    example: resolvedExample,
                    typeResolver,
                    exampleResolver,
                    workspace
                })
            });
        },
        unknown: () => {
            return ExampleTypeReferenceShape.unknown(jsonExample);
        }
    });

    return {
        shape,
        jsonExample
    };
}

function convertPrimitiveExample({
    example,
    typeBeingExemplified
}: {
    example: RawSchemas.ExampleTypeReferenceSchema;
    typeBeingExemplified: PrimitiveType;
}): ExampleTypeReferenceShape {
    return PrimitiveType._visit(typeBeingExemplified, {
        string: () => {
            if (typeof example !== "string") {
                throw new Error("Example is not a string");
            }
            return ExampleTypeReferenceShape.primitive(
                ExamplePrimitive.string({
                    original: example
                })
            );
        },
        dateTime: () => {
            if (typeof example !== "string") {
                throw new Error("Example is not a string");
            }
            return ExampleTypeReferenceShape.primitive(ExamplePrimitive.datetime(new Date(example)));
        },
        date: () => {
            if (typeof example !== "string") {
                throw new Error("Example is not a string");
            }
            return ExampleTypeReferenceShape.primitive(ExamplePrimitive.date(example));
        },
        base64: () => {
            if (typeof example !== "string") {
                throw new Error("Example is not a string");
            }
            return ExampleTypeReferenceShape.primitive(
                ExamplePrimitive.string({
                    original: example
                })
            );
        },
        integer: () => {
            if (typeof example !== "number") {
                throw new Error("Example is not a number");
            }
            return ExampleTypeReferenceShape.primitive(ExamplePrimitive.integer(example));
        },
        double: () => {
            if (typeof example !== "number") {
                throw new Error("Example is not a number");
            }
            return ExampleTypeReferenceShape.primitive(ExamplePrimitive.double(example));
        },
        long: () => {
            if (typeof example !== "number") {
                throw new Error("Example is not a number");
            }
            return ExampleTypeReferenceShape.primitive(ExamplePrimitive.long(example));
        },
        boolean: () => {
            if (typeof example !== "boolean") {
                throw new Error("Example is not a boolean");
            }
            return ExampleTypeReferenceShape.primitive(ExamplePrimitive.boolean(example));
        },
        uuid: () => {
            if (typeof example !== "string") {
                throw new Error("Example is not a string");
            }
            return ExampleTypeReferenceShape.primitive(ExamplePrimitive.uuid(example));
        },
        _other: () => {
            throw new Error("Unknown primitive type: " + typeBeingExemplified);
        }
    });
}

function convertObject({
    typeName,
    rawObject,
    example,
    fileContainingType,
    fileContainingExample,
    typeResolver,
    exampleResolver,
    workspace
}: {
    typeName: DeclaredTypeName;
    rawObject: RawSchemas.ObjectSchema;
    example: RawSchemas.ExampleTypeValueSchema;
    fileContainingType: FernFileContext;
    fileContainingExample: FernFileContext;
    typeResolver: TypeResolver;
    exampleResolver: ExampleResolver;
    workspace: FernWorkspace;
}): ExampleTypeShape.Object_ {
    if (!isPlainObject(example)) {
        throw new Error("Example is not an object");
    }
    return ExampleTypeShape.object({
        properties:
            rawObject.properties != null
                ? Object.entries(example).reduce<ExampleObjectProperty[]>(
                      (exampleProperties, [wireKey, propertyExample]) => {
                          const originalTypeDeclaration = getOriginalTypeDeclarationForProperty({
                              typeName,
                              wirePropertyKey: wireKey,
                              rawObject,
                              typeResolver,
                              file: fileContainingType
                          });
                          if (originalTypeDeclaration == null) {
                              throw new Error("Could not find original type declaration for property: " + wireKey);
                          }

                          const valueExample = convertTypeReferenceExample({
                              example: propertyExample,
                              fileContainingExample,
                              rawTypeBeingExemplified:
                                  typeof originalTypeDeclaration.rawPropertyType === "string"
                                      ? originalTypeDeclaration.rawPropertyType
                                      : originalTypeDeclaration.rawPropertyType.type,
                              fileContainingRawTypeReference: originalTypeDeclaration.file,
                              typeResolver,
                              exampleResolver,
                              workspace
                          });
                          exampleProperties.push({
                              name: fileContainingExample.casingsGenerator.generateNameAndWireValue({
                                  name: getPropertyName({
                                      propertyKey: wireKey,
                                      property: originalTypeDeclaration.rawPropertyType
                                  }).name,
                                  wireValue: wireKey
                              }),
                              value: valueExample,
                              originalTypeDeclaration: originalTypeDeclaration.typeName
                          });

                          return exampleProperties;
                      },
                      []
                  )
                : []
    });
}

function getOriginalTypeDeclarationForProperty({
    typeName,
    wirePropertyKey,
    rawObject,
    typeResolver,
    file
}: {
    typeName: DeclaredTypeName;
    wirePropertyKey: string;
    rawObject: RawSchemas.ObjectSchema;
    typeResolver: TypeResolver;
    file: FernFileContext;
}):
    | { typeName: DeclaredTypeName; rawPropertyType: string | RawSchemas.ObjectPropertySchema; file: FernFileContext }
    | undefined {
    const rawPropertyType = rawObject.properties?.[wirePropertyKey];
    if (rawPropertyType != null) {
        return { typeName, rawPropertyType, file };
    } else {
        return getOriginalTypeDeclarationForPropertyFromExtensions({
            wirePropertyKey,
            extends_: rawObject.extends,
            typeResolver,
            file
        });
    }
}

export function getOriginalTypeDeclarationForPropertyFromExtensions({
    wirePropertyKey,
    extends_,
    typeResolver,
    file
}: {
    wirePropertyKey: string;
    extends_: string | string[] | undefined;
    typeResolver: TypeResolver;
    file: FernFileContext;
}):
    | { typeName: DeclaredTypeName; rawPropertyType: string | RawSchemas.ObjectPropertySchema; file: FernFileContext }
    | undefined {
    if (extends_ != null) {
        const extendsList = typeof extends_ === "string" ? [extends_] : extends_;
        for (const typeName of extendsList) {
            const resolvedType = typeResolver.resolveNamedTypeOrThrow({
                referenceToNamedType: typeName,
                file
            });
            if (resolvedType._type !== "named" || !isRawObjectDefinition(resolvedType.declaration)) {
                throw new Error("Extension is not of a named object");
            }
            const originalTypeDeclaration = getOriginalTypeDeclarationForProperty({
                wirePropertyKey,
                rawObject: resolvedType.declaration,
                typeResolver,
                typeName: resolvedType.name,
                file: resolvedType.file
            });
            if (originalTypeDeclaration != null) {
                return originalTypeDeclaration;
            }
        }
    }

    return undefined;
}

function convertSingleUnionType({
    rawValueType,
    rawSingleUnionType,
    fileContainingType,
    fileContainingExample,
    typeResolver,
    exampleResolver,
    example,
    discriminant,
    discriminantValueForExample,
    workspace
}: {
    rawValueType: string | undefined;
    rawSingleUnionType: RawSchemas.SingleUnionTypeSchema;
    fileContainingType: FernFileContext;
    fileContainingExample: FernFileContext;
    typeResolver: TypeResolver;
    exampleResolver: ExampleResolver;
    example: RawSchemas.ExampleTypeValueSchema;
    discriminant: string;
    discriminantValueForExample: string;
    workspace: FernWorkspace;
}): ExampleSingleUnionType {
    const wireDiscriminantValue = fileContainingExample.casingsGenerator.generateNameAndWireValue({
        name: getSingleUnionTypeName({ unionKey: discriminantValueForExample, rawSingleUnionType }).name,
        wireValue: discriminantValueForExample
    });
    if (rawValueType == null) {
        return {
            wireDiscriminantValue,
            shape: ExampleSingleUnionTypeProperties.noProperties()
        };
    }

    const parsedSingleUnionTypeProperties = getSingleUnionTypeProperties({
        rawSingleUnionType,
        rawValueType,
        parsedValueType: fileContainingType.parseTypeReference(rawValueType),
        file: fileContainingType,
        typeResolver
    });

    switch (parsedSingleUnionTypeProperties.propertiesType) {
        case "singleProperty": {
            if (!isPlainObject(example)) {
                throw new Error("Example is not an object");
            }
            return {
                wireDiscriminantValue,
                shape: ExampleSingleUnionTypeProperties.singleProperty(
                    convertTypeReferenceExample({
                        example: example[parsedSingleUnionTypeProperties.name.wireValue],
                        rawTypeBeingExemplified: rawValueType,
                        typeResolver,
                        exampleResolver,
                        fileContainingRawTypeReference: fileContainingType,
                        fileContainingExample,
                        workspace
                    })
                )
            };
        }
        case "samePropertiesAsObject": {
            if (!isPlainObject(example)) {
                throw new Error("Example is not an object");
            }
            const { [discriminant]: _discriminantValue, ...nonDiscriminantPropertiesFromExample } = example;
            const rawDeclaration = typeResolver.getDeclarationOfNamedTypeOrThrow({
                referenceToNamedType: rawValueType,
                file: fileContainingType
            });
            if (!isRawObjectDefinition(rawDeclaration.declaration)) {
                throw new Error(`${rawValueType} is not an object`);
            }
            const typeName: DeclaredTypeName = {
                typeId: parsedSingleUnionTypeProperties.typeId,
                fernFilepath: parsedSingleUnionTypeProperties.fernFilepath,
                name: parsedSingleUnionTypeProperties.name
            };
            return {
                wireDiscriminantValue,
                shape: ExampleSingleUnionTypeProperties.samePropertiesAsObject({
                    typeId: IdGenerator.generateTypeId(typeName),
                    object: convertObject({
                        rawObject: rawDeclaration.declaration,
                        example: nonDiscriminantPropertiesFromExample,
                        fileContainingType: rawDeclaration.file,
                        fileContainingExample,
                        typeResolver,
                        exampleResolver,
                        typeName,
                        workspace
                    })
                })
            };
        }
        default:
            assertNever(parsedSingleUnionTypeProperties);
    }
}
