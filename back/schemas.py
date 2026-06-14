'''用来规范前端传来的数据pydantic模型'''
from pydantic import BaseModel
from datetime import datetime

# 前端接收
class NoteBase(BaseModel):
    title: str
    content: str

# 前端返回
class NoteResponse(BaseModel):
    id:int
    title:str
    content:str
    created_at:datetime

    class config:
        from_attributes=True

# 任务清单
class TodoCreate(BaseModel):
    title:str
class TodoResponse(BaseModel):
    id:int
    title:str
    is_completed:bool
    created_at:datetime

    class config:
        from_attributes=True