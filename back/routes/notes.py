from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
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


@router.post("/", response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteBase, db: Session = Depends(get_db)):
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


@router.get("/", response_model=list[schemas.NoteResponse])
def read_notes(db: Session = Depends(get_db)):
    notes = db.query(models.Note).all()
    return notes
