from lists_mas import list_names, list_id, list_total
import pickle
import json
import requests
import sys
import numpy 
import time

list_names= list_names.split("\n")
list_id= list_id.split("\n")
list_total = list_total.split("\n")

with open("list_unready.txt", "rb") as f:
    list_unready = pickle.load(f)


num = 1
for group in range(len(list_id)):
    if group in list_unready:
        status=1
        name = list_names[group]
        group_id = int(list_id[group])
        user_num = int(list_total[group])//1000 + 1
        session = requests.Session()
        list_users = []
        try:
            for offset in range(0, user_num, 25):
                response_url = "https://api.vk.com/method/execute?code=return ["
                for j in range(25):
                    response_url += """API.groups.getMembers({{"group_id":{0},"count":1000,"offset":{1}}}),""".format(group_id, str((offset+j)*1000))
                response_url += "];&v=5.124&access_token=fa70318aee7d512540e611fc0a0429a296b805e59fe9bb095876a22e4564aecff48952ede9744c6bbca16"
                response = session.get(response_url)
                json_data = json.loads(response.text)
                for item in json_data['response']:
                    for user_id in item['items']:
                        list_users.append(user_id)

                
                time.sleep(0.3)
                sys.stdout.write("\r{0}% parsed of {1} ({2} out of hz)".format(int((offset/user_num)//0.01), group_id, num))
                
                sys.stdout.flush()
        except Exception as e:
            time.sleep(1)   
            print(json_data, group_id)
            status = 0
        time.sleep(10)
        num+=1

        list_users = numpy.array(list_users)
        final_arr = [name, group_id, user_num, list_users]
        file_name = "id_lists/" + str(group_id) + ".txt"
        if status:
            with open(file_name, "wb") as f:
                pickle.dump(final_arr, f)



