from sqlalchemy import Column, Integer, String

from database import Base

class Alunas(Base):
    __tablename__ = "alunas"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(100), nullable=False)
    cpf: str = Column(String(255), nullable=False)
    turma: int = Column(Integer, nullable=False)
    idade: int = Column(Integer, nullable=False)
