from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Obra(Base):
    __tablename__ = "obras"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True)
    nome = Column(String)
    responsavel = Column(String)
    empresa_contratada = Column(String)
    data_inicio = Column(Date)
    prazo_final = Column(Date)
    valor_orcado_inicial = Column(Float)
    status = Column(String)

    orcamentos = relationship("Orcamento", back_populates="obra")
    compras = relationship("Compra", back_populates="obra")


class Orcamento(Base):
    __tablename__ = "orcamentos"

    id = Column(Integer, primary_key=True)
    obra_id = Column(Integer, ForeignKey("obras.id"))
    tipo = Column(String)
    descricao = Column(String)
    quantidade = Column(Float)
    valor_unitario = Column(Float)
    total = Column(Float)

    obra = relationship("Obra", back_populates="orcamentos")


class Compra(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True)
    obra_id = Column(Integer, ForeignKey("obras.id"))
    fornecedor = Column(String)
    descricao = Column(String)
    classificacao = Column(String)
    valor = Column(Float)
    nf = Column(String)

    obra = relationship("Obra", back_populates="compras")
