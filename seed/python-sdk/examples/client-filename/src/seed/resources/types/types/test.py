# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Test_And(pydantic.BaseModel):
    type: typing.Literal["and"]
    value: bool

    class Config:
        frozen = True
        smart_union = True


class Test_Or(pydantic.BaseModel):
    type: typing.Literal["or"]
    value: bool

    class Config:
        frozen = True
        smart_union = True


"""
from seed import Test_And

Test_And(type="and", value=True)
"""
Test = typing.Union[Test_And, Test_Or]
