# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: greeting/helloworld.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'greeting/helloworld.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19greeting/helloworld.proto\x12\x07\x65xample\"\"\n\x0cHelloRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\")\n\rHelloResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message2M\n\x0e\x45xampleService\x12;\n\x08SayHello\x12\x15.example.HelloRequest\x1a\x16.example.HelloResponse\"\x00\x42m\n\x10greeting.exampleB\x0fHelloworldProtoP\x01Z\x0c/api/example\xa2\x02\x03\x45XX\xaa\x02\x07\x45xample\xca\x02\x07\x45xample\xe2\x02\x13\x45xample\\GPBMetadata\xea\x02\x07\x45xampleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greeting.helloworld_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020greeting.exampleB\017HelloworldProtoP\001Z\014/api/example\242\002\003EXX\252\002\007Example\312\002\007Example\342\002\023Example\\GPBMetadata\352\002\007Example'
  _globals['_HELLOREQUEST']._serialized_start=38
  _globals['_HELLOREQUEST']._serialized_end=72
  _globals['_HELLORESPONSE']._serialized_start=74
  _globals['_HELLORESPONSE']._serialized_end=115
  _globals['_EXAMPLESERVICE']._serialized_start=117
  _globals['_EXAMPLESERVICE']._serialized_end=194
# @@protoc_insertion_point(module_scope)
