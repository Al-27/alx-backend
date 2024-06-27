#!/usr/bin/python3
"""
Test
"""
import sys

try:
    LFUCache = __import__('100-lfu_cache').LFUCache
    from base_caching import BaseCaching

    BaseCaching.MAX_ITEMS = 5
    LFUCache.MAX_ITEMS = 5
    my_cache = LFUCache()
    my_cache.MAX_ITEMS = 5
    prev_key = None

    for i in range(10):
        key = "key-{}".format(i)
        value = "value-{}".format(i)
        my_cache.put(key, value)
        if prev_key is not None:
            my_cache.get(key)
        prev_key = key
        my_cache.print_cache()

    my_cache.get("key-0")
    my_cache.get("key-4")
    my_cache.get("key-6")
    my_cache.get("key-7")
    my_cache.print_cache()
    my_cache.put("key-20", "value-20")
    my_cache.put("key-21", "value-21")
    my_cache.put("key-22", "value-22")
    my_cache.print_cache()
    my_cache.put("key-20", "value-20")
    my_cache.get("key-20")
    my_cache.get("key-20")
    my_cache.get("key-20")
    my_cache.get("key-20")
    my_cache.get("key-20")
    my_cache.print_cache()
    my_cache.put("key-23", "value-23")
    my_cache.put("key-0", "value-0")
    my_cache.put("key-1", "value-1")
    my_cache.put("key-2", "value-2")
    my_cache.print_cache()

except BaseException:
    print(sys.exc_info()[1])
