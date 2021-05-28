import os
from lists_mas import list_names, list_id, list_total
import pickle
import numpy 
list_names= list_names.split("\n")
list_id= list_id.split("\n")
list_total = list_total.split("\n")

for files in os.walk("./id_lists"):
    filenames = files[2]

for file in filenames:
    full_path = "id_lists/" + file
    with open(full_path, "rb") as f:
        data = pickle.load(f)
        users = data[3]
        new_list = numpy.array(users)
    second_path = "new_id/" + file
    # print(second_path, new_list)
    with open(second_path, "wb") as d:
        pickle.dump(new_list, d)
    print(file)