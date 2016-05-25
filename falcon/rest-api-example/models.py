import datetime
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LocationHistory(Base):
    __tablename__ = 'location_history'

    id = Column(Integer, primary_key=True, nullable=False)
    latitude = Column('latitude', Float)
    lognitude = Column('lognitude', Float)
    created_at = Column('created_at', DateTime, default=datetime.datetime.now, nullable=False)

    def __repr__(self):
        return "<LocationHistory(id={0}, latitude={1}, lognitude={2}, created_at={3})>".format(
                   self.id, self.latitude, self.lognitude, self.created_at)
