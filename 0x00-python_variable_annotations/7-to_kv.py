#!/usr/bin/env python3

"""Module defines the `to_kv` method"""

from typing import Tuple, Union

IntOrFloat = Union[int, float]
KVTuple = Tuple[str, float]


def to_kv(k: str, v: IntOrFloat) -> KVTuple:
    """Returns k and square of v"""
    return k, v**2
