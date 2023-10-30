#!/usr/bin/env python3
"""Create a class BasicCache that inherits from BaseCaching and is a caching
system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implement a basic cache"""
    def __init__(self):
        """class constructor"""
        super().__init__()

    def put(self, key, item):
        """implement parent class abstract put method"""
        if (key is None) or (item is None):
            pass
        self.cache_data[key] = item

    def get(self, key: str):
        """Implement parent class abstract get method"""
        return self.cache_data.get(key, None)
