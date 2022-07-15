from datetime import datetime
from email.policy import default
from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class PostTheme(Base):
    __tablename__ = "posttheme"

    post_id = Column(Integer, ForeignKey("post.id"), primary_key=True)
    theme_id = Column(Integer, ForeignKey("theme.id"), primary_key=True)


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    body = Column(String)
    created = Column(DateTime, default=lambda: datetime.now())

    author = relationship("User", lazy='selectin')
    themes = relationship("Theme", secondary="posttheme", lazy='selectin')
    user_id = Column(Integer, ForeignKey("user.id"))
