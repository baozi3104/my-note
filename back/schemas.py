from pydantic import BaseModel
from datetime import datetime


class NoteBase(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class TodoCreate(BaseModel):
    title: str


class TodoResponse(BaseModel):
    id: int
    title: str
    is_completed: bool
    created_at: datetime

    class Config:
        from_attributes = True
