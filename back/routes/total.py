from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from database import sessionlocal

router = APIRouter()


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/statistic")
def statistic(db: Session = Depends(get_db)):
    total_notes = db.query(models.Note).filter(models.Note.is_deleted == False).count()
    total_todos = db.query(models.Todo).filter(models.Todo.is_deleted == False).count()
    return {
        "message": "统计成功",
        "total_notes": total_notes,
        "total_todos": total_todos,
    }
