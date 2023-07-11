#!/usr/bin/env python3
"""more async."""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> List[int]:
    """multiple coroutines at the same time with async."""
    delays: List[float] = []
    delay: Any = None
    for i in range(n):
        delay = await wait_random(max_delay)
        if (delay is not None)
            delays.append(delay)
    return delays
