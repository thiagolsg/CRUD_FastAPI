from .model import Alunas
from .repository import AlunasRepository
from .schema import AlunasRequest, AlunasResponse
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from fastapi import APIRouter, status, HTTPException, Response, Depends

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/alunas',
    tags=['alunas'],
    responses={404: {"description": "Not found"}},
)

@router.post("/",
    response_model=AlunasResponse,
    status_code=status.HTTP_201_CREATED
)
def create(request: AlunasRequest, db: Session = Depends(get_db)):
    alunas = AlunasRepository.save(db, Alunas(**request.dict()))
    return AlunasResponse.from_orm(alunas)


# READ ALL
@router.get("/", response_model=list[AlunasResponse])
def find_all(db: Session = Depends(get_db)):
    alunas = AlunasRepository.find_all(db)
    return [AlunasResponse.from_orm(aluna) for aluna in alunas]


# READ BY ID
@router.get("/{id}", response_model=AlunasResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    aluna = AlunasRepository.find_by_id(db, id)
    if not aluna:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="aluna não encontrada"
        )
    return AlunasResponse.from_orm(aluna)

# DELETE BY ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not AlunasRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="aluna não encontrada"
        )
    AlunasRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# UPDATE BY ID
@router.put("/{id}", response_model=AlunasResponse)
def update(id: int, request: AlunasRequest, db: Session = Depends(get_db)):
    if not AlunasRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluna não encontrada"
        )
    aluna = AlunasRepository.save(db, Alunas(id=id, **request.dict()))
    return AlunasResponse.from_orm(aluna)
