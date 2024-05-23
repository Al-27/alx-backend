#!/usr/bin/python3
""" Caching module
"""
BaseCaching = __import__("base_caching").BaseCaching

class BasicCache(BaseCaching):
    """
    class doc
    """
    
    def __init__(self):
        """func
        """
        super()
        self.MAX_ITEMS = 99999
    
    def put(self, key, item):
        """func
        """
        if not (key is None or item is None):
            self.cache_data.update({key,item})
    
    def get(self, key):
        """func
        """
        return self.cache_data.get(key)