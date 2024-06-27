#!/usr/bin/env python3
"""
this is a doc
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """func
        """
        assert (page is int and page > 0 and page_size > 0 and page_size is int)

        if len(self.__dataset) / page_size < page:
            return []

        start_idx = (page - 1) * page_size
        end_idx = page_size * page

        return self.__dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """func
        """
        d_list = self.get_page(page, page_size)

        next_p = page + 1 if tot_p > page + 1 else None
        prev_p = page - 1 if page > 1 else None
        tot_p = int(len(self.__dataset) / page_size)

        return dict(
            page_size=len(d_list),
            page=page,
            data=d_list,
            next_page=next_p,
            prev_p=prev_p,
            total_pages=tot_p)
