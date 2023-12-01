from datetime import datetime

from pydantic import BaseModel, ConfigDict
from pydantic.functional_serializers import PlainSerializer
from typing_extensions import Annotated

from .utils import to_camel


class CamelModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


DateTime = Annotated[
    datetime, PlainSerializer(lambda x: x.strftime("%Y-%m-%dT%H:%M:%S"), return_type=str, when_used="json-unless-none")
]
