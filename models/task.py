from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    deadline = Column(DateTime)
    status = Column(String(50))

    user = relationship("User")
    user_id = Column(Integer, ForeignKey("user.id"))

    aim = relationship("Aim", lazy="selectin")
    aim_id = Column(Integer, ForeignKey("aim.id"))
