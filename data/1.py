from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import itertools
import time
import pickle
import numpy as np
import json

with open('dict1.txt', 'rb') as f:
    data = pickle.load(f)

temp = {}
for el in list(data.keys())[1:]:
    temp[int(el)] = np.sort(data[el])


data = temp
del temp

d = {
    "nodes": [],
    "links": []
}

for el in list(data.keys()):
    d["nodes"].append({"id": el})


def metric2(x):
    src = x[0]
    tg = x[1]
    m = len(np.intersect1d(data[src], data[tg],
                           assume_unique=True)) / len(data[src])

    return {"source": src, "target": tg, "value": m}


pool = ThreadPoolExecutor(12)

arr = []
for r in itertools.product(list(data.keys()), list(data.keys())):
    if r[0] != r[1]:
        arr.append((r[0], r[1]))


def run(metric2, arr):
    with concurrent.futures.ThreadPoolExecutor(12) as pool:
        results = list(tqdm(pool.map(metric2, arr), total=len(arr)))
        return results


results = run(metric2, arr)

for el in results:
    d["links"].append(el)

with open('result.json', 'w') as fp:
    json.dump(d, fp)
