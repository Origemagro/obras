from sqlalchemy.orm import Session
from . import models, schemas

def criar_obra(db: Session, obra: schemas.ObraCreate):
    nova_obra = models.Obra(**obra.dict())
    db.add(nova_obra)
    db.commit()
    db.refresh(nova_obra)
    return nova_obra

def listar_obras(db: Session):
    return db.query(models.Obra).all()
