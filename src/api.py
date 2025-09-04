from fastapi import FastAPI
from .tier_manager import TierManager

app = FastAPI()
tm = TierManager()

@app.post("/put/{key}")
def put_data(key: str, value: str):
    tm.put(key, value)
    return {"status": "OK", "stored": {key: value}}

@app.get("/get/{key}")
def get_data(key: str):
    value = tm.get(key)
    return {"key": key, "value": value}
