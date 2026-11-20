from fastapi import FastAPI, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Sale

app = FastAPI(title="Sales Analytics API")


@app.get("/")
def home():
    return {"message": "Sales Analytics API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    rows = db.query(func.count(Sale.id)).scalar()
    return {"sales_rows": rows}