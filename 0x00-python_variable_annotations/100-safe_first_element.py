#!/usr/bin/env python3

"""Module defines `safe_first_element` method"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Gets the first element in lst"""
    if lst:
        return lst[0]
    else:
        return None
