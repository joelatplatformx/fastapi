from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-dinosaurs")
async def hello_dinosaurs:():
    return {"message": "Hello, dinosaurs!"}
