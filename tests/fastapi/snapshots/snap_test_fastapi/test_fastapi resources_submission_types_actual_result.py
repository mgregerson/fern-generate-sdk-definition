# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ...commons.types.variable_value import VariableValue
from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2 as resources_submission_types_exception_v_2_ExceptionV2

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def value(self, value: VariableValue) -> ActualResult:
        return ActualResult(__root__=_ActualResult.Value(type="value", value=value))

    def exception(self, value: ExceptionInfo) -> ActualResult:
        return ActualResult(__root__=_ActualResult.Exception(**value.dict(exclude_unset=True), type="exception"))

    def exception_v_2(self, value: resources_submission_types_exception_v_2_ExceptionV2) -> ActualResult:
        return ActualResult(__root__=_ActualResult.ExceptionV2(type="exceptionV2", value=value))


class ActualResult(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2]:
        return self.__root__

    def visit(
        self,
        value: typing.Callable[[VariableValue], T_Result],
        exception: typing.Callable[[ExceptionInfo], T_Result],
        exception_v_2: typing.Callable[[resources_submission_types_exception_v_2_ExceptionV2], T_Result],
    ) -> T_Result:
        if self.__root__.type == "value":
            return value(self.__root__.value)
        if self.__root__.type == "exception":
            return exception(self.__root__)
        if self.__root__.type == "exceptionV2":
            return exception_v_2(self.__root__.value)

    __root__: typing_extensions.Annotated[
        typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2],
        pydantic.Field(discriminator="type"),
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ActualResult.Validators.validate
            def validate(value: typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2]) -> typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2]],
                    typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2]],
                typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2],
            values.get("__root__"),
        )
        for validator in ActualResult.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _ActualResult:
    class Value(pydantic.BaseModel):
        type: typing_extensions.Literal["value"]
        value: VariableValue

    class Exception(ExceptionInfo):
        type: typing_extensions.Literal["exception"]

    class ExceptionV2(pydantic.BaseModel):
        type: typing_extensions.Literal["exceptionV2"]
        value: resources_submission_types_exception_v_2_ExceptionV2


ActualResult.update_forward_refs()
