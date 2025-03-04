# This file was auto-generated by Fern from our API Definition.

import datetime
import uuid

from seed.client import AsyncSeedExhaustive, SeedExhaustive
from seed.types import (
    NestedObjectWithOptionalField,
    NestedObjectWithRequiredField,
    ObjectWithMapOfMap,
    ObjectWithOptionalField,
    ObjectWithRequiredField,
)

from ..utilities import validate_response


async def test_get_and_return_with_optional_field(client: SeedExhaustive, async_client: AsyncSeedExhaustive) -> None:
    expected_response = {}
    response = client.endpoints.object.get_and_return_with_optional_field(
        request=ObjectWithOptionalField(
            string="string",
            integer=1,
            long_=1000000,
            double=1.1,
            bool_=True,
            datetime=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"),
            date=datetime.date.fromisoformat("2023-01-15"),
            uuid_=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
            base_64="SGVsbG8gd29ybGQh",
            list_=["string"],
            set_=["string"],
            map_={1: "string"},
        )
    )
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.object.get_and_return_with_optional_field(
        request=ObjectWithOptionalField(
            string="string",
            integer=1,
            long_=1000000,
            double=1.1,
            bool_=True,
            datetime=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"),
            date=datetime.date.fromisoformat("2023-01-15"),
            uuid_=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
            base_64="SGVsbG8gd29ybGQh",
            list_=["string"],
            set_=["string"],
            map_={1: "string"},
        )
    )
    validate_response(async_response, expected_response)


async def test_get_and_return_with_required_field(client: SeedExhaustive, async_client: AsyncSeedExhaustive) -> None:
    expected_response = {}
    response = client.endpoints.object.get_and_return_with_required_field(
        request=ObjectWithRequiredField(string="string")
    )
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.object.get_and_return_with_required_field(
        request=ObjectWithRequiredField(string="string")
    )
    validate_response(async_response, expected_response)


async def test_get_and_return_with_map_of_map(client: SeedExhaustive, async_client: AsyncSeedExhaustive) -> None:
    expected_response = {}
    response = client.endpoints.object.get_and_return_with_map_of_map(
        request=ObjectWithMapOfMap(map_={"string": {"string": "string"}})
    )
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.object.get_and_return_with_map_of_map(
        request=ObjectWithMapOfMap(map_={"string": {"string": "string"}})
    )
    validate_response(async_response, expected_response)


async def test_get_and_return_nested_with_optional_field(
    client: SeedExhaustive, async_client: AsyncSeedExhaustive
) -> None:
    expected_response = {}
    response = client.endpoints.object.get_and_return_nested_with_optional_field(
        request=NestedObjectWithOptionalField(
            string="string",
            nested_object=ObjectWithOptionalField(
                string="string",
                integer=1,
                long_=1000000,
                double=1.1,
                bool_=True,
                datetime=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"),
                date=datetime.date.fromisoformat("2023-01-15"),
                uuid_=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
                base_64="SGVsbG8gd29ybGQh",
                list_=["string"],
                set_=["string"],
                map_={1: "string"},
            ),
        )
    )
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.object.get_and_return_nested_with_optional_field(
        request=NestedObjectWithOptionalField(
            string="string",
            nested_object=ObjectWithOptionalField(
                string="string",
                integer=1,
                long_=1000000,
                double=1.1,
                bool_=True,
                datetime=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"),
                date=datetime.date.fromisoformat("2023-01-15"),
                uuid_=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
                base_64="SGVsbG8gd29ybGQh",
                list_=["string"],
                set_=["string"],
                map_={1: "string"},
            ),
        )
    )
    validate_response(async_response, expected_response)


async def test_get_and_return_nested_with_required_field(
    client: SeedExhaustive, async_client: AsyncSeedExhaustive
) -> None:
    expected_response = {}
    response = client.endpoints.object.get_and_return_nested_with_required_field(
        request=NestedObjectWithRequiredField(
            string="string",
            nested_object=ObjectWithOptionalField(
                string="string",
                integer=1,
                long_=1000000,
                double=1.1,
                bool_=True,
                datetime=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"),
                date=datetime.date.fromisoformat("2023-01-15"),
                uuid_=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
                base_64="SGVsbG8gd29ybGQh",
                list_=["string"],
                set_=["string"],
                map_={1: "string"},
            ),
        )
    )
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.object.get_and_return_nested_with_required_field(
        request=NestedObjectWithRequiredField(
            string="string",
            nested_object=ObjectWithOptionalField(
                string="string",
                integer=1,
                long_=1000000,
                double=1.1,
                bool_=True,
                datetime=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"),
                date=datetime.date.fromisoformat("2023-01-15"),
                uuid_=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
                base_64="SGVsbG8gd29ybGQh",
                list_=["string"],
                set_=["string"],
                map_={1: "string"},
            ),
        )
    )
    validate_response(async_response, expected_response)


async def test_get_and_return_nested_with_required_field_as_list(
    client: SeedExhaustive, async_client: AsyncSeedExhaustive
) -> None:
    expected_response = {}
    response = client.endpoints.object.get_and_return_nested_with_required_field_as_list(
        request=[
            NestedObjectWithRequiredField(
                string="string",
                nested_object=ObjectWithOptionalField(
                    string="string",
                    integer=1,
                    long_=1000000,
                    double=1.1,
                    bool_=True,
                    datetime=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"),
                    date=datetime.date.fromisoformat("2023-01-15"),
                    uuid_=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
                    base_64="SGVsbG8gd29ybGQh",
                    list_=["string"],
                    set_=["string"],
                    map_={1: "string"},
                ),
            )
        ]
    )
    validate_response(response, expected_response)

    async_response = await async_client.endpoints.object.get_and_return_nested_with_required_field_as_list(
        request=[
            NestedObjectWithRequiredField(
                string="string",
                nested_object=ObjectWithOptionalField(
                    string="string",
                    integer=1,
                    long_=1000000,
                    double=1.1,
                    bool_=True,
                    datetime=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"),
                    date=datetime.date.fromisoformat("2023-01-15"),
                    uuid_=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
                    base_64="SGVsbG8gd29ybGQh",
                    list_=["string"],
                    set_=["string"],
                    map_={1: "string"},
                ),
            )
        ]
    )
    validate_response(async_response, expected_response)
