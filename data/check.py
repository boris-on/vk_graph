import os
from lists_mas import list_names, list_id, list_total
import pickle

list_id= list_id.split("\n")[:700]
for files in os.walk("./id_lists"):
    filenames = files[2]
    filenames = [file[:-4] for file in filenames]
list_not_ready = []
for el in range(len(list_id)):
    if list_id[el] not in filenames:
        list_not_ready.append(el)

with open("list_unready.txt", "wb") as f:
    pickle.dump(list_not_ready, f)
# import pickle
with open("list_unready.txt", "rb") as f:
    data = pickle.load(f)
print(data)
# import pickle
# from lists_mas import list_names, list_id, list_total
# # with open("dict1.txt", "rb") as f:
# #     data = pickle.load(f)


# list_names= list_names.split("\n")
# list_id= list_id.split("\n")
list_total = list_total.split("\n")
# print(len(list_id))