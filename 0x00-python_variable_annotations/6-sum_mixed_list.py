#!/usr/bin/env python3

from functools import reduce
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Sums up a list of floats and integers

    Args:
        mxd_lst: The list of mixed values

    Return:
        The sum
    """
    return reduce(lambda a, b: a + b, mxd_lst)
