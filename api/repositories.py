from sqlalchemy.orm import Session

from models import Alunas

class AlunasRepository:
    @staticmethod
    def find_all(db: Session) -> list[Alunas]:
        return db.query(Alunas).all()

    @staticmethod
    def save(db: Session, alunas: Alunas) -> Alunas:
        if alunas.id:
            db.merge(alunas)
        else:
            db.add(alunas)
        db.commit()
        return alunas

    @staticmethod
    def find_by_id(db: Session, id: int) -> Alunas:
        return db.query(Alunas).filter(Alunas.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Alunas).filter(Alunas.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        alunas = db.query(Alunas).filter(Alunas.id == id).first()
        if alunas is not None:
            db.delete(alunas)
            db.commit()
