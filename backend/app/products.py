from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Product

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post("/")
def create_product(name: str, description: str, price: int, db: Session = Depends(get_db)):
    product = Product(name=name, description=description, price=price)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
