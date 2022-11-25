from pydantic import BaseModel

class AlunasBase(BaseModel):
    nome: str
    cpf: str
    turma: int
    idade: int

class AlunasRequest(AlunasBase):
    ...

class AlunasResponse(AlunasBase):
    id: int

    class Config:
        orm_mode = True
