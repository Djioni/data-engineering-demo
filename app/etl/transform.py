from app.domain.transformations import transform_user, transform_order

def transform_data(extracted_data):
    users, orders = extracted_data
    transformed_users = [transform_user(user) for user in users]
    transformed_orders = [transform_order(order) for order in orders]
    return transformed_users, transformed_orders