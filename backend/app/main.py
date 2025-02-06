from fastapi import FastAPI
from app.db import engine, Base
from app.api import products

app = FastAPI()

# Créer mes tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API e-commerce"}

# Inclure les routes produits
app.include_router(products.router, prefix="/products", tags=["products"])