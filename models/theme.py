from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Theme(Base):
    __tablename__ = "theme"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
