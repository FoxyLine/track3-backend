from database import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Memory(Base):
    __tablename__ = "memory"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    user = relationship("User")
    user_id = Column(Integer, ForeignKey("user.id"))

    # aim = relationship("Aim", lazy="selectin")
    aim_id = Column(Integer, ForeignKey("aim.id"))

    pins = relationship("Pin", lazy="selectin")


class Pin(Base):
    __tablename__ = "pin"
    id = Column(Integer, primary_key=True, autoincrement=True)    
    name = Column(String(255))
    image = Column(String)

    x = Column(Float)
    y = Column(Float)
    memory_id = Column(Integer, ForeignKey("memory.id"))