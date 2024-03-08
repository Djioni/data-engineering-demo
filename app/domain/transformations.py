def transform_user(user):
    return {
        'id': int(user['id']),
        'first_name': user['first_name'],
        'last_name': user['last_name'],
        'email': user['email'],
        'created_at': user['created_at']
    }

def transform_order(order):
    return {
        'id': int(order['id']),
        'user_id': int(order['user_id']),
        'book_id': int(order['book_id']),
        'order_date': order['order_date'],
        'quantity': int(order['quantity']),
        'total_price': float(order['total_price'])
    }