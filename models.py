from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from database import Base
from datetime import datetime

#Classes
class User(Base):
    __tablename__ = "users"

    # Columns
    username = Column("username", TEXT, primary_key=True)
    password = Column("password", TEXT, nullable=False)

    # Constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Textbook(Base):
    __tablename__ = "posts"

    title = Column("title", TEXT, nullable=False)
    topic = Column("topic", TEXT, nullable=False)
    isbn = Column("content", INTEGER, nullable=False)
    owner_username = Column("user_id", TEXT, nullable=False)
    id = Column("id", INTEGER, primary_key=True, autoincrement=True)
    course = Column("time", TEXT, nullable=False)


    # Constructor
    def __init__(self, title, topic, isbn, user_id, course):
        self.title = title
        self.topic = topic
        self.isbn=isbn
        self.owner_username = user_id
        self.course = course
