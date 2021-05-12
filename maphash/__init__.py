__version__ = "0.1.0"

import hashlib
import json
from typing import Dict, List, Optional, Union

Serializable = Optional[Union[Dict, List, str, int, float]]


def json_dump(obj: Serializable) -> str:
    """ Serialize the given object in a fixed and predefined format.

    Args:
        obj:
            Object to serialize.

    Returns:
        JSON serialized object.
    """
    return json.dumps(obj, indent=2, sort_keys=True)


def maphash(obj: Serializable) -> str:
    """ Hash the given object.

    Args:
        obj:
            Object to hash.

    Returns:
        Hash of the object.
    """
    return hashlib.sha3_256(json_dump(obj).encode("utf-8")).hexdigest()
