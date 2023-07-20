#!/usr/bin/env python3
"""The types of the elements of the input are not know."""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a list or None if list is empty."""
    if lst:
        return lst[0]
    else:
        return None
