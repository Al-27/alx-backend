#!/usr/bin/env python3
"""
this is a doc
"""


def index_range(page, page_size):
    """func
    """
    range_ = [(page - 1) * page_size, page_size * page]

    return tuple(range_)
