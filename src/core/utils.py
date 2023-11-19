import codecs
import glob
import json
from typing import Any, List


def loadJson(path: str, decoding: str = "utf-8-sig") -> Any:
    """
    Loads JSON data from a file.

    Parameters:
    path: Path to the JSON file.
    decoding: The character encoding for reading the file. Defaults to 'utf-8-sig'.

    Returns:
    The loaded JSON data.
    """
    try:
        with codecs.open(path, "r", encoding=decoding) as file:
            return json.load(file)
    except Exception as e:
        raise IOError(f"Error loading JSON from {path}: {e}")


def saveFile(path: str, data: Any) -> None:
    """
    Saves data to a file.

    Parameters:
    path: Path where the data will be saved.
    data: Data to be written to the file.
    """
    try:
        with open(path, mode="w") as f:
            f.write(data)
    except Exception as e:
        raise IOError(f"Error saving data to file {path}: {e}")


def saveJson(path: str, data: Any) -> None:
    """
    Saves data as JSON to a file.

    Parameters:
    path: Path where the JSON data will be saved.
    data: Data to be serialized and saved as JSON.
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        raise IOError(f"Error saving JSON to file {path}: {e}")


def getExtList(path: str = "", ext: str = ".json") -> List[str]:
    """
    Gets a list of files with a specific extension.

    Parameters:
    path: The root directory path to search in. If empty, it defaults to the current directory.
    ext: The file extension to look for. Defaults to '.json'.

    Returns:
    A list of file paths matching the specified extension.
    """
    try:
        pattern = f"{path}/**/*{ext}" if path else f"**/*{ext}"
        return [file.replace("\\", "/") for file in glob.glob(pattern, recursive=True)]
    except Exception as e:
        raise IOError(f"Error retrieving files from {path}: {e}")
