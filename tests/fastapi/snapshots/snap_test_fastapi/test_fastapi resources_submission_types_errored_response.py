# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .error_info import ErrorInfo
from .submission_id import SubmissionId


class ErroredResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    error_info: ErrorInfo = pydantic.Field(alias="errorInfo")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ErroredResponse.Validators.field("submission_id")
            def validate_submission_id(v: SubmissionId, values: ErroredResponse.Partial) -> SubmissionId:
                ...

            @ErroredResponse.Validators.field("error_info")
            def validate_error_info(v: ErrorInfo, values: ErroredResponse.Partial) -> ErrorInfo:
                ...
        """

        _submission_id_validators: typing.ClassVar[typing.List[ErroredResponse.Validators.SubmissionIdValidator]] = []
        _error_info_validators: typing.ClassVar[typing.List[ErroredResponse.Validators.ErrorInfoValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [ErroredResponse.Validators.SubmissionIdValidator], ErroredResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["error_info"]
        ) -> typing.Callable[
            [ErroredResponse.Validators.ErrorInfoValidator], ErroredResponse.Validators.ErrorInfoValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                if field_name == "error_info":
                    cls._error_info_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, v: SubmissionId, *, values: ErroredResponse.Partial) -> SubmissionId:
                ...

        class ErrorInfoValidator(typing_extensions.Protocol):
            def __call__(self, v: ErrorInfo, *, values: ErroredResponse.Partial) -> ErrorInfo:
                ...

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, v: SubmissionId, values: ErroredResponse.Partial) -> SubmissionId:
        for validator in ErroredResponse.Validators._submission_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("error_info")
    def _validate_error_info(cls, v: ErrorInfo, values: ErroredResponse.Partial) -> ErrorInfo:
        for validator in ErroredResponse.Validators._error_info_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        error_info: typing_extensions.NotRequired[ErrorInfo]

    class Config:
        frozen = True
        allow_population_by_field_name = True
