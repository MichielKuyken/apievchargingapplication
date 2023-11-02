from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# "sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/cars/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    car_nummerplaat = crud.get_car_by_license_plate(db, nummerplaat=car.nummerplaat)
    if car_nummerplaat:
        raise HTTPException(status_code=400, detail="License plate already registred")
    return crud.create_car(db=db, car=car)


@app.get("/cars/", response_model=list[schemas.Car])
def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cars = crud.get_cars(db, skip=skip, limit=limit)
    return cars


@app.get("/cars/{car_id}", response_model=schemas.Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    car = crud.get_car(db, car_id=car_id)
    if car_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return car


@app.post("/cars/{car_id}/recharges/", response_model=schemas.Recharge)
def create_item_for_user(car_id: int, recharge: schemas.RechargeCreate, db: Session = Depends(get_db)):
    return crud.create_recharge(db=db, recharge=recharge, car_id=car_id)


@app.get("/recharges/", response_model=list[schemas.Recharge])
def read_recharges(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    recharges = crud.get_recharges(db, skip=skip, limit=limit)
    return recharges
