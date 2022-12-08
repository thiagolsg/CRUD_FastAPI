from pydantic import BaseModel
from typing import Union
class AlunasBase(BaseModel):
    nome: str
    cpf: Union[str, None] = None
    turma: int
    idade: int

class AlunasRequest(AlunasBase):
    ...

class AlunasResponse(AlunasBase):
    cpf: str
    id: int
    class Config:
        orm_mode = True
