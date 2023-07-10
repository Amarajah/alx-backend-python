#!/usr/bin/env python3
"""more async."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """multiple coroutines at the same time with async."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

