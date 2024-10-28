#!/usr/bin/env python3
"""module defining index_range function"""
import csv
from typing import List
from typing import Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start and end index for
    a given page and page size.
    """
    """"""
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)


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
        """
        Retrieve a specific page of the dataset.
        """
        assert isinstance(
            page, int) and page > 0
        assert isinstance(
            page_size, int) and page_size > 0
        self.dataset()
        (start, end) = index_range(page, page_size)
        if self.__dataset:
            return self.__dataset[start: end]
        return None

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination details including page size,
        current page, data, next page, previous page, and total pages.
        """
        next = None
        try:
            data = self.get_page(page, page_size)
            next = self.get_page(page+1, page_size)
        except Exception:
            pass

        total = len(self.__dataset) / page_size
        total = int(total + 1) if total - int(total) > 0 else int(total)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": None if not next else page + 1,
            "prev_page": None if page <= 1 else page - 1,
            "total_pages": total
        }
