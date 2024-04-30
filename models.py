from .database import Base 
from sqlalchemy import Column, Integer, String, ForeignKey,JSON
from sqlalchemy.orm import relationship

class Table(Base):
    __tablename__='file_details'
    id=Column(Integer,primary_key=True,index=True)
    file_name=Column(String)
    hash_value=Column(String)
    upload_time=Column(String)
