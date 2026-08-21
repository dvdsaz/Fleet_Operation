from fastapi import FastAPI
import json

app = FastAPI()
fleet = {}
with open("../Simulation/fleet.json", "r") as file:
        fleet = json.load(file)

@app.get("/Vehicles")
def get_Vehicles():
    return fleet

@app.get("/Vehicles/{vid}")
def get_Vehicles(vid: str):
    for i in fleet:
         if i["id"] == vid:
              return i
    return {"404 error: Vehicle not Located"}
