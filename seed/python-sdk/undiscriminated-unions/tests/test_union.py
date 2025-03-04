# This file was auto-generated by Fern from our API Definition.

from seed.client import AsyncSeedUndiscriminatedUnions, SeedUndiscriminatedUnions

from .utilities import validate_response


async def test_get(client: SeedUndiscriminatedUnions, async_client: AsyncSeedUndiscriminatedUnions) -> None:
    expected_response = "string"
    response = client.union.get(request="string")
    validate_response(response, expected_response)

    async_response = await async_client.union.get(request="string")
    validate_response(async_response, expected_response)
