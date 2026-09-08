
# pyrefly: ignore [missing-import]
from sqlalchemy import Column , Integer ,String,Boolean
from database.session import Base

class Task(base):
    __tablename__ = "task"

    id = Column(Integer,primarykey=True)
    title = Column(String(50),unique=true,index=True)
    description = Column(String)
    completed = Column(Boolean,default=False)
