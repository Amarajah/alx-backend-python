#!/usr/bin/env python3
""" 1-concurrent_coroutines """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> List[int]:
    """return a list of float arrays. """
    delays: List[float] = []
    delay: Any = None
    for i in range(n):
        delay = await wait_random(max_delay)
        if (delay is not None):
            delays.append(delay)
    return delays
