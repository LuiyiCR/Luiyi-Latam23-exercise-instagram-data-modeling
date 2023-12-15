import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    full_name = Column(String(300), nullable=False)
    address = Column(String(300), nullable=False)
    post_code = Column(String(250), nullable=False)
    street_name = Column(String(250))
    country_name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    profile_picture_url = Column(String(300))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    caption = Column(String(500))
    image_url = Column(String(500))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    text = Column(String(500), nullable=False)
    user = relationship(User)

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'), unique=True)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
