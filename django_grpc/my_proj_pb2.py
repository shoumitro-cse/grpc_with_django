# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my_proj.proto

"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rmy_proj.proto\x12\x0emy_project_pkg\"d\n\tMyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x11\n\timage_url\x18\x04 \x01(\t\x12\x16\n\x0e\x62\x61lance_amount\x18\x05 \x01(\t\"\x1a\n\x07MyReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"M\n\x0eMyDelayedReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12*\n\x07request\x18\x02 \x03(\x0b\x32\x19.my_project_pkg.MyRequest2\xc2\x02\n\rMyServiceData\x12@\n\nMyUnaryFun\x12\x19.my_project_pkg.MyRequest\x1a\x17.my_project_pkg.MyReply\x12L\n\x14MyServerStreamingFun\x12\x19.my_project_pkg.MyRequest\x1a\x17.my_project_pkg.MyReply0\x01\x12S\n\x14MyClientStreamingFun\x12\x19.my_project_pkg.MyRequest\x1a\x1e.my_project_pkg.MyDelayedReply(\x01\x12L\n\x12MyBothStreamingFun\x12\x19.my_project_pkg.MyRequest\x1a\x17.my_project_pkg.MyReply(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_proj_pb2', _globals)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_MYREQUEST']._serialized_start = 33
    _globals['_MYREQUEST']._serialized_end = 133
    _globals['_MYREPLY']._serialized_start = 135
    _globals['_MYREPLY']._serialized_end = 161
    _globals['_MYDELAYEDREPLY']._serialized_start = 163
    _globals['_MYDELAYEDREPLY']._serialized_end = 240
    _globals['_MYSERVICEDATA']._serialized_start = 243
    _globals['_MYSERVICEDATA']._serialized_end = 565
# @@protoc_insertion_point(module_scope)
