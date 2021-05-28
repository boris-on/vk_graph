import json

with open("result3.json", "rb") as f:
    data1 = json.load(f)
dict_common=[]
print(len(data1["nodes"]))
data = {"nodes": [], "links": []}

for node in data1["nodes"]:
    data["nodes"].append(node)

for link in data1["links"]:
    if link["source"] != link["target"]:
        data["links"].append(link)

for link in data["links"]:
    print(link["value_min"])
    if link["value_min"] > 0.25:
        if link["source"] not in dict_common:
            dict_common.append(link["source"])
        if link["target"] not in dict_common:
            dict_common.append(link["target"])
print(len(dict_common))

new_js = {"nodes": [], "links": []}
for node in data["nodes"]:
    if node["id"] in dict_common:
        new_js["nodes"].append(node)


print(len(new_js["nodes"]))
for link in data["links"]:
    if link["source"] in dict_common and link["target"] in dict_common:
        new_js["links"].append(link)

with open("result4.json", "w") as f:
    json.dump(new_js, f)
