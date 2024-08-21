from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Root"}

@app.get("/obj")
def obj():
    return {"json": {"obj": 1}}
