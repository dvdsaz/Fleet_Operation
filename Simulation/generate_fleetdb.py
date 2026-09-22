from supabase import create_client
import random

SUPABASE_URL = "https://ggdxxbtonxxgfexmdsmf.supabase.co"
SUPABASE_KEY = "sb_publishable_1pCyabPlXRTOG9Jaf33q_A_G3qsVxDq"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Connected!")
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