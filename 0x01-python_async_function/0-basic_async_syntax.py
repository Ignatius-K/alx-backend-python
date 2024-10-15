#!/usr/bin/env python3

"""Module defines `wait_random` method"""

import asyncio
import random


MIN_DELAY = 0


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for delay
    between 0 and max_delay

    Args:
        max_delay: The maximum delay

    Return:
        The delay
    """
    delay = random.uniform(MIN_DELAY, max_delay)
    await asyncio.sleep(delay=delay)
    return delay
