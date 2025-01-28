# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api.proto
# Protobuf Python Version: 5.29.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    1,
    '',
    'api.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\x12\x03\x61pi\"\x82\x01\n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06secret\x18\x02 \x01(\t\x12\x15\n\rredirect_uris\x18\x03 \x03(\t\x12\x15\n\rtrusted_peers\x18\x04 \x03(\t\x12\x0e\n\x06public\x18\x05 \x01(\x08\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x10\n\x08logo_url\x18\x07 \x01(\t\"\x1a\n\x0cGetClientReq\x12\n\n\x02id\x18\x01 \x01(\t\",\n\rGetClientResp\x12\x1b\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x0b.api.Client\".\n\x0f\x43reateClientReq\x12\x1b\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x0b.api.Client\"G\n\x10\x43reateClientResp\x12\x16\n\x0e\x61lready_exists\x18\x01 \x01(\x08\x12\x1b\n\x06\x63lient\x18\x02 \x01(\x0b\x32\x0b.api.Client\"\x1d\n\x0f\x44\x65leteClientReq\x12\n\n\x02id\x18\x01 \x01(\t\"%\n\x10\x44\x65leteClientResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"k\n\x0fUpdateClientReq\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rredirect_uris\x18\x02 \x03(\t\x12\x15\n\rtrusted_peers\x18\x03 \x03(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x10\n\x08logo_url\x18\x05 \x01(\t\"%\n\x10UpdateClientResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"J\n\x08Password\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\"4\n\x11\x43reatePasswordReq\x12\x1f\n\x08password\x18\x01 \x01(\x0b\x32\r.api.Password\",\n\x12\x43reatePasswordResp\x12\x16\n\x0e\x61lready_exists\x18\x01 \x01(\x08\"J\n\x11UpdatePasswordReq\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08new_hash\x18\x02 \x01(\x0c\x12\x14\n\x0cnew_username\x18\x03 \x01(\t\"\'\n\x12UpdatePasswordResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"\"\n\x11\x44\x65letePasswordReq\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"\'\n\x12\x44\x65letePasswordResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"\x11\n\x0fListPasswordReq\"4\n\x10ListPasswordResp\x12 \n\tpasswords\x18\x01 \x03(\x0b\x32\r.api.Password\"C\n\tConnector\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x04 \x01(\x0c\"7\n\x12\x43reateConnectorReq\x12!\n\tconnector\x18\x01 \x01(\x0b\x32\x0e.api.Connector\"-\n\x13\x43reateConnectorResp\x12\x16\n\x0e\x61lready_exists\x18\x01 \x01(\x08\"X\n\x12UpdateConnectorReq\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08new_type\x18\x02 \x01(\t\x12\x10\n\x08new_name\x18\x03 \x01(\t\x12\x12\n\nnew_config\x18\x04 \x01(\x0c\"(\n\x13UpdateConnectorResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\" \n\x12\x44\x65leteConnectorReq\x12\n\n\x02id\x18\x01 \x01(\t\"(\n\x13\x44\x65leteConnectorResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"\x12\n\x10ListConnectorReq\"7\n\x11ListConnectorResp\x12\"\n\nconnectors\x18\x01 \x03(\x0b\x32\x0e.api.Connector\"\x0c\n\nVersionReq\"*\n\x0bVersionResp\x12\x0e\n\x06server\x18\x01 \x01(\t\x12\x0b\n\x03\x61pi\x18\x02 \x01(\x05\"\x0e\n\x0c\x44iscoveryReq\"\xe9\x03\n\rDiscoveryResp\x12\x0e\n\x06issuer\x18\x01 \x01(\t\x12\x1e\n\x16\x61uthorization_endpoint\x18\x02 \x01(\t\x12\x16\n\x0etoken_endpoint\x18\x03 \x01(\t\x12\x10\n\x08jwks_uri\x18\x04 \x01(\t\x12\x19\n\x11userinfo_endpoint\x18\x05 \x01(\t\x12%\n\x1d\x64\x65vice_authorization_endpoint\x18\x06 \x01(\t\x12\x1e\n\x16introspection_endpoint\x18\x07 \x01(\t\x12\x1d\n\x15grant_types_supported\x18\x08 \x03(\t\x12 \n\x18response_types_supported\x18\t \x03(\t\x12\x1f\n\x17subject_types_supported\x18\n \x03(\t\x12-\n%id_token_signing_alg_values_supported\x18\x0b \x03(\t\x12(\n code_challenge_methods_supported\x18\x0c \x03(\t\x12\x18\n\x10scopes_supported\x18\r \x03(\t\x12-\n%token_endpoint_auth_methods_supported\x18\x0e \x03(\t\x12\x18\n\x10\x63laims_supported\x18\x0f \x03(\t\"W\n\x0fRefreshTokenRef\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\x03\x12\x11\n\tlast_used\x18\x06 \x01(\x03\"!\n\x0eListRefreshReq\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"?\n\x0fListRefreshResp\x12,\n\x0erefresh_tokens\x18\x01 \x03(\x0b\x32\x14.api.RefreshTokenRef\"6\n\x10RevokeRefreshReq\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\"&\n\x11RevokeRefreshResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"4\n\x11VerifyPasswordReq\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"9\n\x12VerifyPasswordResp\x12\x10\n\x08verified\x18\x01 \x01(\x08\x12\x11\n\tnot_found\x18\x02 \x01(\x08\x32\xd1\x08\n\x03\x44\x65x\x12\x34\n\tGetClient\x12\x11.api.GetClientReq\x1a\x12.api.GetClientResp\"\x00\x12=\n\x0c\x43reateClient\x12\x14.api.CreateClientReq\x1a\x15.api.CreateClientResp\"\x00\x12=\n\x0cUpdateClient\x12\x14.api.UpdateClientReq\x1a\x15.api.UpdateClientResp\"\x00\x12=\n\x0c\x44\x65leteClient\x12\x14.api.DeleteClientReq\x1a\x15.api.DeleteClientResp\"\x00\x12\x43\n\x0e\x43reatePassword\x12\x16.api.CreatePasswordReq\x1a\x17.api.CreatePasswordResp\"\x00\x12\x43\n\x0eUpdatePassword\x12\x16.api.UpdatePasswordReq\x1a\x17.api.UpdatePasswordResp\"\x00\x12\x43\n\x0e\x44\x65letePassword\x12\x16.api.DeletePasswordReq\x1a\x17.api.DeletePasswordResp\"\x00\x12>\n\rListPasswords\x12\x14.api.ListPasswordReq\x1a\x15.api.ListPasswordResp\"\x00\x12\x46\n\x0f\x43reateConnector\x12\x17.api.CreateConnectorReq\x1a\x18.api.CreateConnectorResp\"\x00\x12\x46\n\x0fUpdateConnector\x12\x17.api.UpdateConnectorReq\x1a\x18.api.UpdateConnectorResp\"\x00\x12\x46\n\x0f\x44\x65leteConnector\x12\x17.api.DeleteConnectorReq\x1a\x18.api.DeleteConnectorResp\"\x00\x12\x41\n\x0eListConnectors\x12\x15.api.ListConnectorReq\x1a\x16.api.ListConnectorResp\"\x00\x12\x31\n\nGetVersion\x12\x0f.api.VersionReq\x1a\x10.api.VersionResp\"\x00\x12\x37\n\x0cGetDiscovery\x12\x11.api.DiscoveryReq\x1a\x12.api.DiscoveryResp\"\x00\x12:\n\x0bListRefresh\x12\x13.api.ListRefreshReq\x1a\x14.api.ListRefreshResp\"\x00\x12@\n\rRevokeRefresh\x12\x15.api.RevokeRefreshReq\x1a\x16.api.RevokeRefreshResp\"\x00\x12\x43\n\x0eVerifyPassword\x12\x16.api.VerifyPasswordReq\x1a\x17.api.VerifyPasswordResp\"\x00\x42\x36\n\x12\x63om.coreos.dex.apiZ github.com/dexidp/dex/api/v2;apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022com.coreos.dex.apiZ github.com/dexidp/dex/api/v2;api'
  _globals['_CLIENT']._serialized_start=19
  _globals['_CLIENT']._serialized_end=149
  _globals['_GETCLIENTREQ']._serialized_start=151
  _globals['_GETCLIENTREQ']._serialized_end=177
  _globals['_GETCLIENTRESP']._serialized_start=179
  _globals['_GETCLIENTRESP']._serialized_end=223
  _globals['_CREATECLIENTREQ']._serialized_start=225
  _globals['_CREATECLIENTREQ']._serialized_end=271
  _globals['_CREATECLIENTRESP']._serialized_start=273
  _globals['_CREATECLIENTRESP']._serialized_end=344
  _globals['_DELETECLIENTREQ']._serialized_start=346
  _globals['_DELETECLIENTREQ']._serialized_end=375
  _globals['_DELETECLIENTRESP']._serialized_start=377
  _globals['_DELETECLIENTRESP']._serialized_end=414
  _globals['_UPDATECLIENTREQ']._serialized_start=416
  _globals['_UPDATECLIENTREQ']._serialized_end=523
  _globals['_UPDATECLIENTRESP']._serialized_start=525
  _globals['_UPDATECLIENTRESP']._serialized_end=562
  _globals['_PASSWORD']._serialized_start=564
  _globals['_PASSWORD']._serialized_end=638
  _globals['_CREATEPASSWORDREQ']._serialized_start=640
  _globals['_CREATEPASSWORDREQ']._serialized_end=692
  _globals['_CREATEPASSWORDRESP']._serialized_start=694
  _globals['_CREATEPASSWORDRESP']._serialized_end=738
  _globals['_UPDATEPASSWORDREQ']._serialized_start=740
  _globals['_UPDATEPASSWORDREQ']._serialized_end=814
  _globals['_UPDATEPASSWORDRESP']._serialized_start=816
  _globals['_UPDATEPASSWORDRESP']._serialized_end=855
  _globals['_DELETEPASSWORDREQ']._serialized_start=857
  _globals['_DELETEPASSWORDREQ']._serialized_end=891
  _globals['_DELETEPASSWORDRESP']._serialized_start=893
  _globals['_DELETEPASSWORDRESP']._serialized_end=932
  _globals['_LISTPASSWORDREQ']._serialized_start=934
  _globals['_LISTPASSWORDREQ']._serialized_end=951
  _globals['_LISTPASSWORDRESP']._serialized_start=953
  _globals['_LISTPASSWORDRESP']._serialized_end=1005
  _globals['_CONNECTOR']._serialized_start=1007
  _globals['_CONNECTOR']._serialized_end=1074
  _globals['_CREATECONNECTORREQ']._serialized_start=1076
  _globals['_CREATECONNECTORREQ']._serialized_end=1131
  _globals['_CREATECONNECTORRESP']._serialized_start=1133
  _globals['_CREATECONNECTORRESP']._serialized_end=1178
  _globals['_UPDATECONNECTORREQ']._serialized_start=1180
  _globals['_UPDATECONNECTORREQ']._serialized_end=1268
  _globals['_UPDATECONNECTORRESP']._serialized_start=1270
  _globals['_UPDATECONNECTORRESP']._serialized_end=1310
  _globals['_DELETECONNECTORREQ']._serialized_start=1312
  _globals['_DELETECONNECTORREQ']._serialized_end=1344
  _globals['_DELETECONNECTORRESP']._serialized_start=1346
  _globals['_DELETECONNECTORRESP']._serialized_end=1386
  _globals['_LISTCONNECTORREQ']._serialized_start=1388
  _globals['_LISTCONNECTORREQ']._serialized_end=1406
  _globals['_LISTCONNECTORRESP']._serialized_start=1408
  _globals['_LISTCONNECTORRESP']._serialized_end=1463
  _globals['_VERSIONREQ']._serialized_start=1465
  _globals['_VERSIONREQ']._serialized_end=1477
  _globals['_VERSIONRESP']._serialized_start=1479
  _globals['_VERSIONRESP']._serialized_end=1521
  _globals['_DISCOVERYREQ']._serialized_start=1523
  _globals['_DISCOVERYREQ']._serialized_end=1537
  _globals['_DISCOVERYRESP']._serialized_start=1540
  _globals['_DISCOVERYRESP']._serialized_end=2029
  _globals['_REFRESHTOKENREF']._serialized_start=2031
  _globals['_REFRESHTOKENREF']._serialized_end=2118
  _globals['_LISTREFRESHREQ']._serialized_start=2120
  _globals['_LISTREFRESHREQ']._serialized_end=2153
  _globals['_LISTREFRESHRESP']._serialized_start=2155
  _globals['_LISTREFRESHRESP']._serialized_end=2218
  _globals['_REVOKEREFRESHREQ']._serialized_start=2220
  _globals['_REVOKEREFRESHREQ']._serialized_end=2274
  _globals['_REVOKEREFRESHRESP']._serialized_start=2276
  _globals['_REVOKEREFRESHRESP']._serialized_end=2314
  _globals['_VERIFYPASSWORDREQ']._serialized_start=2316
  _globals['_VERIFYPASSWORDREQ']._serialized_end=2368
  _globals['_VERIFYPASSWORDRESP']._serialized_start=2370
  _globals['_VERIFYPASSWORDRESP']._serialized_end=2427
  _globals['_DEX']._serialized_start=2430
  _globals['_DEX']._serialized_end=3535
# @@protoc_insertion_point(module_scope)
