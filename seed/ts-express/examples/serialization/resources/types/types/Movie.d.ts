/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../..";
import * as SeedExamples from "../../../../api";
import * as core from "../../../../core";
export declare const Movie: core.serialization.ObjectSchema<serializers.Movie.Raw, SeedExamples.Movie>;
export declare namespace Movie {
    interface Raw {
        id: serializers.MovieId.Raw;
        prequel?: serializers.MovieId.Raw | null;
        title: string;
        from: string;
        rating: number;
        type: "movie";
        tag: serializers.commons.Tag.Raw;
        book?: string | null;
        metadata: Record<string, unknown>;
    }
}
