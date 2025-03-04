import json
import typing

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


def validate_response(response: typing.Any, json_expectation: typing.Any) -> None:
    if not isinstance(response, dict) and not issubclass(type(response), pydantic.BaseModel):
        assert response == json_expectation, "Primitives found, expected: {0}, Actual: {1}".format(
            json_expectation, response
        )
        return

    response_json = response
    if issubclass(type(response), pydantic.BaseModel):
        response_json = json.loads(response.json())

    for key, value in json_expectation.items():
        assert key in response_json
        if isinstance(value, dict):
            validate_response(response_json[key], value)
        elif isinstance(value, list):
            assert set(response_json[key]) == set(value)
        else:
            assert response_json[key] == value

        # Ensure there are no additional fields here either
        del response_json[key]
    assert len(response_json) == 0, "Additional fields found, expected None: {0}".format(response_json)
