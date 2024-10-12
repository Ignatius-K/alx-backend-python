#!/usr/bin/env python3

"""Module that defines `make_multiplier` method"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Generates multiplier

    Arg:
        multiplier: The value to multiply with

    Return:
        Function that multiplies its arg with multiplier
    """
    return lambda x: x*multiplier
