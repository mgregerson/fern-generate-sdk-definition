package com.seed.exhaustive.resources.types.union.types;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.exhaustive.core.ObjectMappers;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(builder = Dog.Builder.class)
public final class Dog {
    private final String name;

    private final boolean likesToWoof;

    private Dog(String name, boolean likesToWoof) {
        this.name = name;
        this.likesToWoof = likesToWoof;
    }

    @JsonProperty("name")
    public String getName() {
        return name;
    }

    @JsonProperty("likesToWoof")
    public boolean getLikesToWoof() {
        return likesToWoof;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof Dog && equalTo((Dog) other);
    }

    private boolean equalTo(Dog other) {
        return name.equals(other.name) && likesToWoof == other.likesToWoof;
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.name, this.likesToWoof);
    }

    @Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static NameStage builder() {
        return new Builder();
    }

    public interface NameStage {
        LikesToWoofStage name(String name);

        Builder from(Dog other);
    }

    public interface LikesToWoofStage {
        _FinalStage likesToWoof(boolean likesToWoof);
    }

    public interface _FinalStage {
        Dog build();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder implements NameStage, LikesToWoofStage, _FinalStage {
        private String name;

        private boolean likesToWoof;

        private Builder() {}

        @Override
        public Builder from(Dog other) {
            name(other.getName());
            likesToWoof(other.getLikesToWoof());
            return this;
        }

        @Override
        @JsonSetter("name")
        public LikesToWoofStage name(String name) {
            this.name = name;
            return this;
        }

        @Override
        @JsonSetter("likesToWoof")
        public _FinalStage likesToWoof(boolean likesToWoof) {
            this.likesToWoof = likesToWoof;
            return this;
        }

        @Override
        public Dog build() {
            return new Dog(name, likesToWoof);
        }
    }
}
