from fastapi import FastAPI
from DB.Supa import supabase

app = FastAPI()

response = supabase.table("Fleet").select("*").execute()
fleet = response.data

@app.get("/")
def home():
    return {"message": "Fleet Operations API is running!"}

#Get all Vehicle in FLeet
@app.get("/vehicles")
def get_Vehicles():
    return fleet

#Get a specific Vehcile
@app.get("/vehicles/{vid}")
def get_Vehicles(vid: int):
    for i in fleet:
         if i["id"] == vid:
              return i
    return {"404 error: Vehicle not Located"} 


#Add a vehicle to the List
@app.post("/vehicles", status_code=201)
def post_vehicle(speed: int, battery: int, temperature: int, status: str):
    veh = {
        "speed": speed,
        "battery": battery,
        "temperature": temperature,
        "status": status
    }
    response = supabase.table("Fleet").insert(veh).execute()
    return {"message": "Vehicle Added Successfully", "vehicle": response.data}



#Delete specific vehicle
@app.delete("/vehicle")
def delete_vehicle(vid: int):
    for i in fleet:
         if i["id"] == vid:
              response = supabase.table("Fleet").delete().eq("id", i["id"]).execute()
              return {"message": "Vehicle Deleted Successfully" , "vehicle": response.data}

    return {"404 error: Vehicle not Located"} 