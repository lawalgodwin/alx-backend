#!/usr/bin/env python3
"""Create a class LIFOCache that inherits from BaseCaching and is a
caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the
parent init: super().__init__()

def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher the BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line

def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return Non
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implement cache replacement policy: LIFO"""
    def __init__(self):
        """Initialize object"""
        super().__init__()

    def put(self, key, item):
        """implement the parent class abstract put method"""
        if key is None or item is None:
            return
        while (len(self.cache_data) >= self.MAX_ITEMS):
            last_inserted_key = sorted(self.cache_data.keys())[-1]
            del self.cache_data[last_inserted_key]
            print("DISCARD: {}".format(last_inserted_key))
        self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)
