# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.language import Language
from ..commons.problem_id import ProblemId
from ..commons.test_case_with_expected_result import TestCaseWithExpectedResult
from ..commons.variable_type import VariableType
from .problem_description import ProblemDescription
from .problem_files import ProblemFiles
from .variable_type_and_name import VariableTypeAndName


class ProblemInfo(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    problem_description: ProblemDescription = pydantic.Field(alias="problemDescription")
    problem_name: str = pydantic.Field(alias="problemName")
    problem_version: int = pydantic.Field(alias="problemVersion")
    files: typing.Dict[Language, ProblemFiles]
    input_params: typing.List[VariableTypeAndName] = pydantic.Field(alias="inputParams")
    output_type: VariableType = pydantic.Field(alias="outputType")
    testcases: typing.List[TestCaseWithExpectedResult]
    method_name: str = pydantic.Field(alias="methodName")
    supports_custom_test_cases: bool = pydantic.Field(alias="supportsCustomTestCases")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ProblemInfo.Validators.field("problem_id")
            def validate_problem_id(v: ProblemId, values: ProblemInfo.Partial) -> ProblemId:
                ...

            @ProblemInfo.Validators.field("problem_description")
            def validate_problem_description(v: ProblemDescription, values: ProblemInfo.Partial) -> ProblemDescription:
                ...

            @ProblemInfo.Validators.field("problem_name")
            def validate_problem_name(v: str, values: ProblemInfo.Partial) -> str:
                ...

            @ProblemInfo.Validators.field("problem_version")
            def validate_problem_version(v: int, values: ProblemInfo.Partial) -> int:
                ...

            @ProblemInfo.Validators.field("files")
            def validate_files(v: typing.Dict[Language, ProblemFiles], values: ProblemInfo.Partial) -> typing.Dict[Language, ProblemFiles]:
                ...

            @ProblemInfo.Validators.field("input_params")
            def validate_input_params(v: typing.List[VariableTypeAndName], values: ProblemInfo.Partial) -> typing.List[VariableTypeAndName]:
                ...

            @ProblemInfo.Validators.field("output_type")
            def validate_output_type(v: VariableType, values: ProblemInfo.Partial) -> VariableType:
                ...

            @ProblemInfo.Validators.field("testcases")
            def validate_testcases(v: typing.List[TestCaseWithExpectedResult], values: ProblemInfo.Partial) -> typing.List[TestCaseWithExpectedResult]:
                ...

            @ProblemInfo.Validators.field("method_name")
            def validate_method_name(v: str, values: ProblemInfo.Partial) -> str:
                ...

            @ProblemInfo.Validators.field("supports_custom_test_cases")
            def validate_supports_custom_test_cases(v: bool, values: ProblemInfo.Partial) -> bool:
                ...
        """

        _problem_id_validators: typing.ClassVar[typing.List[ProblemInfo.Validators.ProblemIdValidator]] = []
        _problem_description_validators: typing.ClassVar[
            typing.List[ProblemInfo.Validators.ProblemDescriptionValidator]
        ] = []
        _problem_name_validators: typing.ClassVar[typing.List[ProblemInfo.Validators.ProblemNameValidator]] = []
        _problem_version_validators: typing.ClassVar[typing.List[ProblemInfo.Validators.ProblemVersionValidator]] = []
        _files_validators: typing.ClassVar[typing.List[ProblemInfo.Validators.FilesValidator]] = []
        _input_params_validators: typing.ClassVar[typing.List[ProblemInfo.Validators.InputParamsValidator]] = []
        _output_type_validators: typing.ClassVar[typing.List[ProblemInfo.Validators.OutputTypeValidator]] = []
        _testcases_validators: typing.ClassVar[typing.List[ProblemInfo.Validators.TestcasesValidator]] = []
        _method_name_validators: typing.ClassVar[typing.List[ProblemInfo.Validators.MethodNameValidator]] = []
        _supports_custom_test_cases_validators: typing.ClassVar[
            typing.List[ProblemInfo.Validators.SupportsCustomTestCasesValidator]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"]
        ) -> typing.Callable[[ProblemInfo.Validators.ProblemIdValidator], ProblemInfo.Validators.ProblemIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_description"]
        ) -> typing.Callable[
            [ProblemInfo.Validators.ProblemDescriptionValidator], ProblemInfo.Validators.ProblemDescriptionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_name"]
        ) -> typing.Callable[
            [ProblemInfo.Validators.ProblemNameValidator], ProblemInfo.Validators.ProblemNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"]
        ) -> typing.Callable[
            [ProblemInfo.Validators.ProblemVersionValidator], ProblemInfo.Validators.ProblemVersionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["files"]
        ) -> typing.Callable[[ProblemInfo.Validators.FilesValidator], ProblemInfo.Validators.FilesValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["input_params"]
        ) -> typing.Callable[
            [ProblemInfo.Validators.InputParamsValidator], ProblemInfo.Validators.InputParamsValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["output_type"]
        ) -> typing.Callable[[ProblemInfo.Validators.OutputTypeValidator], ProblemInfo.Validators.OutputTypeValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["testcases"]
        ) -> typing.Callable[[ProblemInfo.Validators.TestcasesValidator], ProblemInfo.Validators.TestcasesValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"]
        ) -> typing.Callable[[ProblemInfo.Validators.MethodNameValidator], ProblemInfo.Validators.MethodNameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["supports_custom_test_cases"]
        ) -> typing.Callable[
            [ProblemInfo.Validators.SupportsCustomTestCasesValidator],
            ProblemInfo.Validators.SupportsCustomTestCasesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    cls._problem_id_validators.append(validator)
                if field_name == "problem_description":
                    cls._problem_description_validators.append(validator)
                if field_name == "problem_name":
                    cls._problem_name_validators.append(validator)
                if field_name == "problem_version":
                    cls._problem_version_validators.append(validator)
                if field_name == "files":
                    cls._files_validators.append(validator)
                if field_name == "input_params":
                    cls._input_params_validators.append(validator)
                if field_name == "output_type":
                    cls._output_type_validators.append(validator)
                if field_name == "testcases":
                    cls._testcases_validators.append(validator)
                if field_name == "method_name":
                    cls._method_name_validators.append(validator)
                if field_name == "supports_custom_test_cases":
                    cls._supports_custom_test_cases_validators.append(validator)
                return validator

            return decorator

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, v: ProblemId, *, values: ProblemInfo.Partial) -> ProblemId:
                ...

        class ProblemDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, v: ProblemDescription, *, values: ProblemInfo.Partial) -> ProblemDescription:
                ...

        class ProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: ProblemInfo.Partial) -> str:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, v: int, *, values: ProblemInfo.Partial) -> int:
                ...

        class FilesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[Language, ProblemFiles], *, values: ProblemInfo.Partial
            ) -> typing.Dict[Language, ProblemFiles]:
                ...

        class InputParamsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[VariableTypeAndName], *, values: ProblemInfo.Partial
            ) -> typing.List[VariableTypeAndName]:
                ...

        class OutputTypeValidator(typing_extensions.Protocol):
            def __call__(self, v: VariableType, *, values: ProblemInfo.Partial) -> VariableType:
                ...

        class TestcasesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[TestCaseWithExpectedResult], *, values: ProblemInfo.Partial
            ) -> typing.List[TestCaseWithExpectedResult]:
                ...

        class MethodNameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: ProblemInfo.Partial) -> str:
                ...

        class SupportsCustomTestCasesValidator(typing_extensions.Protocol):
            def __call__(self, v: bool, *, values: ProblemInfo.Partial) -> bool:
                ...

    @pydantic.validator("problem_id")
    def _validate_problem_id(cls, v: ProblemId, values: ProblemInfo.Partial) -> ProblemId:
        for validator in ProblemInfo.Validators._problem_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("problem_description")
    def _validate_problem_description(cls, v: ProblemDescription, values: ProblemInfo.Partial) -> ProblemDescription:
        for validator in ProblemInfo.Validators._problem_description_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("problem_name")
    def _validate_problem_name(cls, v: str, values: ProblemInfo.Partial) -> str:
        for validator in ProblemInfo.Validators._problem_name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("problem_version")
    def _validate_problem_version(cls, v: int, values: ProblemInfo.Partial) -> int:
        for validator in ProblemInfo.Validators._problem_version_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("files")
    def _validate_files(
        cls, v: typing.Dict[Language, ProblemFiles], values: ProblemInfo.Partial
    ) -> typing.Dict[Language, ProblemFiles]:
        for validator in ProblemInfo.Validators._files_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("input_params")
    def _validate_input_params(
        cls, v: typing.List[VariableTypeAndName], values: ProblemInfo.Partial
    ) -> typing.List[VariableTypeAndName]:
        for validator in ProblemInfo.Validators._input_params_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("output_type")
    def _validate_output_type(cls, v: VariableType, values: ProblemInfo.Partial) -> VariableType:
        for validator in ProblemInfo.Validators._output_type_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("testcases")
    def _validate_testcases(
        cls, v: typing.List[TestCaseWithExpectedResult], values: ProblemInfo.Partial
    ) -> typing.List[TestCaseWithExpectedResult]:
        for validator in ProblemInfo.Validators._testcases_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("method_name")
    def _validate_method_name(cls, v: str, values: ProblemInfo.Partial) -> str:
        for validator in ProblemInfo.Validators._method_name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("supports_custom_test_cases")
    def _validate_supports_custom_test_cases(cls, v: bool, values: ProblemInfo.Partial) -> bool:
        for validator in ProblemInfo.Validators._supports_custom_test_cases_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        problem_id: typing_extensions.NotRequired[ProblemId]
        problem_description: typing_extensions.NotRequired[ProblemDescription]
        problem_name: typing_extensions.NotRequired[str]
        problem_version: typing_extensions.NotRequired[int]
        files: typing_extensions.NotRequired[typing.Dict[Language, ProblemFiles]]
        input_params: typing_extensions.NotRequired[typing.List[VariableTypeAndName]]
        output_type: typing_extensions.NotRequired[VariableType]
        testcases: typing_extensions.NotRequired[typing.List[TestCaseWithExpectedResult]]
        method_name: typing_extensions.NotRequired[str]
        supports_custom_test_cases: typing_extensions.NotRequired[bool]

    class Config:
        frozen = True
        allow_population_by_field_name = True
