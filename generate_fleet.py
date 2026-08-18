import random
import json
fleet = []
for i in range(10):
    id = f'AV_{i}'
    battery = random.randint(30,80)
    status = random.choice(['Active','Charging'])
    fleet.append({"id": id,"battery":battery,"status":status})

with open("fleet.json", "w") as file:
    json.dump(fleet,file, indent =4)

