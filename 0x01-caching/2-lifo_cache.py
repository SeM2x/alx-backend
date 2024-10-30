#!/usr/bin/env python3
""" module to implement LIFOCache class """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.last_key = ""

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print("DISCARD: {}".format(self.last_key))
        self.last_key = key

    def get(self, key):
        """ Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
