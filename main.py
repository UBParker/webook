from fastapi import FastAPI
from app.routes.flights import router as flights_router

app = FastAPI()

# Register routes
app.include_router(flights_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to we.book - Your AI Travel Assistant"}
