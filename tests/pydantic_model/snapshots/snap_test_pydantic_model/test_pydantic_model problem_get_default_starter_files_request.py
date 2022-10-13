# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.variable_type import VariableType
from .variable_type_and_name import VariableTypeAndName


class GetDefaultStarterFilesRequest(pydantic.BaseModel):
    input_params: typing.List[VariableTypeAndName] = pydantic.Field(alias="inputParams")
    output_type: VariableType = pydantic.Field(alias="outputType")
    method_name: str = pydantic.Field(alias="methodName")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetDefaultStarterFilesRequest.Validators.field("input_params")
            def validate_input_params(v: typing.List[VariableTypeAndName], values: GetDefaultStarterFilesRequest.Partial) -> typing.List[VariableTypeAndName]:
                ...

            @GetDefaultStarterFilesRequest.Validators.field("output_type")
            def validate_output_type(v: VariableType, values: GetDefaultStarterFilesRequest.Partial) -> VariableType:
                ...

            @GetDefaultStarterFilesRequest.Validators.field("method_name")
            def validate_method_name(v: str, values: GetDefaultStarterFilesRequest.Partial) -> str:
                ...
        """

        _input_params_validators: typing.ClassVar[
            typing.List[GetDefaultStarterFilesRequest.Validators.InputParamsValidator]
        ] = []
        _output_type_validators: typing.ClassVar[
            typing.List[GetDefaultStarterFilesRequest.Validators.OutputTypeValidator]
        ] = []
        _method_name_validators: typing.ClassVar[
            typing.List[GetDefaultStarterFilesRequest.Validators.MethodNameValidator]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["input_params"]
        ) -> typing.Callable[
            [GetDefaultStarterFilesRequest.Validators.InputParamsValidator],
            GetDefaultStarterFilesRequest.Validators.InputParamsValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["output_type"]
        ) -> typing.Callable[
            [GetDefaultStarterFilesRequest.Validators.OutputTypeValidator],
            GetDefaultStarterFilesRequest.Validators.OutputTypeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"]
        ) -> typing.Callable[
            [GetDefaultStarterFilesRequest.Validators.MethodNameValidator],
            GetDefaultStarterFilesRequest.Validators.MethodNameValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "input_params":
                    cls._input_params_validators.append(validator)
                if field_name == "output_type":
                    cls._output_type_validators.append(validator)
                if field_name == "method_name":
                    cls._method_name_validators.append(validator)
                return validator

            return decorator

        class InputParamsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[VariableTypeAndName], *, values: GetDefaultStarterFilesRequest.Partial
            ) -> typing.List[VariableTypeAndName]:
                ...

        class OutputTypeValidator(typing_extensions.Protocol):
            def __call__(self, v: VariableType, *, values: GetDefaultStarterFilesRequest.Partial) -> VariableType:
                ...

        class MethodNameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: GetDefaultStarterFilesRequest.Partial) -> str:
                ...

    @pydantic.validator("input_params")
    def _validate_input_params(
        cls, v: typing.List[VariableTypeAndName], values: GetDefaultStarterFilesRequest.Partial
    ) -> typing.List[VariableTypeAndName]:
        for validator in GetDefaultStarterFilesRequest.Validators._input_params_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("output_type")
    def _validate_output_type(cls, v: VariableType, values: GetDefaultStarterFilesRequest.Partial) -> VariableType:
        for validator in GetDefaultStarterFilesRequest.Validators._output_type_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("method_name")
    def _validate_method_name(cls, v: str, values: GetDefaultStarterFilesRequest.Partial) -> str:
        for validator in GetDefaultStarterFilesRequest.Validators._method_name_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        input_params: typing_extensions.NotRequired[typing.List[VariableTypeAndName]]
        output_type: typing_extensions.NotRequired[VariableType]
        method_name: typing_extensions.NotRequired[str]

    class Config:
        frozen = True
        allow_population_by_field_name = True
