from sqlalchemy import Column, Integer, String, Boolean
from database.session import Base

class Task(Base):
    __tablename__ = "tasks"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=True)
    completed   = Column(Boolean, default=False)
