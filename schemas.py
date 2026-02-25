from pydantic import BaseModel
from datetime import date

class ObraCreate(BaseModel):
    codigo: str
    nome: str
    responsavel: str
    empresa_contratada: str
    data_inicio: date
    prazo_final: date
    valor_orcado_inicial: float
    status: str

class ObraResponse(ObraCreate):
    id: int
    class Config:
        orm_mode = True
