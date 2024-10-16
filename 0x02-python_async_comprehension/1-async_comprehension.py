#!/usr/bin/env python3

"""Module defines `async_comprehension` method"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """
    Generate ten random numbers

    Return:
        The list of random numbers
    """
    return [ value async for value in async_generator() ]
