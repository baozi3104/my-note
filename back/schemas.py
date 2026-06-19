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
    is_deleted: bool

    class Config:
        from_attributes = True


class TodoCreate(BaseModel):
    title: str
    parent_id: int | None = None


class TodoResponse(BaseModel):
    id: int
    title: str
    is_completed: bool
    created_at: datetime
    is_deleted: bool
    tomato_count: int
    parent_id: int | None = None

    class Config:
        from_attributes = True
