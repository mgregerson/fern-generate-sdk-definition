# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .doubly_linked_list_node_value import DoublyLinkedListNodeValue
from .node_id import NodeId


class DoublyLinkedListValue(pydantic.BaseModel):
    head: typing.Optional[NodeId]
    nodes: typing.Dict[NodeId, DoublyLinkedListNodeValue]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DoublyLinkedListValue.Validators.field("head")
            def validate_head(v: typing.Optional[NodeId], values: DoublyLinkedListValue.Partial) -> typing.Optional[NodeId]:
                ...

            @DoublyLinkedListValue.Validators.field("nodes")
            def validate_nodes(v: typing.Dict[NodeId, DoublyLinkedListNodeValue], values: DoublyLinkedListValue.Partial) -> typing.Dict[NodeId, DoublyLinkedListNodeValue]:
                ...
        """

        _head_validators: typing.ClassVar[typing.List[DoublyLinkedListValue.Validators.HeadValidator]] = []
        _nodes_validators: typing.ClassVar[typing.List[DoublyLinkedListValue.Validators.NodesValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["head"]
        ) -> typing.Callable[
            [DoublyLinkedListValue.Validators.HeadValidator], DoublyLinkedListValue.Validators.HeadValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["nodes"]
        ) -> typing.Callable[
            [DoublyLinkedListValue.Validators.NodesValidator], DoublyLinkedListValue.Validators.NodesValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "head":
                    cls._head_validators.append(validator)
                if field_name == "nodes":
                    cls._nodes_validators.append(validator)
                return validator

            return decorator

        class HeadValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[NodeId], *, values: DoublyLinkedListValue.Partial
            ) -> typing.Optional[NodeId]:
                ...

        class NodesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[NodeId, DoublyLinkedListNodeValue], *, values: DoublyLinkedListValue.Partial
            ) -> typing.Dict[NodeId, DoublyLinkedListNodeValue]:
                ...

    @pydantic.validator("head")
    def _validate_head(
        cls, v: typing.Optional[NodeId], values: DoublyLinkedListValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in DoublyLinkedListValue.Validators._head_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("nodes")
    def _validate_nodes(
        cls, v: typing.Dict[NodeId, DoublyLinkedListNodeValue], values: DoublyLinkedListValue.Partial
    ) -> typing.Dict[NodeId, DoublyLinkedListNodeValue]:
        for validator in DoublyLinkedListValue.Validators._nodes_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        head: typing_extensions.NotRequired[typing.Optional[NodeId]]
        nodes: typing_extensions.NotRequired[typing.Dict[NodeId, DoublyLinkedListNodeValue]]

    class Config:
        frozen = True
