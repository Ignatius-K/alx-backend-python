#!/usr/bin/env python3

"""Module defines `wait_n` coroutine"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times

    Args:
        n: The number of times to execute wait_random
        max_delay: The maximum delay for wait_random

    Return:
        The delays
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return delays
