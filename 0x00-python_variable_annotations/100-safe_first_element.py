#!/usr/bin/env python3
"""
Module for a type-annotated function safe_first_element
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it exists, otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
