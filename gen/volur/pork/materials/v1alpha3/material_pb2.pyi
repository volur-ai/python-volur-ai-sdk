"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import sys
import typing
import volur.pork.shared.v1alpha1.characteristic_pb2
import volur.pork.shared.v1alpha1.quantity_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _MaterialType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _MaterialTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MaterialType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    MATERIAL_TYPE_UNSPECIFIED: _MaterialType.ValueType  # 0
    """Default value, unspecified."""
    MATERIAL_TYPE_CARCASS: _MaterialType.ValueType  # 1
    """A side portion of an animal carcass."""

class MaterialType(_MaterialType, metaclass=_MaterialTypeEnumTypeWrapper):
    """MaterialType enumerates the kinds of materials used during the fabrication or
    production process. This helps in classifying the materials and understanding
    their intended use in the operation.
    """

MATERIAL_TYPE_UNSPECIFIED: MaterialType.ValueType  # 0
"""Default value, unspecified."""
MATERIAL_TYPE_CARCASS: MaterialType.ValueType  # 1
"""A side portion of an animal carcass."""
global___MaterialType = MaterialType

@typing_extensions.final
class Material(google.protobuf.message.Message):
    """Material is an entity that represents the various inputs used during fabrication
    or production processes, such as carcasses, sides, primal cuts, and other forms
    of material. It contains details about the available supply of materials, including
    their quantity and attributes that are important for processing, like weight and
    quality.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MATERIAL_ID_FIELD_NUMBER: builtins.int
    PLANT_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    CHARACTERISTICS_FIELD_NUMBER: builtins.int
    ARRIVED_AT_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    material_id: builtins.str
    """A unique identifier for the material."""
    plant: builtins.str
    """Identifier of the plant or facility where the material is located."""
    @property
    def quantity(self) -> volur.pork.shared.v1alpha1.quantity_pb2.Quantity:
        """The amount of this material that is available."""
    type: global___MaterialType.ValueType
    """The specific type of the material (e.g., side, carcass, primal cut)."""
    @property
    def characteristics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[volur.pork.shared.v1alpha1.characteristic_pb2.Characteristic]:
        """A list of additional characteristics that further describe the material."""
    @property
    def arrived_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp indicating when the material arrived at the facility."""
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp indicating when the material is expected to expire."""
    def __init__(
        self,
        *,
        material_id: builtins.str = ...,
        plant: builtins.str = ...,
        quantity: volur.pork.shared.v1alpha1.quantity_pb2.Quantity | None = ...,
        type: global___MaterialType.ValueType = ...,
        characteristics: collections.abc.Iterable[volur.pork.shared.v1alpha1.characteristic_pb2.Characteristic] | None = ...,
        arrived_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["arrived_at", b"arrived_at", "expires_at", b"expires_at", "quantity", b"quantity"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["arrived_at", b"arrived_at", "characteristics", b"characteristics", "expires_at", b"expires_at", "material_id", b"material_id", "plant", b"plant", "quantity", b"quantity", "type", b"type"]) -> None: ...

global___Material = Material

@typing_extensions.final
class UploadMaterialInformationRequest(google.protobuf.message.Message):
    """UploadMaterialInformationRequest is the request message for uploading
    material information. It contains the inventory information of a material
    to be uploaded.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MATERIAL_FIELD_NUMBER: builtins.int
    @property
    def material(self) -> global___Material:
        """Material represents a single entry of the material to be processed.
        It contains all relevant details that define the identity, location,
        quantity, and attributes of the material within a facility.
        """
    def __init__(
        self,
        *,
        material: global___Material | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["material", b"material"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["material", b"material"]) -> None: ...

global___UploadMaterialInformationRequest = UploadMaterialInformationRequest

@typing_extensions.final
class UploadMaterialInformationResponse(google.protobuf.message.Message):
    """UploadMaterialInformationResponse is the response message for the
    UploadMaterialInformation service, containing the status of the material
    upload.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    @property
    def status(self) -> google.rpc.status_pb2.Status:
        """The status of material upload, including any messages or errors."""
    def __init__(
        self,
        *,
        status: google.rpc.status_pb2.Status | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["status", b"status"]) -> None: ...

global___UploadMaterialInformationResponse = UploadMaterialInformationResponse
