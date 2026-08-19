import json 
import time 

while True:
    with open("fleet.json", "r") as file:
        fleet = json.load(file)
    for i in range(len(fleet)):
        fleet[i]["speed"] = fleet[i]["speed"] - 1
    with open("fleet.json",'w') as file:
        fleet = json.dump(fleet,file, indent =4)
    time.sleep(5)
