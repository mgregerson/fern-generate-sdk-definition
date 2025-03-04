# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .binary_tree_node_and_tree_value import BinaryTreeNodeAndTreeValue
from .binary_tree_node_value import BinaryTreeNodeValue
from .binary_tree_value import BinaryTreeValue
from .doubly_linked_list_node_and_list_value import DoublyLinkedListNodeAndListValue
from .doubly_linked_list_node_value import DoublyLinkedListNodeValue
from .doubly_linked_list_value import DoublyLinkedListValue
from .generic_value import GenericValue
from .node_id import NodeId
from .singly_linked_list_node_and_list_value import SinglyLinkedListNodeAndListValue
from .singly_linked_list_node_value import SinglyLinkedListNodeValue
from .singly_linked_list_value import SinglyLinkedListValue

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DebugVariableValue_IntegerValue(pydantic.BaseModel):
    type: typing.Literal["integerValue"]
    value: int


class DebugVariableValue_BooleanValue(pydantic.BaseModel):
    type: typing.Literal["booleanValue"]
    value: bool


class DebugVariableValue_DoubleValue(pydantic.BaseModel):
    type: typing.Literal["doubleValue"]
    value: float


class DebugVariableValue_StringValue(pydantic.BaseModel):
    type: typing.Literal["stringValue"]
    value: str


class DebugVariableValue_CharValue(pydantic.BaseModel):
    type: typing.Literal["charValue"]
    value: str


class DebugVariableValue_MapValue(DebugMapValue):
    type: typing.Literal["mapValue"]

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class DebugVariableValue_ListValue(pydantic.BaseModel):
    type: typing.Literal["listValue"]
    value: typing.List[DebugVariableValue]


class DebugVariableValue_BinaryTreeNodeValue(BinaryTreeNodeAndTreeValue):
    type: typing.Literal["binaryTreeNodeValue"]

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class DebugVariableValue_SinglyLinkedListNodeValue(SinglyLinkedListNodeAndListValue):
    type: typing.Literal["singlyLinkedListNodeValue"]

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class DebugVariableValue_DoublyLinkedListNodeValue(DoublyLinkedListNodeAndListValue):
    type: typing.Literal["doublyLinkedListNodeValue"]

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class DebugVariableValue_UndefinedValue(pydantic.BaseModel):
    type: typing.Literal["undefinedValue"]


class DebugVariableValue_NullValue(pydantic.BaseModel):
    type: typing.Literal["nullValue"]


class DebugVariableValue_GenericValue(GenericValue):
    type: typing.Literal["genericValue"]

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


DebugVariableValue = typing.Union[
    DebugVariableValue_IntegerValue,
    DebugVariableValue_BooleanValue,
    DebugVariableValue_DoubleValue,
    DebugVariableValue_StringValue,
    DebugVariableValue_CharValue,
    DebugVariableValue_MapValue,
    DebugVariableValue_ListValue,
    DebugVariableValue_BinaryTreeNodeValue,
    DebugVariableValue_SinglyLinkedListNodeValue,
    DebugVariableValue_DoublyLinkedListNodeValue,
    DebugVariableValue_UndefinedValue,
    DebugVariableValue_NullValue,
    DebugVariableValue_GenericValue,
]
from .debug_key_value_pairs import DebugKeyValuePairs  # noqa: E402
from .debug_map_value import DebugMapValue  # noqa: E402

DebugVariableValue_MapValue.update_forward_refs(
    DebugKeyValuePairs=DebugKeyValuePairs, DebugMapValue=DebugMapValue, DebugVariableValue=DebugVariableValue
)
DebugVariableValue_ListValue.update_forward_refs(
    DebugKeyValuePairs=DebugKeyValuePairs, DebugMapValue=DebugMapValue, DebugVariableValue=DebugVariableValue
)
