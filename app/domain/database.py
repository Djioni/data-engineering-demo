import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.domain.models import Base, UserORM, OrderORM
from dotenv import load_dotenv



load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def load_users(db: Session, users: list[dict]):
    for user in users:
        db_user = UserORM(
            id=user['id'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            email=user['email'],
            created_at=user['created_at']
        )
        db.add(db_user)
    db.commit()

def load_orders(db: Session, orders: list[dict]):
    for order in orders:
        db_order = OrderORM(
            id=order['id'],
            user_id=order['user_id'],
            book_id=order['book_id'],
            order_date=order['order_date'],
            quantity=order['quantity'],
            total_price=order['total_price']
        )
        db.add(db_order)
    db.commit()