from typing import Union,  Tuple
from pydantic import BaseModel, root_validator


class Vector1Model(BaseModel):
    array: Tuple[Union[int, float]]
    x:  Union[int, float]

    @root_validator(pre=True)
    def create_new_attribute(cls, values) -> Tuple[Union[int, float]]:
        values["x"] = values.get("array")[0]
        return values


class Vector2Model(BaseModel):
    array: Tuple[Union[int, float], Union[int, float]]
    x:  Union[int, float]
    y:  Union[int, float]

    @root_validator(pre=True)
    def create_new_attribute(cls, values) -> Tuple[Union[int, float]]:
        values["x"] = values.get("array")[0]
        values["y"] = values.get("array")[1]
        return values


class Vector3Model(BaseModel):
    array: Tuple[Union[int, float], Union[int, float], Union[int, float]]
    x:  Union[int, float]
    y:  Union[int, float]
    z:  Union[int, float]

    @root_validator(pre=True)
    def create_new_attribute(cls, values) -> Tuple[Union[int, float]]:
        values["x"] = values.get("array")[0]
        values["y"] = values.get("array")[1]
        values["z"] = values.get("array")[2]
        return values


class Vector4Model(BaseModel):
    array: Tuple[Union[int, float], Union[int, float], Union[int, float], Union[int, float]]
    x:  Union[int, float]
    y:  Union[int, float]
    z:  Union[int, float]
    w:  Union[int, float]

    @root_validator(pre=True)
    def create_new_attribute(cls, values) -> Tuple[Union[int, float]]:
        values["x"] = values.get("array")[0]
        values["y"] = values.get("array")[1]
        values["z"] = values.get("array")[2]
        values["w"] = values.get("array")[3]
        return values
