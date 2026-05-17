from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta

app = FastAPI()

security = HTTPBearer()

fake_token = "token-123"
expenses = []

class LoginRequest(BaseModel):
    username: str
    password: str

class Expense(BaseModel):
    amount: float
    category: str

@app.post("/login")
def login(data: LoginRequest):
    if data.username == "Admin" and data.password == "password":
        return {"token": fake_token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/expenses")
def create_expense(
    expense: Expense,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    if token != fake_token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    if expense.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    expenses.append(expense)

    return {
        "message": "Expense added",
        "amount": expense.amount,
        "category": expense.category
    }

@app.get("/expenses")
def get_expenses(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    if token != fake_token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return expenses