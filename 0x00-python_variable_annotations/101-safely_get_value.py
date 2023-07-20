#!/usr/bin/env python3
"""Given the parameters and the return values,
add type annotations to the function."""
from typing import Union, Any, Mapping, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                    default: Optional[T] = None) -> Union[Any, T]:
    """Safely gets value from dictionary.
    Returns:
        Value from dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
