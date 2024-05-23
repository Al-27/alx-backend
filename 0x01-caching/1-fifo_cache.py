#!/usr/bin/python3
""" Caching module
"""
BaseCaching = __import__("base_caching").BaseCaching

class FIFOCache(BaseCaching):
    """
    class doc
    """
    
    def __init__(self,*args, **kwargs):
        """func
        """
        super().__init__(*args, **kwargs)
    
    def put(self, key, item):
        """func
        """
        if not (key is None or item is None):
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                fo_key = list(self.cache_data.keys())[0]
                discarded = self.cache_data.pop(fo_key)
                print(f"DISCARD: {discarded.key}")
            self.cache_data[key] = item
    
    def get(self, key):
        """func
        """
        return self.cache_data.get(key)