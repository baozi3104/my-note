# 数据库结构
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import Base
from datetime import datetime

# 1. 记事本数据模型 (相当于在数据库里建一张名为 notes 的表)
class Note(Base):
    __tablename__="notes"
    id= Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True)
    content=Column(String)
    created_at=Column(DateTime,default=datetime.utcnow)

class Todo(Base):
    __tablename__="todos"
    id=Column(Interger,primary_key=True,index=True)
    title=Column(String,index=True)
    is_completed=Column(Boolean,default=False)
    created_at=Column(DateTime,default=datetime.utcnow)
