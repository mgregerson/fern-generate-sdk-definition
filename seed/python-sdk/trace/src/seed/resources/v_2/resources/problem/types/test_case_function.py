# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .test_case_with_actual_result_implementation import TestCaseWithActualResultImplementation
from .void_function_definition import VoidFunctionDefinition


class TestCaseFunction_WithActualResult(TestCaseWithActualResultImplementation):
    type: typing.Literal["withActualResult"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class TestCaseFunction_Custom(VoidFunctionDefinition):
    type: typing.Literal["custom"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


TestCaseFunction = typing.Union[TestCaseFunction_WithActualResult, TestCaseFunction_Custom]
