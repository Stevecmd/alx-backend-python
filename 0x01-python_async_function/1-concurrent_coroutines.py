#!/usr/bin/env python3
"""
Module for an asynchronous coroutine that spawns wait_random n times
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns
    the list of all the delays in ascending order
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delays = []
    for delay in asyncio.as_completed(delays):
        completed_delays.append(await delay)

    return completed_delays
