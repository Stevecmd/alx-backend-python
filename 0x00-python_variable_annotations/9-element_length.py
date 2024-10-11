#!/usr/bin/env python3
"""
Module for a type-annotated function element_length
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element
    from the input list and its length
    """
    return [(i, len(i)) for i in lst]
