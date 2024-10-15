#!/usr/bin/env python3

"""Module defines `measure_time` method"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures execution time

    Args:
        n: Number of times to executes wait_n
        max_delay: Maximum delay of wait_n

    Return:
        The approximate elapsed time per n
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()

    return (end_time - start_time) / n
