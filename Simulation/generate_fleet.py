import random
import json
fleet = []
for i in range(10):
    id = f'AV_{i}'
    battery = random.randint(30,80)
    speed = random.randint(25,45)
    temperature = random.randint(20,100)
    status = random.choice(['Active','Charging'])
    fleet.append({"id": id,
                  "speed": speed,
                  "battery":battery,
                  "temperature": temperature,
                  "status":status})

with open("utilities/fleet.json", "w") as file:
    json.dump(fleet,file, indent =4)


