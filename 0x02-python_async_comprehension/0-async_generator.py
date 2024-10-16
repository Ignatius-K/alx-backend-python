#!/usr/bin/env python3

"""Module defines the `async_generator` method"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generates random number asynchronously

    Yield:
        The random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
