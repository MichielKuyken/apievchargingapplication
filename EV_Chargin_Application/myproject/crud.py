from sqlalchemy.orm import Session

import models
import schemas


def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()


def get_car_by_license_plate(db: Session, nummerplaat: str):
    return db.query(models.Car).filter(models.Car.nummerplaat == nummerplaat).first()


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Car).offset(skip).limit(limit).all()


def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def get_recharges(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Recharge).offset(skip).limit(limit).all()


def create_recharge(db: Session, recharge: schemas.RechargeCreate, car_id: int):
    db_recharge = models.Recharge(**recharge.dict(), car_id=car_id)
    db.add(db_recharge)
    db.commit()
    db.refresh(db_recharge)
    return db_recharge
