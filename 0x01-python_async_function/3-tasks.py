#!/usr/bin/env python3

"""Module defines the `task_wait_random method`"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Generates a Task for wait_random"""
    return asyncio.create_task(wait_random(max_delay))
