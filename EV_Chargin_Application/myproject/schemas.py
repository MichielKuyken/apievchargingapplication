from pydantic import BaseModel
from datetime import datetime

class CarBase(BaseModel):
    nummerplaat: str
    auto: str
    voornaam: str
    achternaam: str
    telefoonnummer: str


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int

    class Config:
        orm_mode = True


class RechargeBase(BaseModel):
    datum: datetime = None
    startuur: datetime = None
    einduur: datetime = None
    tijd: int
    elektriciteit: float
    prijs: float
    car_id: int


class RechargeCreate(RechargeBase):
    pass


class Recharge(RechargeBase):
    id: int

    class Config:
        orm_mode = True

