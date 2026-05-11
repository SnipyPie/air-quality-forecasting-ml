from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PollutionData(Base):
    __tablename__ = "pollution_data"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    lat = Column(Float)
    lon = Column(Float)

    aqi = Column(Integer)
    pm2_5 = Column(Float)
    pm10 = Column(Float)
    no2 = Column(Float)
    so2 = Column(Float)
    o3 = Column(Float)

    timestamp = Column(DateTime, default=datetime.utcnow)