import io

import pytest
from pydantic_core._pydantic_core import ValidationError
from volur.pork.shared.v1alpha1 import quantity_pb2
from volur.sdk import CharacteristicColumn, Column, QuantityColumn, Value
from volur.sdk.v1alpha1.sources.csv import shared


@pytest.mark.parametrize(
    argnames=[
        "column_name",
        "characteristic_name",
        "data_type",
        "expected_result",
        "exception",
    ],
    argvalues=[
        (
            "column_name",
            "characteristic",
            "string",
            CharacteristicColumn(
                column_name="column_name",
                characteristic_name="characteristic",
                data_type="string",
            ),
            False,
        ),
        (
            "column_name",
            "characteristic",
            "bool",
            CharacteristicColumn(
                column_name="column_name",
                characteristic_name="characteristic",
                data_type="bool",
            ),
            False,
        ),
        (
            "column_name",
            "characteristic",
            "integer",
            CharacteristicColumn(
                column_name="column_name",
                characteristic_name="characteristic",
                data_type="integer",
            ),
            False,
        ),
        (
            "column_name",
            "characteristic",
            "float",
            CharacteristicColumn(
                column_name="column_name",
                characteristic_name="characteristic",
                data_type="float",
            ),
            False,
        ),
        (
            "column_name",
            "characteristic",
            "datetime",
            CharacteristicColumn(
                column_name="column_name",
                characteristic_name="characteristic",
                data_type="datetime",
            ),
            False,
        ),
        (
            "column_name",
            "characteristic",
            "unsupported-data-type",
            None,
            True,
        ),
    ],
)
def test_characteristic_column_value(
    column_name: str,
    characteristic_name: str,
    data_type: str,
    expected_result: CharacteristicColumn | None,
    exception: bool,
) -> None:
    if exception:
        with pytest.raises(ValidationError):
            CharacteristicColumn(
                column_name=column_name,
                characteristic_name=characteristic_name,
                data_type=data_type,
            )
    else:
        actual = CharacteristicColumn(
            column_name=column_name,
            characteristic_name=characteristic_name,
            data_type=data_type,
        )
        assert actual == expected_result


@pytest.mark.parametrize(
    argnames=[
        "column_name",
        "unit",
        "expected_result",
        "exception",
    ],
    argvalues=[
        (
            "column_name",
            "kilogram",
            QuantityColumn(
                column_name="column_name",
                unit="kilogram",
            ),
            False,
        ),
        (
            "column_name",
            "pound",
            QuantityColumn(
                column_name="column_name",
                unit="pound",
            ),
            False,
        ),
        (
            "column_name",
            "box",
            QuantityColumn(
                column_name="column_name",
                unit="box",
            ),
            False,
        ),
        (
            "column_name",
            "piece",
            QuantityColumn(
                column_name="column_name",
                unit="piece",
            ),
            False,
        ),
        (
            "column_name",
            "unsupported-unit",
            None,
            True,
        ),
    ],
)
def test_quantity_column(
    column_name: str,
    unit: str,
    expected_result: QuantityColumn | None,
    exception: bool,
) -> None:
    if exception:
        with pytest.raises(ValidationError):
            QuantityColumn(
                column_name=column_name,
                unit=unit,
            )
    else:
        actual = QuantityColumn(
            column_name=column_name,
            unit=unit,
        )
        assert actual == expected_result


@pytest.mark.parametrize(
    argnames=[
        "value",
        "column",
        "expected",
        "exception",
        "exception_message",
    ],
    argvalues=[
        (
            "1.8",
            QuantityColumn(
                column_name="value",
                unit="kilogram",
            ),
            quantity_pb2.QuantityValue(
                kilogram=1.8,
            ),
            False,
            "",
        ),
        (
            "1.8",
            QuantityColumn(
                column_name="value",
                unit="pound",
            ),
            quantity_pb2.QuantityValue(
                pound=1.8,
            ),
            False,
            "",
        ),
        (
            "2",
            QuantityColumn(
                column_name="value",
                unit="box",
            ),
            quantity_pb2.QuantityValue(
                box=2,
            ),
            False,
            "",
        ),
        (
            "2",
            QuantityColumn(
                column_name="value",
                unit="piece",
            ),
            quantity_pb2.QuantityValue(
                piece=2,
            ),
            False,
            "",
        ),
        (
            None,
            QuantityColumn(
                column_name="value",
                unit="piece",
            ),
            quantity_pb2.QuantityValue(),
            False,
            "",
        ),
        (
            "random-value-that-can-not-be-converted",
            QuantityColumn(
                column_name="value",
                unit="piece",
            ),
            None,
            True,
            "unknown quantity unit piece or provided value",
        ),
    ],
)
def test_load_quantity(
    value: str | None,
    column: QuantityColumn,
    expected: QuantityColumn | None,
    exception: bool,
    exception_message: str,
) -> None:
    if exception:
        with pytest.raises(ValueError, match=exception_message):
            shared.load_quantity(
                value=value,
                column=column,
            )
    else:
        actual = shared.load_quantity(
            value=value,
            column=column,
        )
        assert actual == expected


@pytest.mark.parametrize(
    argnames=[
        "row",
        "column",
        "expected",
        "exception",
        "exception_message",
    ],
    argvalues=[
        (
            {
                "column_name": "string-column-value",
            },
            Column(column_name="column_name"),
            Value(
                value_string="string-column-value",
            ),
            False,
            None,
        ),
        (
            {
                "column_name": "1",
            },
            Column(
                column_name="column_name",
                data_type="integer",
            ),
            Value(
                value_integer=1,
            ),
            False,
            None,
        ),
        (
            {
                "column_name": "1.2345",
            },
            Column(
                column_name="column_name",
                data_type="float",
            ),
            Value(
                value_float=1.2345,
            ),
            False,
            None,
        ),
        (
            {
                "column_name": "True",
            },
            Column(
                column_name="column_name",
                data_type="bool",
            ),
            Value(
                value_bool=True,
            ),
            False,
            None,
        ),
        (
            {
                "column_name": "string-column-value",
            },
            Column(column_name="column-name-that-does-not-exist"),
            Value(),
            False,
            "",
        ),
    ],
)
def test_fetch_value(
    row: dict[str, str],
    column: Column,
    expected: Value,
    exception: bool,
    exception_message: str,
) -> None:
    if exception:
        with pytest.raises(ValueError, match=exception_message):
            shared.fetch_value(
                row=row,
                column=column,
            )
    else:
        actual = shared.fetch_value(
            row=row,
            column=column,
        )
        assert actual == expected


@pytest.fixture()
def source() -> io.BytesIO:
    source = io.BytesIO()
    source.writelines(
        [
            b"fake-string-a\n",
            b"fake-string-b\n",
            b"fake-string-c\n",
        ]
    )
    source.seek(0)
    return source


@pytest.fixture()
def expected_strings() -> list[str]:
    return [
        "fake-string-a",
        "fake-string-b",
        "fake-string-c",
    ]


def test_buffered_io_base_to_str_iterable(
    source: io.BytesIO,
    expected_strings: list[str],
) -> None:
    actual = shared.buffered_io_base_to_str_iterable(source)
    assert list(actual) == expected_strings
