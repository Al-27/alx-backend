#!/usr/bin/python3
""" Caching module
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    class doc
    """

    def __init__(self, *args, **kwargs):
        """func
        """
        super().__init__(*args, **kwargs)

    def put(self, key, item):
        """func
        """
        if not (key is None or item is None):
            while len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                k, v = self.cache_data.popitem()
                print(f"DISCARD: {k}")
            self.cache_data.update({key: item})

    def get(self, key):
        """func
        """
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data.update({key: value})

        return self.cache_data.get(key)
