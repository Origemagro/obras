from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/obras", tags=["Obras"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ObraResponse)
def criar_obra(obra: schemas.ObraCreate, db: Session = Depends(get_db)):
    return crud.criar_obra(db, obra)

@router.get("/")
def listar_obras(db: Session = Depends(get_db)):
    return crud.listar_obras(db)
