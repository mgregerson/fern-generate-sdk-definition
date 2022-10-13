# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2


class WorkspaceRunDetails(pydantic.BaseModel):
    exception_v_2: typing.Optional[ExceptionV2] = pydantic.Field(alias="exceptionV2")
    exception: typing.Optional[ExceptionInfo]
    stdout: str

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceRunDetails.Validators.field("exception_v_2")
            def validate_exception_v_2(v: typing.Optional[ExceptionV2], values: WorkspaceRunDetails.Partial) -> typing.Optional[ExceptionV2]:
                ...

            @WorkspaceRunDetails.Validators.field("exception")
            def validate_exception(v: typing.Optional[ExceptionInfo], values: WorkspaceRunDetails.Partial) -> typing.Optional[ExceptionInfo]:
                ...

            @WorkspaceRunDetails.Validators.field("stdout")
            def validate_stdout(v: str, values: WorkspaceRunDetails.Partial) -> str:
                ...
        """

        _exception_v_2_validators: typing.ClassVar[
            typing.List[WorkspaceRunDetails.Validators.ExceptionV2Validator]
        ] = []
        _exception_validators: typing.ClassVar[typing.List[WorkspaceRunDetails.Validators.ExceptionValidator]] = []
        _stdout_validators: typing.ClassVar[typing.List[WorkspaceRunDetails.Validators.StdoutValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["exception_v_2"]
        ) -> typing.Callable[
            [WorkspaceRunDetails.Validators.ExceptionV2Validator], WorkspaceRunDetails.Validators.ExceptionV2Validator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["exception"]
        ) -> typing.Callable[
            [WorkspaceRunDetails.Validators.ExceptionValidator], WorkspaceRunDetails.Validators.ExceptionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"]
        ) -> typing.Callable[
            [WorkspaceRunDetails.Validators.StdoutValidator], WorkspaceRunDetails.Validators.StdoutValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "exception_v_2":
                    cls._exception_v_2_validators.append(validator)
                if field_name == "exception":
                    cls._exception_validators.append(validator)
                if field_name == "stdout":
                    cls._stdout_validators.append(validator)
                return validator

            return decorator

        class ExceptionV2Validator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[ExceptionV2], *, values: WorkspaceRunDetails.Partial
            ) -> typing.Optional[ExceptionV2]:
                ...

        class ExceptionValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[ExceptionInfo], *, values: WorkspaceRunDetails.Partial
            ) -> typing.Optional[ExceptionInfo]:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: WorkspaceRunDetails.Partial) -> str:
                ...

    @pydantic.validator("exception_v_2")
    def _validate_exception_v_2(
        cls, v: typing.Optional[ExceptionV2], values: WorkspaceRunDetails.Partial
    ) -> typing.Optional[ExceptionV2]:
        for validator in WorkspaceRunDetails.Validators._exception_v_2_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("exception")
    def _validate_exception(
        cls, v: typing.Optional[ExceptionInfo], values: WorkspaceRunDetails.Partial
    ) -> typing.Optional[ExceptionInfo]:
        for validator in WorkspaceRunDetails.Validators._exception_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("stdout")
    def _validate_stdout(cls, v: str, values: WorkspaceRunDetails.Partial) -> str:
        for validator in WorkspaceRunDetails.Validators._stdout_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        exception_v_2: typing_extensions.NotRequired[typing.Optional[ExceptionV2]]
        exception: typing_extensions.NotRequired[typing.Optional[ExceptionInfo]]
        stdout: typing_extensions.NotRequired[str]

    class Config:
        frozen = True
        allow_population_by_field_name = True
