/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as SeedTrace from "../../../../api";
import * as core from "../../../../core";

export const ErrorInfo: core.serialization.Schema<serializers.ErrorInfo.Raw, SeedTrace.ErrorInfo> = core.serialization
    .union("type", {
        compileError: core.serialization.lazyObject(async () => (await import("../../..")).CompileError),
        runtimeError: core.serialization.lazyObject(async () => (await import("../../..")).RuntimeError),
        internalError: core.serialization.lazyObject(async () => (await import("../../..")).InternalError),
    })
    .transform<SeedTrace.ErrorInfo>({
        transform: (value) => {
            switch (value.type) {
                case "compileError":
                    return SeedTrace.ErrorInfo.compileError(value);
                case "runtimeError":
                    return SeedTrace.ErrorInfo.runtimeError(value);
                case "internalError":
                    return SeedTrace.ErrorInfo.internalError(value);
                default:
                    return SeedTrace.ErrorInfo._unknown(value);
            }
        },
        untransform: ({ _visit, ...value }) => value as any,
    });

export declare namespace ErrorInfo {
    type Raw = ErrorInfo.CompileError | ErrorInfo.RuntimeError | ErrorInfo.InternalError;

    interface CompileError extends serializers.CompileError.Raw {
        type: "compileError";
    }

    interface RuntimeError extends serializers.RuntimeError.Raw {
        type: "runtimeError";
    }

    interface InternalError extends serializers.InternalError.Raw {
        type: "internalError";
    }
}
