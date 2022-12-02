import { HttpEndpoint, HttpService } from "@fern-fern/ir-model/services/http";
import { ErrorResolver } from "@fern-typescript/resolvers";
import { EndpointTypeSchemasContext, GeneratedEndpointTypeSchemas } from "@fern-typescript/sdk-declaration-handler";
import { ts } from "ts-morph";
import { GeneratedEndpointErrorSchema } from "./GeneratedEndpointErrorSchema";
import { GeneratedEndpointTypeSchema } from "./GeneratedEndpointTypeSchema";

export declare namespace GeneratedEndpointTypeSchemasImpl {
    export interface Init {
        service: HttpService;
        endpoint: HttpEndpoint;
        errorResolver: ErrorResolver;
    }
}

export class GeneratedEndpointTypeSchemasImpl implements GeneratedEndpointTypeSchemas {
    private static REQUEST_SCHEMA_NAME = "Request";
    private static RESPONSE_SCHEMA_NAME = "Response";

    private generatedRequestSchema: GeneratedEndpointTypeSchema | undefined;
    private generatedResponseSchema: GeneratedEndpointTypeSchema | undefined;
    private generatedErrorSchema: GeneratedEndpointErrorSchema;

    constructor({ service, endpoint, errorResolver }: GeneratedEndpointTypeSchemasImpl.Init) {
        this.generatedRequestSchema =
            endpoint.request.typeV2 != null
                ? new GeneratedEndpointTypeSchema({
                      service,
                      endpoint,
                      typeName: GeneratedEndpointTypeSchemasImpl.REQUEST_SCHEMA_NAME,
                      type: endpoint.request.typeV2,
                  })
                : undefined;
        this.generatedResponseSchema =
            endpoint.response.typeV2 != null
                ? new GeneratedEndpointTypeSchema({
                      service,
                      endpoint,
                      typeName: GeneratedEndpointTypeSchemasImpl.RESPONSE_SCHEMA_NAME,
                      type: endpoint.response.typeV2,
                  })
                : undefined;
        this.generatedErrorSchema = new GeneratedEndpointErrorSchema({ service, endpoint, errorResolver });
    }

    public writeToFile(context: EndpointTypeSchemasContext): void {
        if (this.generatedRequestSchema != null) {
            this.generatedRequestSchema.writeSchemaToFile(context);
            context.base.sourceFile.addStatements("\n");
        }

        if (this.generatedResponseSchema != null) {
            this.generatedResponseSchema.writeSchemaToFile(context);
            context.base.sourceFile.addStatements("\n");
        }

        this.generatedErrorSchema.writeToFile(context);
    }

    public getReferenceToRawResponse(context: EndpointTypeSchemasContext): ts.TypeNode {
        if (this.generatedResponseSchema == null) {
            throw new Error("No response schema was generated");
        }
        return this.generatedResponseSchema.getReferenceToRawShape(context);
    }

    public getReferenceToRawError(context: EndpointTypeSchemasContext): ts.TypeNode {
        return this.generatedErrorSchema.getReferenceToRawShape(context);
    }

    public serializeRequest(
        referenceToParsedRequest: ts.Expression,
        context: EndpointTypeSchemasContext
    ): ts.Expression {
        if (this.generatedRequestSchema == null) {
            throw new Error("No request schema was generated");
        }
        return this.generatedRequestSchema.getReferenceToZurgSchema(context).json(referenceToParsedRequest);
    }

    public deserializeResponse(
        referenceToRawResponse: ts.Expression,
        context: EndpointTypeSchemasContext
    ): ts.Expression {
        if (this.generatedResponseSchema == null) {
            throw new Error("No response schema was generated");
        }
        return this.generatedResponseSchema.getReferenceToZurgSchema(context).parse(referenceToRawResponse);
    }

    public deserializeError(referenceToRawError: ts.Expression, context: EndpointTypeSchemasContext): ts.Expression {
        return this.generatedErrorSchema.getReferenceToZurgSchema(context).parse(referenceToRawError);
    }
}
