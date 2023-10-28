#!/usr/bin/env python3
"""Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments (and defaults)
as get_page and returns a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary.
"""
import csv
import math
from typing import List, Mapping, Tuple
import math

index_range = __import__('0-simple_helper_function').index_range


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
        """Return the appropriate page of dataset(the correct list of rows)"""
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert ((page > 0) and (page_size > 0))
        (start_index, end_index) = index_range(page, page_size)
        all_data = self.dataset()
        try:
            requested_dataset = all_data[start_index: end_index]
            return requested_dataset
        except IndexError:
            return []

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> dict:
        """Implement HATEOAS concept to make the API intuitive to use"""
        hypermedia_response = {}
        result = self.get_page(page, page_size)
        total_pages = math.ceil(len(result) / page_size)
        hypermedia_response = {
            "page_size": len(result),
            "page": page,
            "data": result,
            "next_page": (page + 1) if page < total_pages else None,
            "prev_page": (page - 1) if page - 1 else None,
            "total_pages": total_pages
        }
        return hypermedia_response
