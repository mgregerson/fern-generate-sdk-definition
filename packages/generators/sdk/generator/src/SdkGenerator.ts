import { AbsoluteFilePath } from "@fern-api/fs-utils";
import { IntermediateRepresentation } from "@fern-fern/ir-model/ir";
import { GeneratorContext } from "@fern-typescript/contexts";
import { EndpointTypeSchemasGenerator } from "@fern-typescript/endpoint-type-schemas-generator";
import { EndpointTypesGenerator } from "@fern-typescript/endpoint-types-generator";
import { EnvironmentsGenerator } from "@fern-typescript/environments-generator";
import { ErrorGenerator } from "@fern-typescript/error-generator";
import { ErrorSchemaGenerator } from "@fern-typescript/error-schema-generator";
import { GenericAPIErrorGenerator, TimeoutErrorGenerator } from "@fern-typescript/generic-error-generators";
import { RequestWrapperGenerator } from "@fern-typescript/request-wrapper-generator";
import { ErrorResolver, ServiceResolver, TypeResolver } from "@fern-typescript/resolvers";
import { ServiceGenerator } from "@fern-typescript/service-generator";
import { TypeGenerator } from "@fern-typescript/type-generator";
import { TypeReferenceExampleGenerator } from "@fern-typescript/type-reference-example-generator";
import { TypeSchemaGenerator } from "@fern-typescript/type-schema-generator";
import { Volume } from "memfs/lib/volume";
import { Directory, Project, SourceFile } from "ts-morph";
import { EndpointTypeSchemasContextImpl } from "./contexts/EndpointTypeSchemasContextImpl";
import { EndpointTypesContextImpl } from "./contexts/EndpointTypesContextImpl";
import { EnvironmentsContextImpl } from "./contexts/EnvironmentsContextImpl";
import { ErrorContextImpl } from "./contexts/ErrorContextImpl";
import { ErrorSchemaContextImpl } from "./contexts/ErrorSchemaContextImpl";
import { GenericAPIErrorContextImpl } from "./contexts/GenericAPIErrorContextImpl";
import { RequestWrapperContextImpl } from "./contexts/RequestWrapperContextImpl";
import { ServiceContextImpl } from "./contexts/ServiceContextImpl";
import { TimeoutErrorContextImpl } from "./contexts/TimeoutErrorContextImpl";
import { TypeContextImpl } from "./contexts/TypeContextImpl";
import { TypeSchemaContextImpl } from "./contexts/TypeSchemaContextImpl";
import { CoreUtilitiesManager } from "./core-utilities/CoreUtilitiesManager";
import { EndpointDeclarationReferencer } from "./declaration-referencers/EndpointDeclarationReferencer";
import { EnvironmentsDeclarationReferencer } from "./declaration-referencers/EnvironmentsDeclarationReferencer";
import { ErrorDeclarationReferencer } from "./declaration-referencers/ErrorDeclarationReferencer";
import { GenericAPIErrorDeclarationReferencer } from "./declaration-referencers/GenericAPIErrorDeclarationReferencer";
import { RequestWrapperDeclarationReferencer } from "./declaration-referencers/RequestWrapperDeclarationReferencer";
import { ServiceDeclarationReferencer } from "./declaration-referencers/ServiceDeclarationReferencer";
import { TimeoutErrorDeclarationReferencer } from "./declaration-referencers/TimeoutErrorDeclarationReferencer";
import { TypeDeclarationReferencer } from "./declaration-referencers/TypeDeclarationReferencer";
import { DependencyManager } from "./dependency-manager/DependencyManager";
import {
    convertExportedFilePathToFilePath,
    ExportedDirectory,
    ExportedFilePath,
} from "./exports-manager/ExportedFilePath";
import { ExportsManager } from "./exports-manager/ExportsManager";
import { generateTypeScriptProject } from "./generate-ts-project/generateTypeScriptProject";
import { ImportsManager } from "./imports-manager/ImportsManager";

const FILE_HEADER = `/**
 * This file was auto-generated by Fern from our API Definition.
 */
`;

export declare namespace SdkGenerator {
    export interface Init {
        apiName: string;
        intermediateRepresentation: IntermediateRepresentation;
        context: GeneratorContext;
        volume: Volume;
        packageName: string;
        packageVersion: string | undefined;
        repositoryUrl: string | undefined;
        config: Config;
    }

    export interface Config {
        shouldUseBrandedStringAliases: boolean;
        isPackagePrivate: boolean;
        neverThrowErrors: boolean;
    }
}

export class SdkGenerator {
    private context: GeneratorContext;
    private intermediateRepresentation: IntermediateRepresentation;
    private config: SdkGenerator.Config;

    private rootDirectory: Directory;
    private exportsManager: ExportsManager;
    private dependencyManager = new DependencyManager();
    private coreUtilitiesManager: CoreUtilitiesManager;
    private typeResolver: TypeResolver;
    private errorResolver: ErrorResolver;
    private serviceResolver: ServiceResolver;

    private typeDeclarationReferencer: TypeDeclarationReferencer;
    private typeSchemaDeclarationReferencer: TypeDeclarationReferencer;
    private errorDeclarationReferencer: ErrorDeclarationReferencer;
    private errorSchemaDeclarationReferencer: ErrorDeclarationReferencer;
    private serviceDeclarationReferencer: ServiceDeclarationReferencer;
    private endpointDeclarationReferencer: EndpointDeclarationReferencer;
    private requestWrapperDeclarationReferencer: RequestWrapperDeclarationReferencer;
    private endpointSchemaDeclarationReferencer: EndpointDeclarationReferencer;
    private environmentsDeclarationReferencer: EnvironmentsDeclarationReferencer;
    private genericAPIErrorDeclarationReferencer: GenericAPIErrorDeclarationReferencer;
    private timeoutErrorDeclarationReferencer: TimeoutErrorDeclarationReferencer;

    private typeGenerator: TypeGenerator;
    private typeSchemaGenerator: TypeSchemaGenerator;
    private typeReferenceExampleGenerator: TypeReferenceExampleGenerator;
    private errorGenerator: ErrorGenerator;
    private errorSchemaGenerator: ErrorSchemaGenerator;
    private endpointTypesGenerator: EndpointTypesGenerator;
    private requestWrapperGenerator: RequestWrapperGenerator;
    private endpointTypeSchemasGenerator: EndpointTypeSchemasGenerator;
    private environmentsGenerator: EnvironmentsGenerator;
    private serviceGenerator: ServiceGenerator;
    private genericAPIErrorGenerator: GenericAPIErrorGenerator;
    private timeoutErrorGenerator: TimeoutErrorGenerator;

    private generatePackage: () => Promise<void>;

    constructor({
        apiName,
        intermediateRepresentation,
        context,
        volume,
        packageName,
        packageVersion,
        repositoryUrl,
        config,
    }: SdkGenerator.Init) {
        this.context = context;
        this.intermediateRepresentation = intermediateRepresentation;
        this.config = config;

        this.exportsManager = new ExportsManager({ packageName });
        this.coreUtilitiesManager = new CoreUtilitiesManager({ apiName, packageName });

        const project = new Project({
            useInMemoryFileSystem: true,
        });
        this.rootDirectory = project.createDirectory("/");
        this.typeResolver = new TypeResolver(intermediateRepresentation);
        this.errorResolver = new ErrorResolver(intermediateRepresentation);
        this.serviceResolver = new ServiceResolver(intermediateRepresentation);

        const apiDirectory: ExportedDirectory[] = [
            {
                nameOnDisk: "api",
                exportDeclaration: { namespaceExport: apiName },
            },
        ];

        const schemaDirectory: ExportedDirectory[] = [
            {
                nameOnDisk: "serialization",
            },
        ];

        this.typeDeclarationReferencer = new TypeDeclarationReferencer({
            containingDirectory: apiDirectory,
            packageName,
            apiName,
        });
        this.typeSchemaDeclarationReferencer = new TypeDeclarationReferencer({
            containingDirectory: schemaDirectory,
            packageName,
            apiName,
        });
        this.errorDeclarationReferencer = new ErrorDeclarationReferencer({
            containingDirectory: apiDirectory,
            packageName,
            apiName,
        });
        this.errorSchemaDeclarationReferencer = new ErrorDeclarationReferencer({
            containingDirectory: schemaDirectory,
            packageName,
            apiName,
        });
        this.serviceDeclarationReferencer = new ServiceDeclarationReferencer({
            apiName,
            containingDirectory: apiDirectory,
            packageName,
        });
        this.endpointDeclarationReferencer = new EndpointDeclarationReferencer({
            containingDirectory: apiDirectory,
            packageName,
            apiName,
        });
        this.requestWrapperDeclarationReferencer = new RequestWrapperDeclarationReferencer({
            containingDirectory: apiDirectory,
            packageName,
            apiName,
        });
        this.endpointSchemaDeclarationReferencer = new EndpointDeclarationReferencer({
            containingDirectory: schemaDirectory,
            packageName,
            apiName,
        });
        this.environmentsDeclarationReferencer = new EnvironmentsDeclarationReferencer({
            containingDirectory: [],
            packageName,
            apiName,
            environmentsConfig: intermediateRepresentation.environments ?? undefined,
        });
        this.genericAPIErrorDeclarationReferencer = new GenericAPIErrorDeclarationReferencer({
            containingDirectory: [],
            packageName,
            apiName,
        });
        this.timeoutErrorDeclarationReferencer = new TimeoutErrorDeclarationReferencer({
            containingDirectory: [],
            packageName,
            apiName,
        });

        this.typeGenerator = new TypeGenerator({ useBrandedStringAliases: config.shouldUseBrandedStringAliases });
        this.typeSchemaGenerator = new TypeSchemaGenerator();
        this.typeReferenceExampleGenerator = new TypeReferenceExampleGenerator();
        this.errorGenerator = new ErrorGenerator({
            useBrandedStringAliases: config.shouldUseBrandedStringAliases,
            neverThrowErrors: config.neverThrowErrors,
        });
        this.errorSchemaGenerator = new ErrorSchemaGenerator({
            errorGenerator: this.errorGenerator,
        });
        this.endpointTypesGenerator = new EndpointTypesGenerator({
            errorResolver: this.errorResolver,
            intermediateRepresentation,
            neverThrowErrors: config.neverThrowErrors,
        });
        this.endpointTypeSchemasGenerator = new EndpointTypeSchemasGenerator({
            errorResolver: this.errorResolver,
            intermediateRepresentation,
        });
        this.requestWrapperGenerator = new RequestWrapperGenerator();
        this.environmentsGenerator = new EnvironmentsGenerator();
        this.serviceGenerator = new ServiceGenerator({
            intermediateRepresentation: this.intermediateRepresentation,
            errorResolver: this.errorResolver,
            neverThrowErrors: config.neverThrowErrors,
        });
        this.genericAPIErrorGenerator = new GenericAPIErrorGenerator();
        this.timeoutErrorGenerator = new TimeoutErrorGenerator();

        this.generatePackage = async () => {
            await generateTypeScriptProject({
                volume,
                packageName,
                packageVersion,
                isPackagePrivate: config.isPackagePrivate,
                project,
                dependencies: this.dependencyManager.getDependencies(),
                repositoryUrl,
            });
        };
    }

    public async generate(): Promise<void> {
        this.generateTypeDeclarations();
        this.generateTypeSchemas();
        this.generateErrorDeclarations();
        this.generateErrorSchemas();
        this.generateEndpointTypes();
        this.generateEndpointTypeSchemas();
        this.generateServiceDeclarations();
        this.generateEnvironments();

        if (!this.config.neverThrowErrors) {
            this.generateGenericAPIError();
            this.generateTimeoutError();
        }

        this.coreUtilitiesManager.finalize(this.exportsManager, this.dependencyManager);
        this.exportsManager.writeExportsToProject(this.rootDirectory);
        await this.generatePackage();
    }

    public async copyCoreUtilities({ pathToPackage }: { pathToPackage: AbsoluteFilePath }): Promise<void> {
        await this.coreUtilitiesManager.copyCoreUtilities({ pathToPackage });
    }

    private generateTypeDeclarations() {
        for (const typeDeclaration of this.intermediateRepresentation.types) {
            this.withSourceFile({
                filepath: this.typeDeclarationReferencer.getExportedFilepath(typeDeclaration.name),
                run: ({ sourceFile, importsManager }) => {
                    const typeContext = new TypeContextImpl({
                        sourceFile,
                        coreUtilitiesManager: this.coreUtilitiesManager,
                        dependencyManager: this.dependencyManager,
                        fernConstants: this.intermediateRepresentation.constants,
                        importsManager,
                        typeResolver: this.typeResolver,
                        typeDeclarationReferencer: this.typeDeclarationReferencer,
                        typeGenerator: this.typeGenerator,
                        typeReferenceExampleGenerator: this.typeReferenceExampleGenerator,
                    });
                    typeContext.type.getGeneratedType(typeDeclaration.name).writeToFile(typeContext);
                },
            });
        }
    }

    private generateTypeSchemas() {
        for (const typeDeclaration of this.intermediateRepresentation.types) {
            this.withSourceFile({
                filepath: this.typeSchemaDeclarationReferencer.getExportedFilepath(typeDeclaration.name),
                run: ({ sourceFile, importsManager }) => {
                    const typeSchemaContext = new TypeSchemaContextImpl({
                        sourceFile,
                        coreUtilitiesManager: this.coreUtilitiesManager,
                        dependencyManager: this.dependencyManager,
                        fernConstants: this.intermediateRepresentation.constants,
                        importsManager,
                        typeResolver: this.typeResolver,
                        typeDeclarationReferencer: this.typeDeclarationReferencer,
                        typeSchemaDeclarationReferencer: this.typeSchemaDeclarationReferencer,
                        typeGenerator: this.typeGenerator,
                        typeSchemaGenerator: this.typeSchemaGenerator,
                        typeReferenceExampleGenerator: this.typeReferenceExampleGenerator,
                    });
                    typeSchemaContext.typeSchema
                        .getGeneratedTypeSchema(typeDeclaration.name)
                        .writeToFile(typeSchemaContext);
                },
            });
        }
    }

    private generateErrorDeclarations() {
        for (const errorDeclaration of this.intermediateRepresentation.errors) {
            this.withSourceFile({
                filepath: this.errorDeclarationReferencer.getExportedFilepath(errorDeclaration.name),
                run: ({ sourceFile, importsManager }) => {
                    const errorContext = new ErrorContextImpl({
                        sourceFile,
                        coreUtilitiesManager: this.coreUtilitiesManager,
                        dependencyManager: this.dependencyManager,
                        fernConstants: this.intermediateRepresentation.constants,
                        importsManager,
                        typeResolver: this.typeResolver,
                        typeDeclarationReferencer: this.typeDeclarationReferencer,
                        typeGenerator: this.typeGenerator,
                        typeReferenceExampleGenerator: this.typeReferenceExampleGenerator,
                        errorDeclarationReferencer: this.errorDeclarationReferencer,
                        errorGenerator: this.errorGenerator,
                        errorResolver: this.errorResolver,
                    });
                    errorContext.error.getGeneratedError(errorDeclaration.name)?.writeToFile(errorContext);
                },
            });
        }
    }

    private generateErrorSchemas() {
        for (const errorDeclaration of this.intermediateRepresentation.errors) {
            this.withSourceFile({
                filepath: this.errorSchemaDeclarationReferencer.getExportedFilepath(errorDeclaration.name),
                run: ({ sourceFile, importsManager }) => {
                    const errorSchemaContext = new ErrorSchemaContextImpl({
                        sourceFile,
                        coreUtilitiesManager: this.coreUtilitiesManager,
                        dependencyManager: this.dependencyManager,
                        fernConstants: this.intermediateRepresentation.constants,
                        importsManager,
                        typeResolver: this.typeResolver,
                        typeDeclarationReferencer: this.typeDeclarationReferencer,
                        typeSchemaDeclarationReferencer: this.typeSchemaDeclarationReferencer,
                        typeReferenceExampleGenerator: this.typeReferenceExampleGenerator,
                        errorDeclarationReferencer: this.errorDeclarationReferencer,
                        errorGenerator: this.errorGenerator,
                        errorResolver: this.errorResolver,
                        typeGenerator: this.typeGenerator,
                        typeSchemaGenerator: this.typeSchemaGenerator,
                        errorSchemaDeclarationReferencer: this.errorSchemaDeclarationReferencer,
                        errorSchemaGenerator: this.errorSchemaGenerator,
                    });
                    errorSchemaContext.errorSchema
                        .getGeneratedErrorSchema(errorDeclaration.name)
                        ?.writeToFile(errorSchemaContext);
                },
            });
        }
    }

    private generateEndpointTypes() {
        for (const service of this.intermediateRepresentation.services) {
            for (const endpoint of service.endpoints) {
                this.withSourceFile({
                    filepath: this.endpointDeclarationReferencer.getExportedFilepath({
                        service: service.name.fernFilepath,
                        endpoint,
                    }),
                    run: ({ sourceFile, importsManager }) => {
                        const endpointTypesContext = new EndpointTypesContextImpl({
                            sourceFile,
                            coreUtilitiesManager: this.coreUtilitiesManager,
                            dependencyManager: this.dependencyManager,
                            fernConstants: this.intermediateRepresentation.constants,
                            importsManager,
                            typeResolver: this.typeResolver,
                            typeDeclarationReferencer: this.typeDeclarationReferencer,
                            typeReferenceExampleGenerator: this.typeReferenceExampleGenerator,
                            errorDeclarationReferencer: this.errorDeclarationReferencer,
                            endpointDeclarationReferencer: this.endpointDeclarationReferencer,
                            errorGenerator: this.errorGenerator,
                            errorResolver: this.errorResolver,
                            typeGenerator: this.typeGenerator,
                            serviceResolver: this.serviceResolver,
                            endpointTypesGenerator: this.endpointTypesGenerator,
                        });
                        endpointTypesContext.endpointTypes
                            .getGeneratedEndpointTypes(service.name.fernFilepath, endpoint.name)
                            .writeToFile(endpointTypesContext);
                    },
                });
                if (endpoint.sdkRequest?.shape.type === "wrapper") {
                    this.withSourceFile({
                        filepath: this.requestWrapperDeclarationReferencer.getExportedFilepath({
                            service: service.name.fernFilepath,
                            endpoint,
                        }),
                        run: ({ sourceFile, importsManager }) => {
                            const context = new RequestWrapperContextImpl({
                                sourceFile,
                                coreUtilitiesManager: this.coreUtilitiesManager,
                                dependencyManager: this.dependencyManager,
                                fernConstants: this.intermediateRepresentation.constants,
                                importsManager,
                                typeResolver: this.typeResolver,
                                typeDeclarationReferencer: this.typeDeclarationReferencer,
                                typeReferenceExampleGenerator: this.typeReferenceExampleGenerator,
                                typeGenerator: this.typeGenerator,
                                errorDeclarationReferencer: this.errorDeclarationReferencer,
                                errorGenerator: this.errorGenerator,
                                errorResolver: this.errorResolver,
                                serviceResolver: this.serviceResolver,
                                endpointDeclarationReferencer: this.endpointDeclarationReferencer,
                                endpointTypesGenerator: this.endpointTypesGenerator,
                                requestWrapperDeclarationReferencer: this.requestWrapperDeclarationReferencer,
                                requestWrapperGenerator: this.requestWrapperGenerator,
                            });
                            context.requestWrapper
                                .getGeneratedRequestWrapper(service.name.fernFilepath, endpoint.name)
                                .writeToFile(context);
                        },
                    });
                }
            }
        }
    }

    private generateEndpointTypeSchemas() {
        for (const service of this.intermediateRepresentation.services) {
            for (const endpoint of service.endpoints) {
                this.withSourceFile({
                    filepath: this.endpointSchemaDeclarationReferencer.getExportedFilepath({
                        service: service.name.fernFilepath,
                        endpoint,
                    }),
                    run: ({ sourceFile, importsManager }) => {
                        const endpointTypeSchemasContext = new EndpointTypeSchemasContextImpl({
                            sourceFile,
                            coreUtilitiesManager: this.coreUtilitiesManager,
                            dependencyManager: this.dependencyManager,
                            fernConstants: this.intermediateRepresentation.constants,
                            importsManager,
                            typeResolver: this.typeResolver,
                            typeDeclarationReferencer: this.typeDeclarationReferencer,
                            typeSchemaDeclarationReferencer: this.typeSchemaDeclarationReferencer,
                            typeReferenceExampleGenerator: this.typeReferenceExampleGenerator,
                            errorDeclarationReferencer: this.errorDeclarationReferencer,
                            errorSchemaDeclarationReferencer: this.errorSchemaDeclarationReferencer,
                            endpointSchemaDeclarationReferencer: this.endpointSchemaDeclarationReferencer,
                            endpointDeclarationReferencer: this.endpointDeclarationReferencer,
                            endpointTypesGenerator: this.endpointTypesGenerator,
                            requestWrapperDeclarationReferencer: this.requestWrapperDeclarationReferencer,
                            requestWrapperGenerator: this.requestWrapperGenerator,
                            typeGenerator: this.typeGenerator,
                            errorGenerator: this.errorGenerator,
                            errorResolver: this.errorResolver,
                            serviceResolver: this.serviceResolver,
                            endpointTypeSchemasGenerator: this.endpointTypeSchemasGenerator,
                            typeSchemaGenerator: this.typeSchemaGenerator,
                            errorSchemaGenerator: this.errorSchemaGenerator,
                        });
                        endpointTypeSchemasContext.endpointTypeSchemas
                            .getGeneratedEndpointTypeSchemas(service.name.fernFilepath, endpoint.name)
                            .writeToFile(endpointTypeSchemasContext);
                    },
                });
            }
        }
    }

    private generateServiceDeclarations() {
        const services = this.serviceResolver.getAllAugmentedServices();
        for (const service of services) {
            this.withSourceFile({
                filepath: this.serviceDeclarationReferencer.getExportedFilepath(service.fernFilepath),
                run: ({ sourceFile, importsManager }) => {
                    const serviceContext = new ServiceContextImpl({
                        intermediateRepresentation: this.intermediateRepresentation,
                        sourceFile,
                        coreUtilitiesManager: this.coreUtilitiesManager,
                        dependencyManager: this.dependencyManager,
                        fernConstants: this.intermediateRepresentation.constants,
                        importsManager,
                        typeResolver: this.typeResolver,
                        typeDeclarationReferencer: this.typeDeclarationReferencer,
                        typeSchemaDeclarationReferencer: this.typeSchemaDeclarationReferencer,
                        typeReferenceExampleGenerator: this.typeReferenceExampleGenerator,
                        errorDeclarationReferencer: this.errorDeclarationReferencer,
                        errorSchemaDeclarationReferencer: this.errorSchemaDeclarationReferencer,
                        endpointDeclarationReferencer: this.endpointDeclarationReferencer,
                        endpointSchemaDeclarationReferencer: this.endpointSchemaDeclarationReferencer,
                        endpointTypesGenerator: this.endpointTypesGenerator,
                        requestWrapperDeclarationReferencer: this.requestWrapperDeclarationReferencer,
                        requestWrapperGenerator: this.requestWrapperGenerator,
                        typeGenerator: this.typeGenerator,
                        errorGenerator: this.errorGenerator,
                        errorResolver: this.errorResolver,
                        serviceResolver: this.serviceResolver,
                        endpointTypeSchemasGenerator: this.endpointTypeSchemasGenerator,
                        typeSchemaGenerator: this.typeSchemaGenerator,
                        errorSchemaGenerator: this.errorSchemaGenerator,
                        environmentsGenerator: this.environmentsGenerator,
                        environmentsDeclarationReferencer: this.environmentsDeclarationReferencer,
                        serviceDeclarationReferencer: this.serviceDeclarationReferencer,
                        serviceGenerator: this.serviceGenerator,
                        genericAPIErrorDeclarationReferencer: this.genericAPIErrorDeclarationReferencer,
                        genericAPIErrorGenerator: this.genericAPIErrorGenerator,
                        timeoutErrorDeclarationReferencer: this.timeoutErrorDeclarationReferencer,
                        timeoutErrorGenerator: this.timeoutErrorGenerator,
                    });
                    serviceContext.service.getGeneratedService(service.fernFilepath).writeToFile(serviceContext);
                },
            });
        }
    }

    private generateEnvironments(): void {
        this.withSourceFile({
            filepath: this.environmentsDeclarationReferencer.getExportedFilepath(),
            run: ({ sourceFile, importsManager }) => {
                const environmentsContext = new EnvironmentsContextImpl({
                    sourceFile,
                    coreUtilitiesManager: this.coreUtilitiesManager,
                    dependencyManager: this.dependencyManager,
                    fernConstants: this.intermediateRepresentation.constants,
                    importsManager,
                    intermediateRepresentation: this.intermediateRepresentation,
                    environmentsGenerator: this.environmentsGenerator,
                    environmentsDeclarationReferencer: this.environmentsDeclarationReferencer,
                });
                environmentsContext.environments.getGeneratedEnvironments().writeToFile(environmentsContext);
            },
        });
    }

    private generateGenericAPIError(): void {
        this.withSourceFile({
            filepath: this.genericAPIErrorDeclarationReferencer.getExportedFilepath(),
            run: ({ sourceFile, importsManager }) => {
                const context = new GenericAPIErrorContextImpl({
                    sourceFile,
                    coreUtilitiesManager: this.coreUtilitiesManager,
                    dependencyManager: this.dependencyManager,
                    fernConstants: this.intermediateRepresentation.constants,
                    importsManager,
                    genericAPIErrorDeclarationReferencer: this.genericAPIErrorDeclarationReferencer,
                    genericAPIErrorGenerator: this.genericAPIErrorGenerator,
                });
                this.genericAPIErrorGenerator
                    .generateGenericAPIError({
                        errorClassName: this.genericAPIErrorDeclarationReferencer.getExportedName(),
                    })
                    .writeToFile(context);
            },
        });
    }

    private generateTimeoutError(): void {
        this.withSourceFile({
            filepath: this.timeoutErrorDeclarationReferencer.getExportedFilepath(),
            run: ({ sourceFile, importsManager }) => {
                const context = new TimeoutErrorContextImpl({
                    sourceFile,
                    coreUtilitiesManager: this.coreUtilitiesManager,
                    dependencyManager: this.dependencyManager,
                    fernConstants: this.intermediateRepresentation.constants,
                    importsManager,
                    timeoutErrorDeclarationReferencer: this.timeoutErrorDeclarationReferencer,
                    timeoutErrorGenerator: this.timeoutErrorGenerator,
                });
                this.timeoutErrorGenerator
                    .generateTimeoutError({
                        errorClassName: this.timeoutErrorDeclarationReferencer.getExportedName(),
                    })
                    .writeToFile(context);
            },
        });
    }

    private withSourceFile({
        run,
        filepath,
    }: {
        run: (args: { sourceFile: SourceFile; importsManager: ImportsManager }) => void;
        filepath: ExportedFilePath;
    }) {
        const filepathStr = convertExportedFilePathToFilePath(filepath);
        this.context.logger.debug(`Generating ${filepathStr}`);

        const sourceFile = this.rootDirectory.createSourceFile(filepathStr);
        const importsManager = new ImportsManager();

        run({ sourceFile, importsManager });

        if (sourceFile.getStatements().length === 0) {
            sourceFile.delete();
            this.context.logger.debug(`Skipping ${filepathStr} (no content)`);
        } else {
            importsManager.writeImportsToSourceFile(sourceFile);
            this.exportsManager.addExportsForFilepath(filepath);

            // this needs to be last.
            // https://github.com/dsherret/ts-morph/issues/189#issuecomment-414174283
            sourceFile.insertText(0, (writer) => {
                writer.writeLine(FILE_HEADER);
            });

            this.context.logger.debug(`Generated ${filepathStr}`);
        }
    }
}
