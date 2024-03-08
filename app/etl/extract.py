from app.infrastructure.csv_reader import extract_users, extract_orders

def extract_data():
    users = list(extract_users())
    orders = list(extract_orders())
    return users, orders