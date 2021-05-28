import pickle
import os
from lists_mas import list_names, list_id, list_total
import sys
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import itertools
for files in os.walk("./id_lists"):
    filenames = files[2]
    filenames = [file[:-4] for file in filenames]


list_names= list_names.split("\n")[:500]
list_id= list_id.split("\n")[:500]
list_total = list_total.split("\n")[:500]
i=0

def obr(file):
    if file in list_id:
        path = "id_lists/" + file + ".txt"
        with open("dict2.txt", "rb") as d:
            data = pickle.load(d)
        with open(path, "rb") as f:
            cur_dict = pickle.load(f)
        data[int(file)] = cur_dict[3]
        # print(data)
        with open("dict2.txt", "wb") as ff:
            pickle.dump(data, ff)

def run(func, arr):
    with concurrent.futures.ThreadPoolExecutor(12) as pool:
        results = list(tqdm(pool.map(func, arr), total=len(arr)))
        return results


results = run(obr, filenames)

with open("dict2.txt", "wb") as d:
    pickle.dump({1: ['1'], 2: ['2', '3']}, d)

with open("dict2.txt", "rb") as d:
    data = pickle.load(d)
print(data)