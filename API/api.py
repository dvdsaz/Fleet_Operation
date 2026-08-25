from fastapi import FastAPI
import json

app = FastAPI()
fleet = {}
with open("../utilities/fleet.json", "r") as file:
        fleet = json.load(file)
#I need to figure out how to run this in the simulate.py file
def read_json():
    with open("../utilities/fleet.json", "r") as file:
        fleet = json.load(file)


#Get all Vehicle in FLeet
@app.get("/vehicles")
def get_Vehicles():
    return fleet

#Get a specific Vehcile
@app.get("/vehicles/{vid}")
def get_Vehicles(vid: str):
    for i in fleet:
         if i["id"] == vid:
              return i
    return {"404 error: Vehicle not Located"} 


#Add a vehicle to the List
@app.post("/vehicles")
def post_vehicle(vid: str):
    veh = {
        "id": vid,
        "speed": 0,
        "battery": 80,
        "temperature": 50,
        "status": "Active"
    }
    fleet.append(veh) 
    with open("../utilities/fleet.json", "w") as file:
            json.dump(fleet, file, indent=4)
    return veh
#Delete specific vehicle
@app.delete("/vehicle")
def get_Vehicles(vid: str):
    for i in fleet:
         if i["id"] == vid:
              fleet.remove(i)
              with open("../utilities/fleet.json", "w") as file:
                    json.dump(fleet, file, indent=4)
              return {"Vehicle Found and Deleted"}

    return {"404 error: Vehicle not Located"} 