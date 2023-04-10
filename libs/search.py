# -*- coding:utf-8 -*-


import os
import functools


@functools.lru_cache(maxsize=None)
def search_files(directory, query):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            if query in name:
                results.append(os.path.join(root, name))

    return results
