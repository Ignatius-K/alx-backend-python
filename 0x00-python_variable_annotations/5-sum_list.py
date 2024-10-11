#!/usr/bin/env python3

"""Module explores annotating collections"""

from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums up a float list

    Args:
        input_list: List of floats

    Return:
        The sum of floats
    """
    return reduce(lambda a, b: a + b, input_list)
