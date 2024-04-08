from sqlalchemy import create_engine, ARRAY, String,ForeignKey,Date, DateTime,LargeBinary,Integer,Column, Text, JSON, UUID, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func 
from datetime import datetime

Base = declarative_base()

class DaftarFR(Base):
    __tablename__ = 'DaftarDeteksiAPD'
    id = Column(Integer,autoincrement=True, primary_key=True)
    image_captured = Column(LargeBinary)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


