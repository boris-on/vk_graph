import pickle
from lists_mas import list_names, list_id, list_total
with open("dict1.txt", "rb") as f:
    data = pickle.load(f)


list_names= list_names.split("\n")
list_id= list_id.split("\n")
list_total = list_total.split("\n")

# print(list(data.keys())[1:4])

for el in range(len(list_id)):
    if list_id[el] in list(data.keys())[1:]:
        file_name = "id_lists/" + list_id[el] + ".txt"
        final_arr = [list_names[el], int(list_id[el]), int(list_total[el]), data[list_id[el]]]
        with open(file_name, "wb") as f:
            pickle.dump(final_arr, f)
        print(el)