from typing import Dict, Optional, Union

from typing_extensions import Literal

from samtranslator.internal.schema_source.common import BaseModel, DictStrAny, PassThroughProp, get_prop

properties = get_prop("sam-resource-graphqlapi")


# TODO: add docs
class Auth(BaseModel):
    Type: str


class Logging(BaseModel):
    CloudWatchLogsRoleArn: Optional[PassThroughProp]
    ExcludeVerboseContent: Optional[PassThroughProp]
    FieldLogLevel: Optional[str]


class DeltaSync(BaseModel):
    BaseTableTTL: str
    DeltaSyncTableName: str
    DeltaSyncTableTTL: str


class DynamoDBDataSource(BaseModel):
    # TableArn, Permissions properties for connector
    ServiceRoleArn: PassThroughProp  # TODO: make optional when we ship connector changes
    TableName: str
    Name: Optional[str]
    Description: Optional[PassThroughProp]
    Region: Optional[PassThroughProp]
    DeltaSync: Optional[DeltaSync]
    UseCallerCredentials: Optional[PassThroughProp]
    Versioned: Optional[PassThroughProp]


class Properties(BaseModel):
    Auth: Auth
    Tags: Optional[DictStrAny]
    Name: Optional[str]
    XrayEnabled: Optional[bool]
    SchemaInline: Optional[str]
    SchemaUri: Optional[str]
    Logging: Optional[Union[Logging, bool]]
    DynamoDBDataSources: Optional[Dict[str, DynamoDBDataSource]]


class Resource(BaseModel):
    Type: Literal["AWS::Serverless::GraphQLApi"]
    Properties: Properties