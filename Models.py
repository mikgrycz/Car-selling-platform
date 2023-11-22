from sqlalchemy import Boolean, Column, Integer, String
from Database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, index=True)
    content = Column(String(100), unique=True, index=True)
    user_id = Column(Integer, index=True)