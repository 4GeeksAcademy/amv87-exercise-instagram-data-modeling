import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username =  Column(String(250), nullable=False)
    password =  Column(String(250), nullable=False)
    email =  Column(String(250), nullable=False)
    first_name =  Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    date_of_birth =  Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = "followers"
    id = Column(Integer, primary_key=True)
    followed_user = Column(Integer, ForeignKey('user.id'))
    followed = relationship(User)
    follower_user = Column(Integer, ForeignKey('user.id'))
    follower = relationship(User)

class Following(Base):
    __tablename__ = "following"
    id = Column(Integer, primary_key=True)
    follower_user = Column(Integer, ForeignKey('user.id'))
    follower = relationship(User)
    followed_user = Column(Integer, ForeignKey('user.id'))
    followed = relationship(User)

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    title =  Column(String(250), nullable=False)
    image_url = Column(String(250), nullable=False)
    body =  Column(String(250), nullable=False)
    date =  Column(String(250), nullable=False)

class LikedBy(Base):
    __tablename__ = "liked_by"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    liked_by =  Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    comment_by =  Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    comment =  Column(String(250), nullable=False)

render_er(Base, 'diagram.png')