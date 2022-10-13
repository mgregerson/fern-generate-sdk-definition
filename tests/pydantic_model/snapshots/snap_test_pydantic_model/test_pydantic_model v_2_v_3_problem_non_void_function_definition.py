# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .function_implementation_for_multiple_languages import FunctionImplementationForMultipleLanguages
from .non_void_function_signature import NonVoidFunctionSignature


class NonVoidFunctionDefinition(pydantic.BaseModel):
    signature: NonVoidFunctionSignature
    code: FunctionImplementationForMultipleLanguages

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @NonVoidFunctionDefinition.Validators.field("signature")
            def validate_signature(v: NonVoidFunctionSignature, values: NonVoidFunctionDefinition.Partial) -> NonVoidFunctionSignature:
                ...

            @NonVoidFunctionDefinition.Validators.field("code")
            def validate_code(v: FunctionImplementationForMultipleLanguages, values: NonVoidFunctionDefinition.Partial) -> FunctionImplementationForMultipleLanguages:
                ...
        """

        _signature_validators: typing.ClassVar[
            typing.List[NonVoidFunctionDefinition.Validators.SignatureValidator]
        ] = []
        _code_validators: typing.ClassVar[typing.List[NonVoidFunctionDefinition.Validators.CodeValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["signature"]
        ) -> typing.Callable[
            [NonVoidFunctionDefinition.Validators.SignatureValidator],
            NonVoidFunctionDefinition.Validators.SignatureValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["code"]
        ) -> typing.Callable[
            [NonVoidFunctionDefinition.Validators.CodeValidator], NonVoidFunctionDefinition.Validators.CodeValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "signature":
                    cls._signature_validators.append(validator)
                if field_name == "code":
                    cls._code_validators.append(validator)
                return validator

            return decorator

        class SignatureValidator(typing_extensions.Protocol):
            def __call__(
                self, v: NonVoidFunctionSignature, *, values: NonVoidFunctionDefinition.Partial
            ) -> NonVoidFunctionSignature:
                ...

        class CodeValidator(typing_extensions.Protocol):
            def __call__(
                self, v: FunctionImplementationForMultipleLanguages, *, values: NonVoidFunctionDefinition.Partial
            ) -> FunctionImplementationForMultipleLanguages:
                ...

    @pydantic.validator("signature")
    def _validate_signature(
        cls, v: NonVoidFunctionSignature, values: NonVoidFunctionDefinition.Partial
    ) -> NonVoidFunctionSignature:
        for validator in NonVoidFunctionDefinition.Validators._signature_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("code")
    def _validate_code(
        cls, v: FunctionImplementationForMultipleLanguages, values: NonVoidFunctionDefinition.Partial
    ) -> FunctionImplementationForMultipleLanguages:
        for validator in NonVoidFunctionDefinition.Validators._code_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        signature: typing_extensions.NotRequired[NonVoidFunctionSignature]
        code: typing_extensions.NotRequired[FunctionImplementationForMultipleLanguages]

    class Config:
        frozen = True
