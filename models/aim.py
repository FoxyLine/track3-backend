from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Aim(Base):
    __tablename__ = "aim"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    deadline = Column(DateTime)

    user = relationship("User")
    tasks = relationship("Task")
    user_id = Column(Integer, ForeignKey("user.id"))
