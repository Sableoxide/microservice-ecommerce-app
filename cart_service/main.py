from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_route():
    return {"message": "welcome to rooit"}