#!/usr/bin/env python3
"""
Module for a type-annotated function to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k
    and the second element is the square of the int/float v as a float
    """
    return (k, float(v ** 2))
