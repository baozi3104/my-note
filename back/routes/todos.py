from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import sessionlocal

router = APIRouter()


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(title=todo.title, parent_id=todo.parent_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.get("/", response_model=List[schemas.TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).filter(models.Todo.is_deleted == False).all()


@router.patch("/{todo_id}/toggle", response_model=schemas.TodoResponse)
def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="没有找到这个任务")
    db_todo.is_completed = not db_todo.is_completed
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.patch("/{todo_id}/delete", response_model=schemas.TodoResponse)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="没有找到这个任务")
    db_todo.is_deleted = True
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.patch("/{todo_id}/tomato", response_model=schemas.TodoResponse)
def add_tomato(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="没有找到这个任务")
    db_todo.tomato_count += 1
    db.commit()
    db.refresh(db_todo)
    return db_todo
