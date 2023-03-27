from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

from db import engine

Base = declarative_base()

# class Author(Base):
#     __tablename__="app_mysite_author"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     fullname = Column(String(250), nullable=False, unique=True)
#     born_date = Column(Date, primary_key=True, nullable=False)
#     born_location = Column(String(250), nullable=False, unique=True)
#     description = Column(Text, nullable=False, unique=True)
#     user_id = Column(Integer)


# class Quote(Base):
#     __tablename__="app_mysite_quote"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     quote = Column(String(1000), nullable=False, unique=True)
#     tags = Column(ARRAY(String), nullable=True, unique=False)
#     author_id = Column(Integer, ForeignKey("app_mysite_author.id", ondelete="CASCADE"), unique=False)

#     quote_rel = relationship("Author", backref="app_mysite_quote")

class Author(Base):
    __tablename__ = 'app_mysite_author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(250), nullable=False)
    born_date = Column(String(20))
    born_location = Column(String(250))
    description = Column(Text)
    user_id = Column(Integer)

class Quote(Base):
    __tablename__ = 'app_mysite_quote'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tags = Column(ARRAY(Text))
    author_id = Column(Integer, ForeignKey('app_mysite_author.id', ondelete='CASCADE') )
    quote = Column(Text)
    quote_rel = relationship('Author', backref='app_mysite_quote')
    
if __name__ == '__main__':    
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine    
