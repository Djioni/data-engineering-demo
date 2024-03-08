import sys
import os

from app.domain.transformations import transform_user, transform_order


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app=None

def test_transform_user():
    user = {
        'id': '1',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'created_at': '2022-01-01 10:00:00'
    }
    
    transformed_user = transform_user(user)
    
    assert transformed_user == {
        'id': 1,
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'created_at': '2022-01-01 10:00:00'
    }

def test_transform_order():
    order = {
        'id': '1',
        'user_id': '2',
        'book_id': '3',
        'order_date': '2022-01-01 10:00:00',
        'quantity': '1',
        'total_price': '10.99'
    }
    
    transformed_order = transform_order(order)
    
    assert transformed_order == {
        'id': 1,
        'user_id': 2,
        'book_id': 3,
        'order_date': '2022-01-01 10:00:00',
        'quantity': 1,
        'total_price': 10.99
    }