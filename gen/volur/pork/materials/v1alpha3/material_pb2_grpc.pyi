"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import volur.pork.materials.v1alpha3.material_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class MaterialInformationServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    UploadMaterialInformation: grpc.StreamStreamMultiCallable[
        volur.pork.materials.v1alpha3.material_pb2.UploadMaterialInformationRequest,
        volur.pork.materials.v1alpha3.material_pb2.UploadMaterialInformationResponse,
    ]
    """UploadMaterialInformation allows client to upload a stream of material
    inventory information to the server and receive a stream of responses
    containing the status of each upload. This supports batch processing and
    real-time feedback on the operation.
    """

class MaterialInformationServiceAsyncStub:
    UploadMaterialInformation: grpc.aio.StreamStreamMultiCallable[
        volur.pork.materials.v1alpha3.material_pb2.UploadMaterialInformationRequest,
        volur.pork.materials.v1alpha3.material_pb2.UploadMaterialInformationResponse,
    ]
    """UploadMaterialInformation allows client to upload a stream of material
    inventory information to the server and receive a stream of responses
    containing the status of each upload. This supports batch processing and
    real-time feedback on the operation.
    """

class MaterialInformationServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def UploadMaterialInformation(
        self,
        request_iterator: _MaybeAsyncIterator[volur.pork.materials.v1alpha3.material_pb2.UploadMaterialInformationRequest],
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[volur.pork.materials.v1alpha3.material_pb2.UploadMaterialInformationResponse], collections.abc.AsyncIterator[volur.pork.materials.v1alpha3.material_pb2.UploadMaterialInformationResponse]]:
        """UploadMaterialInformation allows client to upload a stream of material
        inventory information to the server and receive a stream of responses
        containing the status of each upload. This supports batch processing and
        real-time feedback on the operation.
        """

def add_MaterialInformationServiceServicer_to_server(servicer: MaterialInformationServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
