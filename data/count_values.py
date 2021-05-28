from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import itertools
import time
import pickle
import numpy as np
import json
from lists_mas import list_names, list_id, list_total
import os

d = {
    "nodes": [],
    "links": []
}

for files in os.walk("./id_lists"):
    filenames = files[2]
    filenames = [file[:-4] for file in filenames]

list_names= list_names.split("\n")[100:500]
list_id= list_id.split("\n")[100:500]
list_total = list_total.split("\n")[100:500]
arr = []
# print(len(list_id))
for group1 in range(len(list_id)):
    for group2 in range(group1, len(list_id)):
        if list_id[group1] in filenames and list_id[group2] in filenames:
            id1, id2 = int(list_id[group1]), int(list_id[group2])
            arr.append((id1, id2))

for id in range(len(list_id)):
    if list_id[id] in filenames:
        d["nodes"].append({"id": int(list_id[id]), "name": list_names[id]})

def get_users(id):
    file_name = "id_lists/" + str(id) + ".txt"
    with open(file_name, 'rb') as f:
        data = pickle.load(f)
        # print(data)
    return data[3]

# get_users("491")

def metric(x):
    src = x[0]
    tg = x[1]
    src_users, tg_useres = get_users(src), get_users(tg)
    m = len(np.intersect1d(src_users, tg_useres,
                           assume_unique=True)) 

    return {"source": src, "target": tg, "value_common": m, "value_min": m/min([len(src_users), len(tg_useres)]), "len1": len(src_users), "len2": len(tg_useres)}

def run(metric, arr):
    with concurrent.futures.ThreadPoolExecutor(12) as pool:
        results = list(tqdm(pool.map(metric, arr), total=len(arr)))
        return results

results = run(metric, arr)

for el in results:
    d["links"].append(el)

with open('result3.json', 'w') as fp:
    json.dump(d, fp)
