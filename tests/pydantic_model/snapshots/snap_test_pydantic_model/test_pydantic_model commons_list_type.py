# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class ListType(pydantic.BaseModel):
    value_type: VariableType = pydantic.Field(alias="valueType")
    is_fixed_length: typing.Optional[bool] = pydantic.Field(alias="isFixedLength")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ListType.Validators.field("value_type")
            def validate_value_type(v: VariableType, values: ListType.Partial) -> VariableType:
                ...

            @ListType.Validators.field("is_fixed_length")
            def validate_is_fixed_length(v: typing.Optional[bool], values: ListType.Partial) -> typing.Optional[bool]:
                ...
        """

        _value_type_validators: typing.ClassVar[typing.List[ListType.Validators.ValueTypeValidator]] = []
        _is_fixed_length_validators: typing.ClassVar[typing.List[ListType.Validators.IsFixedLengthValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value_type"]
        ) -> typing.Callable[[ListType.Validators.ValueTypeValidator], ListType.Validators.ValueTypeValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["is_fixed_length"]
        ) -> typing.Callable[[ListType.Validators.IsFixedLengthValidator], ListType.Validators.IsFixedLengthValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "value_type":
                    cls._value_type_validators.append(validator)
                if field_name == "is_fixed_length":
                    cls._is_fixed_length_validators.append(validator)
                return validator

            return decorator

        class ValueTypeValidator(typing_extensions.Protocol):
            def __call__(self, v: VariableType, *, values: ListType.Partial) -> VariableType:
                ...

        class IsFixedLengthValidator(typing_extensions.Protocol):
            def __call__(self, v: typing.Optional[bool], *, values: ListType.Partial) -> typing.Optional[bool]:
                ...

    @pydantic.validator("value_type")
    def _validate_value_type(cls, v: VariableType, values: ListType.Partial) -> VariableType:
        for validator in ListType.Validators._value_type_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("is_fixed_length")
    def _validate_is_fixed_length(cls, v: typing.Optional[bool], values: ListType.Partial) -> typing.Optional[bool]:
        for validator in ListType.Validators._is_fixed_length_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        value_type: typing_extensions.NotRequired[VariableType]
        is_fixed_length: typing_extensions.NotRequired[typing.Optional[bool]]

    class Config:
        frozen = True
        allow_population_by_field_name = True


from .variable_type import VariableType  # noqa: E402

ListType.update_forward_refs()
