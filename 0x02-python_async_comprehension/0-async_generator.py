#!/usr/bin/env python3

"""Module defines the `async_generator` method"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Generates random number asynchronously

    Yield:
        The random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
