import os
from pathlib import Path, WindowsPath
from pydantic import BaseModel, root_validator, validator

from typing import List
from core import utils


PATH_RESOURCE = Path(os.getcwd()) / "resource"

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
    def convertWindowPath(cls, v):
        return Path(PATH_RESOURCE) / str(v)[10:]
    

    @root_validator(pre=True)
    def create_new_attribute(cls, values):
        values["baseName"] = values.get("filePath")
        values["displayName"] = values.get("baseName").split(".")[0]
        return values
    
