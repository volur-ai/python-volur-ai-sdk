import io
from pathlib import Path

import pytest
from volur.pork.materials.v1alpha3 import material_pb2
from volur.pork.shared.v1alpha1.characteristic_pb2 import (
    Characteristic,
    CharacteristicValue,
)
from volur.pork.shared.v1alpha1.quantity_pb2 import Quantity, QuantityValue
from volur.sdk.v1alpha2.sources.csv.base import (
    CharacteristicColumnBool,
    CharacteristicColumnFloat,
    CharacteristicColumnInteger,
    CharacteristicColumnString,
    Column,
    QuantityColumn,
)
from volur.sdk.v1alpha2.sources.csv.source import MaterialsCSVFileSource


@pytest.fixture()
def materials_csv_content() -> list[str]:
    return [
        "id,plant,quantity,float_column,integer_column,string_column,bool_column",
        "material-id-1,Plant1,100,1.0,1,string-value,true",
        "material-id-2,Plant1,100,,1,string-value,true",
        "material-id-3,Plant1,100,1.0,,string-value,true",
        "material-id-4,Plant1,100,1.0,1,,false",
        "material-id-5,Plant1,100,1.0,1,string-value,",
    ]


@pytest.fixture()
def csv_file(
    tmpdir: Path,
    materials_csv_content: list[str],
) -> str:
    # See https://stackoverflow.com/questions/40784950/pathlib-path-and-py-test-localpath
    path = Path(tmpdir / "test.csv")
    with open(path, "wb") as f:
        for _ in materials_csv_content:
            f.write(_.encode())
            f.write("\n".encode())
    return str(path)


@pytest.fixture()
def csv_source(
    csv_file: str,
) -> MaterialsCSVFileSource:
    return MaterialsCSVFileSource(
        path=csv_file,
        material_id_column=Column(column_name="id"),
        plant_id_column=Column(column_name="plant"),
        quantity_column=QuantityColumn(column_name="quantity", unit="kilogram"),
        characteristics_columns=[
            CharacteristicColumnFloat(
                column_name="float_column",
                characteristic_name="float-characteristic",
            ),
            CharacteristicColumnInteger(
                column_name="integer_column",
                characteristic_name="integer-characteristic",
            ),
            CharacteristicColumnString(
                column_name="string_column",
                characteristic_name="string-characteristic",
            ),
            CharacteristicColumnBool(
                column_name="bool_column",
                characteristic_name="bool-characteristic",
            ),
        ],
    )


@pytest.fixture()
def expected_materials() -> list[material_pb2.Material]:
    return [
        material_pb2.Material(
            material_id="material-id-1",
            plant="Plant1",
            quantity=Quantity(value=QuantityValue(kilogram=100)),
            characteristics=[
                Characteristic(
                    name="float-characteristic",
                    value=CharacteristicValue(value_float=1.0),
                ),
                Characteristic(
                    name="integer-characteristic",
                    value=CharacteristicValue(value_integer=1),
                ),
                Characteristic(
                    name="string-characteristic",
                    value=CharacteristicValue(value_string="string-value"),
                ),
                Characteristic(
                    name="bool-characteristic",
                    value=CharacteristicValue(value_bool=True),
                ),
            ],
        ),
        material_pb2.Material(
            material_id="material-id-2",
            plant="Plant1",
            quantity=Quantity(value=QuantityValue(kilogram=100)),
            characteristics=[
                Characteristic(
                    name="float-characteristic",
                    value=CharacteristicValue(),
                ),
                Characteristic(
                    name="integer-characteristic",
                    value=CharacteristicValue(value_integer=1),
                ),
                Characteristic(
                    name="string-characteristic",
                    value=CharacteristicValue(value_string="string-value"),
                ),
                Characteristic(
                    name="bool-characteristic",
                    value=CharacteristicValue(value_bool=True),
                ),
            ],
        ),
        material_pb2.Material(
            material_id="material-id-3",
            plant="Plant1",
            quantity=Quantity(value=QuantityValue(kilogram=100)),
            characteristics=[
                Characteristic(
                    name="float-characteristic",
                    value=CharacteristicValue(value_float=1.0),
                ),
                Characteristic(
                    name="integer-characteristic",
                    value=CharacteristicValue(),
                ),
                Characteristic(
                    name="string-characteristic",
                    value=CharacteristicValue(value_string="string-value"),
                ),
                Characteristic(
                    name="bool-characteristic",
                    value=CharacteristicValue(value_bool=True),
                ),
            ],
        ),
        material_pb2.Material(
            material_id="material-id-4",
            plant="Plant1",
            quantity=Quantity(value=QuantityValue(kilogram=100)),
            characteristics=[
                Characteristic(
                    name="float-characteristic",
                    value=CharacteristicValue(value_float=1.0),
                ),
                Characteristic(
                    name="integer-characteristic",
                    value=CharacteristicValue(value_integer=1),
                ),
                Characteristic(
                    name="string-characteristic",
                    value=CharacteristicValue(),
                ),
                Characteristic(
                    name="bool-characteristic",
                    value=CharacteristicValue(value_bool=False),
                ),
            ],
        ),
        material_pb2.Material(
            material_id="material-id-5",
            plant="Plant1",
            quantity=Quantity(value=QuantityValue(kilogram=100)),
            characteristics=[
                Characteristic(
                    name="float-characteristic",
                    value=CharacteristicValue(value_float=1.0),
                ),
                Characteristic(
                    name="integer-characteristic",
                    value=CharacteristicValue(value_integer=1),
                ),
                Characteristic(
                    name="string-characteristic",
                    value=CharacteristicValue(value_string="string-value"),
                ),
                Characteristic(
                    name="bool-characteristic",
                    value=CharacteristicValue(),
                ),
            ],
        ),
    ]


@pytest.mark.asyncio()
async def test_load_file(
    csv_source: MaterialsCSVFileSource,
    expected_materials: list[material_pb2.Material],
) -> None:
    actual_materials = [_ async for _ in csv_source]
    assert actual_materials == expected_materials


@pytest.fixture()
def buffered_csv(materials_csv_content: list[str]) -> io.BufferedIOBase:
    bio = io.BytesIO()
    for _ in materials_csv_content:
        bio.write(_.encode())
        bio.write("\n".encode())
    bio.seek(0)
    return bio


@pytest.fixture()
def io_buffered_csv_source(buffered_csv: io.BufferedIOBase) -> MaterialsCSVFileSource:
    return MaterialsCSVFileSource(
        path=buffered_csv,
        material_id_column=Column(column_name="id"),
        plant_id_column=Column(column_name="plant"),
        quantity_column=QuantityColumn(column_name="quantity", unit="kilogram"),
        characteristics_columns=[
            CharacteristicColumnFloat(
                column_name="float_column",
                characteristic_name="float-characteristic",
            ),
            CharacteristicColumnInteger(
                column_name="integer_column",
                characteristic_name="integer-characteristic",
            ),
            CharacteristicColumnString(
                column_name="string_column",
                characteristic_name="string-characteristic",
            ),
            CharacteristicColumnBool(
                column_name="bool_column",
                characteristic_name="bool-characteristic",
            ),
        ],
    )


@pytest.mark.asyncio()
async def test_load_from_io_buffered(
    io_buffered_csv_source: MaterialsCSVFileSource,
    expected_materials: list[material_pb2.Material],
) -> None:
    actual_materials = [_ async for _ in io_buffered_csv_source]
    actual_materials.sort(key=lambda _: _.material_id)
    expected_materials.sort(key=lambda _: _.material_id)
    assert actual_materials == expected_materials