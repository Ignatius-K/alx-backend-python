#!/usr/bin/env python3

"""Module defines the `sum_mixed_list` method"""

from functools import reduce
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums up a list of floats and integers

    Args:
        mxd_lst: The list of mixed values

    Return:
        The sum
    """
    return reduce(lambda a, b: a + b, mxd_lst)
