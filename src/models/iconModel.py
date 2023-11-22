import os
from pathlib import Path, WindowsPath
from pydantic import BaseModel, root_validator, validator

from typing import List, Dict


PATH_RESOURCE = Path().cwd() / "resource"


class IconModel(BaseModel):
    displayName: str
    assetVersion: int
    imageUrl: WindowsPath
    filePath: WindowsPath
    lastAuthor: str
    fileUpdateTime: str
    authors: List[str]
    baseName: str
    displayName: str

    @validator("imageUrl")
    def convertWindowPath(cls, v) -> WindowsPath:
        return Path(PATH_RESOURCE) / str(v)[10:]

    @root_validator(pre=True)
    def create_new_attribute(cls, values) -> Dict:
        values["baseName"] = values.get("filePath").name
        values["displayName"] = values.get("filePath").stem
        return values
