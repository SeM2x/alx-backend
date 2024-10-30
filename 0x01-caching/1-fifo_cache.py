#!/usr/bin/env python3
""" module to implement FIFOCache class """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache class """

    def __init__(self):
        """ Constructor """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            key = keys[0]
            del self.cache_data[key]
            print("DISCARD: {}".format(key))

    def get(self, key):
        """ Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
