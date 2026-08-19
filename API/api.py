from fastapi import FastAPI

app = FastAPI()
@app.get("/Vehicles")
def get_Vehicles():
    return {"HEEEE"}