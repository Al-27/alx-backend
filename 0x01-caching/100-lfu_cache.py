#!/usr/bin/python3
""" Caching module
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    class doc
    """

    def __init__(self, *args, **kwargs):
        """func
        """
        super().__init__(*args, **kwargs)
        self.cache_freq = {}

    def put(self, key, item):
        """func
        """
        if not (key is None or item is None):
            while len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                fo_key = self.get_lf_key(self.cache_freq)
                if isinstance(fo_key, list):
                    for k in list(self.cache_data.keys())[::-1]:
                        if k in fo_key:
                            fo_key = k
                            break
                self.cache_data.pop(fo_key)
                self.cache_freq.pop(fo_key)
                print(f"DISCARD: {fo_key}")

            self.cache_data.update({key: item})
            self.cache_freq.update({key: 1})

    def get(self, key):
        """func
        """
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data.update({key: value})
        self.cache_freq[key] += 1

        return self.cache_data.get(key)

    def get_lf_key(self, dic):
        """
        return key of the item with least freq(LF)
        return list of keys if there more than one item with LF
        """
        vals = list(dic.values())
        min_n = min(vals)
        n_times = vals.count(min_n)

        if n_times == 1:
            return list(dic)[vals.index(min_n)]
        else:
            keys = []
            for k, v in dic.items():
                if v == min_n:
                    keys.append(k)
            return keys
