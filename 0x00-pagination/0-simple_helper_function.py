#!/usr/bin/env python3
"""module defining index_range function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start and end index for
    a given page and page size.
    """
    """"""
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)


res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)
