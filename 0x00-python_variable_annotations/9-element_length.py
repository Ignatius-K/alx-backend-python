#!/usr/bin/env python3

"""Module defines the `element_length` method"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Gets length of elements

    Args:
        lst: An iterable of sequences

    Return:
        List of items in lst with their length
    """
    return [(i, len(i)) for i in lst]
