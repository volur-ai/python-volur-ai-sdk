# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: volur/pork/bom/v1alpha1/bom.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!volur/pork/bom/v1alpha1/bom.proto\x12\x17volur.pork.bom.v1alpha1\x1a\x17google/rpc/status.proto\"\xa3\x01\n\x03\x42om\x12\x1d\n\nprocess_id\x18\x01 \x01(\tR\tprocessId\x12\x14\n\x05plant\x18\x02 \x01(\tR\x05plant\x12\x1d\n\nmachine_id\x18\x03 \x01(\tR\tmachineId\x12\x1d\n\nproduct_id\x18\x04 \x01(\tR\tproductId\x12)\n\x10quantity_percent\x18\x05 \x01(\x02R\x0fquantityPercent\"M\n\x1bUploadBomInformationRequest\x12.\n\x03\x62om\x18\x01 \x01(\x0b\x32\x1c.volur.pork.bom.v1alpha1.BomR\x03\x62om\"J\n\x1cUploadBomInformationResponse\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status2\xa1\x01\n\x15\x42omInformationService\x12\x87\x01\n\x14UploadBomInformation\x12\x34.volur.pork.bom.v1alpha1.UploadBomInformationRequest\x1a\x35.volur.pork.bom.v1alpha1.UploadBomInformationResponse(\x01\x30\x01\x42\xec\x01\n\x1b\x63om.volur.pork.bom.v1alpha1B\x08\x42omProtoP\x01ZDgithub.com/volur-ai/ryder/protos/volur/pork/bom/v1alpha1;bomv1alpha1\xa2\x02\x03VPB\xaa\x02\x17Volur.Pork.Bom.V1alpha1\xca\x02\x17Volur\\Pork\\Bom\\V1alpha1\xe2\x02#Volur\\Pork\\Bom\\V1alpha1\\GPBMetadata\xea\x02\x1aVolur::Pork::Bom::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'volur.pork.bom.v1alpha1.bom_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.volur.pork.bom.v1alpha1B\010BomProtoP\001ZDgithub.com/volur-ai/ryder/protos/volur/pork/bom/v1alpha1;bomv1alpha1\242\002\003VPB\252\002\027Volur.Pork.Bom.V1alpha1\312\002\027Volur\\Pork\\Bom\\V1alpha1\342\002#Volur\\Pork\\Bom\\V1alpha1\\GPBMetadata\352\002\032Volur::Pork::Bom::V1alpha1'
  _globals['_BOM']._serialized_start=88
  _globals['_BOM']._serialized_end=251
  _globals['_UPLOADBOMINFORMATIONREQUEST']._serialized_start=253
  _globals['_UPLOADBOMINFORMATIONREQUEST']._serialized_end=330
  _globals['_UPLOADBOMINFORMATIONRESPONSE']._serialized_start=332
  _globals['_UPLOADBOMINFORMATIONRESPONSE']._serialized_end=406
  _globals['_BOMINFORMATIONSERVICE']._serialized_start=409
  _globals['_BOMINFORMATIONSERVICE']._serialized_end=570
# @@protoc_insertion_point(module_scope)
