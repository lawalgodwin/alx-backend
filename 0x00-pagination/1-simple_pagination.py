#!/usr/bin/env python3
"""Implement a method named get_page that takes two
   integer arguments page with default value 1 and
   page_size with default value 10.
   You have to use this CSV file
   (same as the one presented at the top of the project)
   Use assert to verify that both arguments are integers greater than 0.
   Use index_range to find the correct indexes to paginate the dataset
   correctly and return the appropriate page of the dataset
   (i.e. the correct list of rows).

   If the input arguments are out of range for the dataset,
   an empty list should be returned.
   """

import csv
import math
from typing import List


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a
    start index and an end index corresponding to the range of indexes
    to return in a list
    """
    start_index = page_size * (page - 1)
    end_index = page * page_size
    return (start_index, end_index)


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
