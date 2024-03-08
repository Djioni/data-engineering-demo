import csv
from pathlib import Path

def extract_users():
    file_path = Path(__file__).parent.parent / "data" / "users.csv"
    with file_path.open('r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row

def extract_orders():
    file_path = Path(__file__).parent.parent / "data" / "orders.csv"
    with file_path.open('r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row