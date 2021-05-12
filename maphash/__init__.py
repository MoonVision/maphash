__version__ = "0.1.0"

import hashlib
import json
from typing import Dict, List, Union

Serializable = Union[Dict, List, str, int, float]


def json_dump(obj: Serializable) -> str:
    """"""
    return json.dumps(obj, indent=2, sort_keys=True,)


def maphash(obj: Serializable) -> str:
    """"""
    return hashlib.sha3_256(json_dump(obj),).hexdigest()
