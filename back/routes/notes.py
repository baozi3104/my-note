from fastapi import APIRouter, Depends, HTTPException
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
    return db.query(models.Note).filter(models.Note.is_deleted == False).all()


@router.patch("/{note_id}/delete", response_model=schemas.NoteResponse)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="没有找到这个笔记")
    db_note.is_deleted = True
    db.commit()
    db.refresh(db_note)
    return db_note
