#!/usr/bin/env python3
"""
Module for an asynchronous coroutine that spawns task_wait_random n times
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and returns
    the list of all the delays in ascending order
    """
    delays = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))

    completed_delays = []
    for delay in asyncio.as_completed(delays):
        completed_delays.append(await delay)

    return completed_delays
