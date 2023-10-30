#!/usr/bin/env python3
"""Create a class MRUCache that inherits from BaseCaching and is
a caching system:

You must use self.cache_data - dictionary from the
parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the
parent init: super().__init__()

def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher the BaseCaching.MAX_ITEMS:
you must discard the Most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line

def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Implement cache replacement policy: MRU (Most Recently Used)"""
    def __init__(self):
        """Initialize object"""
        super().__init__()
        self.cache_data = OrderedDict()

    def get(self, key):
        """Implement the parent abstract method get"""
        if key in self.cache_data.keys():
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None

    def put(self, key, item):
        """Implement the parent abstract method put"""
        if key is None or item is None:
            return
        while len(self.cache_data) >= self.MAX_ITEMS:
            most_used_key = self.cache_data.popitem(True)[0]
            print("DISCARD: {}".format(most_used_key))
        self.cache_data[key] = item
