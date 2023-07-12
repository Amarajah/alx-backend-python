#!/usr/bin/env python3
"""Async Generator."""
import random
import asyncio


async def async_generator():
    value = randint(0, 10)
    for i in range(10):
        await asyncio.sleep(1)
        yield value
