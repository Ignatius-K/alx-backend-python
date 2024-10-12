#!/usr/bin/env python3

"""
Given the parameters and the return values,
add type annotations to the function
Hint: look into TypeVar

"""

from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')
ValueType = Union[T, None]


def safely_get_value(
    dct: Mapping, key: Any, default: ValueType = None
) -> ValueType:
    """Safely gets value from dct"""
    if key in dct:
        return dct[key]
    else:
        return default
