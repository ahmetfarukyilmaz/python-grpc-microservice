# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommendations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15recommendations.proto\"/\n\x12\x42ookRecommendation\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\"^\n\x15RecommendationRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x1f\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\r.BookCategory\x12\x13\n\x0bmax_results\x18\x03 \x01(\x05\"F\n\x16RecommendationResponse\x12,\n\x0frecommendations\x18\x01 \x03(\x0b\x32\x13.BookRecommendation*\x89\x03\n\x0c\x42ookCategory\x12\x0b\n\x07\x46\x41NTASY\x10\x00\x12\x13\n\x0fSCIENCE_FICTION\x10\x01\x12\x0b\n\x07ROMANCE\x10\x02\x12\n\n\x06HORROR\x10\x03\x12\x0b\n\x07MYSTERY\x10\x04\x12\x0c\n\x08THRILLER\x10\x05\x12\t\n\x05\x44RAMA\x10\x06\x12\n\n\x06\x43OMEDY\x10\x07\x12\t\n\x05\x43RIME\x10\x08\x12\n\n\x06\x41\x43TION\x10\t\x12\r\n\tADVENTURE\x10\n\x12\r\n\tANIMATION\x10\x0b\x12\r\n\tBIOGRAPHY\x10\x0c\x12\t\n\x05GUIDE\x10\r\x12\x0b\n\x07HISTORY\x10\x0e\x12\t\n\x05HUMOR\x10\x0f\x12\n\n\x06MYSTIC\x10\x10\x12\x0e\n\nPHILOSOPHY\x10\x11\x12\x0c\n\x08POLITICS\x10\x12\x12\x0c\n\x08RELIGION\x10\x13\x12\x0c\n\x08ROYALITY\x10\x14\x12\x0b\n\x07SCIENCE\x10\x15\x12\x0b\n\x07SOCIETY\x10\x16\x12\t\n\x05SPORT\x10\x17\x12\n\n\x06TRAVEL\x10\x18\x12\x07\n\x03WAR\x10\x19\x12\x0b\n\x07WESTERN\x10\x1a\x12\t\n\x05OTHER\x10\x1b\x12\r\n\tSELF_HELP\x10\x1c\x32O\n\x0fRecommendations\x12<\n\tRecommend\x12\x16.RecommendationRequest\x1a\x17.RecommendationResponseb\x06proto3')

_BOOKCATEGORY = DESCRIPTOR.enum_types_by_name['BookCategory']
BookCategory = enum_type_wrapper.EnumTypeWrapper(_BOOKCATEGORY)
FANTASY = 0
SCIENCE_FICTION = 1
ROMANCE = 2
HORROR = 3
MYSTERY = 4
THRILLER = 5
DRAMA = 6
COMEDY = 7
CRIME = 8
ACTION = 9
ADVENTURE = 10
ANIMATION = 11
BIOGRAPHY = 12
GUIDE = 13
HISTORY = 14
HUMOR = 15
MYSTIC = 16
PHILOSOPHY = 17
POLITICS = 18
RELIGION = 19
ROYALITY = 20
SCIENCE = 21
SOCIETY = 22
SPORT = 23
TRAVEL = 24
WAR = 25
WESTERN = 26
OTHER = 27
SELF_HELP = 28


_BOOKRECOMMENDATION = DESCRIPTOR.message_types_by_name['BookRecommendation']
_RECOMMENDATIONREQUEST = DESCRIPTOR.message_types_by_name['RecommendationRequest']
_RECOMMENDATIONRESPONSE = DESCRIPTOR.message_types_by_name['RecommendationResponse']
BookRecommendation = _reflection.GeneratedProtocolMessageType('BookRecommendation', (_message.Message,), {
  'DESCRIPTOR' : _BOOKRECOMMENDATION,
  '__module__' : 'recommendations_pb2'
  # @@protoc_insertion_point(class_scope:BookRecommendation)
  })
_sym_db.RegisterMessage(BookRecommendation)

RecommendationRequest = _reflection.GeneratedProtocolMessageType('RecommendationRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDATIONREQUEST,
  '__module__' : 'recommendations_pb2'
  # @@protoc_insertion_point(class_scope:RecommendationRequest)
  })
_sym_db.RegisterMessage(RecommendationRequest)

RecommendationResponse = _reflection.GeneratedProtocolMessageType('RecommendationResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDATIONRESPONSE,
  '__module__' : 'recommendations_pb2'
  # @@protoc_insertion_point(class_scope:RecommendationResponse)
  })
_sym_db.RegisterMessage(RecommendationResponse)

_RECOMMENDATIONS = DESCRIPTOR.services_by_name['Recommendations']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOKCATEGORY._serialized_start=243
  _BOOKCATEGORY._serialized_end=636
  _BOOKRECOMMENDATION._serialized_start=25
  _BOOKRECOMMENDATION._serialized_end=72
  _RECOMMENDATIONREQUEST._serialized_start=74
  _RECOMMENDATIONREQUEST._serialized_end=168
  _RECOMMENDATIONRESPONSE._serialized_start=170
  _RECOMMENDATIONRESPONSE._serialized_end=240
  _RECOMMENDATIONS._serialized_start=638
  _RECOMMENDATIONS._serialized_end=717
# @@protoc_insertion_point(module_scope)
