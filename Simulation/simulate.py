from DB.Supa import supabase
import time 


response = supabase.table("Fleet").select("*").execute()
data = response.data

while True:
    for i in data: 
        i["speed"] -= 1
        response = supabase.table("Fleet").update({"speed": i["speed"]}).eq("id",i["id"]).execute()
        print("updated car ...")
    time.sleep(5)
    print("5 Seconds .....")