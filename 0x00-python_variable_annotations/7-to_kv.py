#!/usr/bin/env python3
"""type-annotated function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes string k and int OR float v as arguments and returns a tuple."""
    return (k, v ** 2)
