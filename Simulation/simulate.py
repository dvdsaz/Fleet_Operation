from supabase import create_client
import random
import time 

SUPABASE_URL = "https://ggdxxbtonxxgfexmdsmf.supabase.co"
SUPABASE_KEY = "sb_publishable_1pCyabPlXRTOG9Jaf33q_A_G3qsVxDq"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Connected!")



response = supabase.table("Fleet").select("*").execute()
data = response.data

while True:
    for i in data: 
        i["speed"] -= 1
        response = supabase.table("Fleet").update({"speed": i["speed"]}).eq("id",i["id"]).execute()
        print("updated car ...")
    time.sleep(5)
    print("5 Seconds .....")