# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: volur/pork/demand/v1alpha2/demand.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.type import money_pb2 as google_dot_type_dot_money__pb2
from volur.pork.products.v1alpha2 import product_pb2 as volur_dot_pork_dot_products_dot_v1alpha2_dot_product__pb2
from volur.pork.shared.v1alpha1 import characteristic_pb2 as volur_dot_pork_dot_shared_dot_v1alpha1_dot_characteristic__pb2
from volur.pork.shared.v1alpha1 import quantity_pb2 as volur_dot_pork_dot_shared_dot_v1alpha1_dot_quantity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'volur/pork/demand/v1alpha2/demand.proto\x12\x1avolur.pork.demand.v1alpha2\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x17google/type/money.proto\x1a*volur/pork/products/v1alpha2/product.proto\x1a/volur/pork/shared/v1alpha1/characteristic.proto\x1a)volur/pork/shared/v1alpha1/quantity.proto\"\xd0\x03\n\x06\x44\x65mand\x12?\n\x07product\x18\x01 \x01(\x0b\x32%.volur.pork.products.v1alpha2.ProductR\x07product\x12\x14\n\x05plant\x18\x02 \x01(\tR\x05plant\x12\x1f\n\x0b\x63ustomer_id\x18\x03 \x01(\tR\ncustomerId\x12@\n\x08quantity\x18\x04 \x01(\x0b\x32$.volur.pork.shared.v1alpha1.QuantityR\x08quantity\x12?\n\x0b\x64ispatch_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\ndispatchAt\x12;\n\tdemand_on\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x08\x64\x65mandOn\x12\x38\n\x0eprice_per_unit\x18\x07 \x01(\x0b\x32\x12.google.type.MoneyR\x0cpricePerUnit\x12T\n\x0f\x63haracteristics\x18\x08 \x03(\x0b\x32*.volur.pork.shared.v1alpha1.CharacteristicR\x0f\x63haracteristics\"\\\n\x1eUploadDemandInformationRequest\x12:\n\x06\x64\x65mand\x18\x01 \x01(\x0b\x32\".volur.pork.demand.v1alpha2.DemandR\x06\x64\x65mand\"M\n\x1fUploadDemandInformationResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status\".\n\x12\x44\x65mandUploadStatus\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message2\xb3\x01\n\x18\x44\x65mandInformationService\x12\x96\x01\n\x17UploadDemandInformation\x12:.volur.pork.demand.v1alpha2.UploadDemandInformationRequest\x1a;.volur.pork.demand.v1alpha2.UploadDemandInformationResponse(\x01\x30\x01\x42\x99\x02\n\x1e\x63om.volur.pork.demand.v1alpha2B\x0b\x44\x65mandProtoP\x01Z_github.com/volur-ai/data-component-cooperl/api/protos/volur/pork/demand/v1alpha2;demandv1alpha2\xa2\x02\x03VPD\xaa\x02\x1aVolur.Pork.Demand.V1alpha2\xca\x02\x1aVolur\\Pork\\Demand\\V1alpha2\xe2\x02&Volur\\Pork\\Demand\\V1alpha2\\GPBMetadata\xea\x02\x1dVolur::Pork::Demand::V1alpha2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'volur.pork.demand.v1alpha2.demand_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.volur.pork.demand.v1alpha2B\013DemandProtoP\001Z_github.com/volur-ai/data-component-cooperl/api/protos/volur/pork/demand/v1alpha2;demandv1alpha2\242\002\003VPD\252\002\032Volur.Pork.Demand.V1alpha2\312\002\032Volur\\Pork\\Demand\\V1alpha2\342\002&Volur\\Pork\\Demand\\V1alpha2\\GPBMetadata\352\002\035Volur::Pork::Demand::V1alpha2'
  _DEMAND.fields_by_name['dispatch_at']._options = None
  _DEMAND.fields_by_name['dispatch_at']._serialized_options = b'\030\001'
  _DEMAND.fields_by_name['demand_on']._options = None
  _DEMAND.fields_by_name['demand_on']._serialized_options = b'\030\001'
  _globals['_DEMAND']._serialized_start=291
  _globals['_DEMAND']._serialized_end=755
  _globals['_UPLOADDEMANDINFORMATIONREQUEST']._serialized_start=757
  _globals['_UPLOADDEMANDINFORMATIONREQUEST']._serialized_end=849
  _globals['_UPLOADDEMANDINFORMATIONRESPONSE']._serialized_start=851
  _globals['_UPLOADDEMANDINFORMATIONRESPONSE']._serialized_end=928
  _globals['_DEMANDUPLOADSTATUS']._serialized_start=930
  _globals['_DEMANDUPLOADSTATUS']._serialized_end=976
  _globals['_DEMANDINFORMATIONSERVICE']._serialized_start=979
  _globals['_DEMANDINFORMATIONSERVICE']._serialized_end=1158
# @@protoc_insertion_point(module_scope)
