from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, column
from sqlalchemy.orm import relationship

from .constants import DREAMER


class UserFavoriteTheme(Base):
    __tablename__ = "user_favorite_theme"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    theme_id = Column(Integer, ForeignKey("theme.id"), primary_key=True)


class UserFavoriteInspirer(Base):
    __tablename__ = "user_favorite_inspirer"
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    inspirer_id = Column(Integer, ForeignKey("user.id"), primary_key=True)


class User(Base):
    __tablename__ = "user"

    id = Column(
        Integer().with_variant(Integer, "sqlite"), primary_key=True, autoincrement=True
    )
    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))

    role = Column(String(100), default=DREAMER)
    user_themes = relationship(
        "Theme", secondary="user_favorite_theme", lazy="selectin"
    )
    user_inspirer = relationship(
        "User",
        secondary="user_favorite_inspirer",
        lazy="selectin",
        primaryjoin=id == UserFavoriteInspirer.user_id,
        secondaryjoin=id == UserFavoriteInspirer.inspirer_id,
    )
