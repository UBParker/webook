from fastapi import APIRouter

router = APIRouter()

@router.get("/search")
def search_flights():
    return {"message": "This will handle flight search"}

@router.post("/book")
def book_flight():
    return {"message": "This will handle flight booking"}
