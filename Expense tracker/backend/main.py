from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal, Base
from stats_routes import router as stats_router
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API",
    description="A comprehensive expense tracking API with chart data endpoints",
    version="1.0.0"
)

# CORS Configuration - Allow frontend to connect
origins = [
    "http://localhost:3000",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:8080",
    "file://",  # Allow local HTML files
    "*"  # Allow all origins in development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include stats router
app.include_router(stats_router)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root
@app.get("/")
def home():
    return {
        "message": "Expense Tracker API running",
        "version": "1.0.0",
        "status": "healthy",
        "endpoints": {
            "expenses": "/expenses",
            "category_summary": "/summary/category",
            "monthly_summary": "/summary/monthly",
            "docs": "/docs"
        }
    }

# Add expense
@app.post("/expenses", response_model=schemas.ExpenseResponse)
def add_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)

# Get all expenses
@app.get("/expenses")
def get_all_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)

# Delete expense
@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int, db: Session = Depends(get_db)):
    return crud.delete_expense(db, expense_id)

# Category summary for Pie chart
@app.get("/summary/category")
def category_summary(db: Session = Depends(get_db)):
    data = crud.get_category_summary(db)
    return [{"category": c, "total": t} for c, t in data]

# Monthly summary for Bar chart
@app.get("/summary/monthly")
def monthly_summary(db: Session = Depends(get_db)):
    data = crud.get_monthly_summary(db)
    return [{"month": m, "total": t} for m, t in data]
