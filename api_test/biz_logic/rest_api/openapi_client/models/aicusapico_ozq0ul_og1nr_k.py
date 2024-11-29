# coding: utf-8

"""
    aics-api

    AI-Customer-Service - Core API

    The version of the OpenAPI document: 2024-10-24T04:30:07Z
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.aicusapico_ozq0ul_og1nr_k_input_payload import AicusapicoOzq0ulOG1nrKInputPayload
from typing import Optional, Set
from typing_extensions import Self

class AicusapicoOzq0ulOG1nrK(BaseModel):
    """
    AicusapicoOzq0ulOG1nrK
    """ # noqa: E501
    result: Optional[StrictStr] = None
    execution_id: Optional[StrictStr] = None
    input_payload: Optional[AicusapicoOzq0ulOG1nrKInputPayload] = None
    __properties: ClassVar[List[str]] = ["result", "execution_id", "input_payload"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AicusapicoOzq0ulOG1nrK from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of input_payload
        if self.input_payload:
            _dict['input_payload'] = self.input_payload.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AicusapicoOzq0ulOG1nrK from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "result": obj.get("result"),
            "execution_id": obj.get("execution_id"),
            "input_payload": AicusapicoOzq0ulOG1nrKInputPayload.from_dict(obj["input_payload"]) if obj.get("input_payload") is not None else None
        })
        return _obj

