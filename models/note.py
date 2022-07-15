from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Note(Base):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    user = relationship("User")
    user_id = Column(Integer, ForeignKey("user.id"))
