#!/usr/bin/env python3

"""Module defines `task_wait_n` coroutine"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times

    Args:
        n: The number of times to execute task_wait_random
        max_delay: The maximum delay for task_wait_random

    Return:
        The delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
