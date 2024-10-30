#!/usr/bin/env python3
""" module to implement LFUCache class """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        from collections import OrderedDict
        self.cache_data = OrderedDict()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:

            lfu_key = min(self.frequency, key=self.frequency.get)
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            print("DISCARD: {}".format(lfu_key))

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
