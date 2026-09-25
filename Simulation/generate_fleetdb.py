from DB.Supa import supabase
import random

for i in range(10):
    battery = random.randint(30,80)
    speed = random.randint(25,45)
    temperature = random.randint(20,100)
    status = random.choice(['Active','Charging'])
    data = {
    "speed": speed,
    "battery":battery,
    "temperature":temperature,
    "status": status
}
    response = supabase.table("Fleet").insert(data).execute()

print(response.data)