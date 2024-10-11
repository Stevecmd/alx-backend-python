#!/usr/bin/env python3
"""
Module for a type-annotated function safely_get_value
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Returns the value for the given key if it exists in the dictionary,
    otherwise returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
