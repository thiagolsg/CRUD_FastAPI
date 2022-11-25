from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Alunas
from database import engine, Base, get_db
from repositories import AlunasRepository
from schemas import AlunasRequest, AlunasResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CREATE
@app.post("/api/alunas", response_model=AlunasResponse, status_code=status.HTTP_201_CREATED)
def create(request: AlunasRequest, db: Session = Depends(get_db)):
    alunas = AlunasRepository.save(db, Alunas(**request.dict()))
    return AlunasResponse.from_orm(alunas)


# READ ALL
@app.get("/api/alunas", response_model=list[AlunasResponse])
def find_all(db: Session = Depends(get_db)):
    alunas = AlunasRepository.find_all(db)
    return [AlunasResponse.from_orm(aluna) for aluna in alunas]


# READ BY ID
@app.get("/api/alunas/{id}", response_model=AlunasResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    aluna = AlunasRepository.find_by_id(db, id)
    if not aluna:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="aluna não encontrada"
        )
    return AlunasResponse.from_orm(aluna)

# DELETE BY ID
@app.delete("/api/alunas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not AlunasRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="aluna não encontrada"
        )
    AlunasRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# UPDATE BY ID
@app.put("/api/alunas/{id}", response_model=AlunasResponse)
def update(id: int, request: AlunasRequest, db: Session = Depends(get_db)):
    if not AlunasRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluna não encontrada"
        )
    aluna = AlunasRepository.save(db, Alunas(id=id, **request.dict()))
    return AlunasResponse.from_orm(aluna)
