from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/postgres")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    category_id = Column(Integer)
    brand_id = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return [p.__dict__ for p in products]

@app.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product.__dict__

@app.post("/")
def create_product(product: dict, db: Session = Depends(get_db)):
    db_product = Product(**product)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product.__dict__

@app.put("/{product_id}")
def update_product(product_id: int, product: dict, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product.items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product.__dict__

@app.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"detail": "Product deleted successfully"}