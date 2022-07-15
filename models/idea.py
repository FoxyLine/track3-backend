from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Idea(Base):
    __tablename__ = "idea"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    user = relationship("User")
    comments = relationship("IdeaComment", lazy="selectin")
    user_id = Column(Integer, ForeignKey("user.id"))


class IdeaComment(Base):
    __tablename__ = "ideacomment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    body = Column(String)

    author = relationship("User")
    author_id = Column(Integer, ForeignKey("user.id"))
    idea_id = Column(Integer, ForeignKey("idea.id"))
