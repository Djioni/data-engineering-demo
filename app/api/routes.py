from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.models import User, Order, UserORM, OrderORM
from app.domain.database import get_db

router = APIRouter()

@router.get("/users", response_model=list[User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserORM).all()
    return users

@router.get("/orders", response_model=list[Order])
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(OrderORM).all()
    return orders