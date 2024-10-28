#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data with hypermedia pagination,
        accounting for deleted records.
        """
        data = self.indexed_dataset()

        assert index >= 0 and index < len(data)
        deleted_index = None
        for key, val in data.items():
            if val != list(data.values())[key]:
                deleted_index = key
                break

        start = list(data.items())[index][0]
        end = list(data.items())[index+page_size-1][0]
        diff = start - index

        includes_deleted = isinstance(
            deleted_index, int
        ) and deleted_index >= start and deleted_index <= end
        if (includes_deleted):
            next_index = end + 1
        else:
            index = index - diff
            next_index = index + page_size

        page_data = list(data.values())[index: next_index]
        return {
            "index": index if includes_deleted else index + diff,
            "next_index": next_index if includes_deleted else
            next_index + diff,
            "page_size": len(page_data),
            "data": page_data
        }
