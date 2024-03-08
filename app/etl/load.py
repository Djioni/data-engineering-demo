from app.domain.database import load_users, load_orders, get_db

def load_data(transformed_data):
    users, orders = transformed_data
    db = next(get_db())
    load_users(db, users)
    load_orders(db, orders)