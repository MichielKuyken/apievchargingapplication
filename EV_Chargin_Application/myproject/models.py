from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    nummerplaat = Column(String, unique=True, index=True)
    auto = Column(String)
    voornaam = Column(String)
    achternaam = Column(String)
    telefoonnummer = Column(String)

    recharges = relationship("Recharge", back_populates="cars")


class Recharge(Base):
    __tablename__ = "recharges"
    id = Column(Integer, primary_key=True, index=True)
    datum = Column(Date)
    startuur = Column(DateTime)
    einduur = Column(DateTime)
    tijd = Column(Integer)
    elektriciteit = Column(Boolean)
    prijs = Column(Boolean)
    car_id = Column(Integer, ForeignKey("cars.id"))

    cars = relationship("Car", back_populates="recharges")
