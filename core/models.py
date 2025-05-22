from sqlalchemy import Column, Integer, String, Boolean, Time, Date
from core.db import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    title = Column(String, nullable=False)
    days = Column(String)  # example: "mon,tue,fri"
    time = Column(Time)
    is_done = Column(Boolean, default=False)
    date = Column(Date)
