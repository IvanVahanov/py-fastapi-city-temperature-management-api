from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.dependencies import get_db
import asyncio

router = APIRouter()

@router.get("/temperatures/", response_model=list[schemas.Temperature])
def get_temperatures(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_temperatures(db=db, skip=skip, limit=limit)

@router.get("/temperatures/", response_model=list[schemas.Temperature])
def get_temperatures_by_city(city_id: int, db: Session = Depends(get_db)):
    db_temperatures = crud.get_temperatures_by_city(db=db, city_id=city_id)
    if not db_temperatures:
        raise HTTPException(status_code=404, detail="No temperature records found for the city")
    return db_temperatures

@router.post("/temperatures/update")
async def update_temperatures(db: Session = Depends(get_db)):
    await crud.update_city_temperatures(db=db)
    return {"detail": "Temperatures updated"}
