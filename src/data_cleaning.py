import pandas as pd

# 🔹 Clean Orders Data
def clean_orders(orders:pd.DataFrame) -> pd.DataFrame:
    """
    Cleans orders dataset:
    - Filters delivered orders
    - Converts timestamp to datetime
    - Creates month column
    """
        
    orders = orders.copy()

    # Filter only delivered orders
    orders = orders[orders['order_status'] == 'delivered']

    # Convert to datetime
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
    orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
    orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
    

    # Create month column
    orders['month'] = orders['order_purchase_timestamp'].dt.to_period('M')    

    return orders


def clean_items(order_items:pd.DataFrame) -> pd.DataFrame:

    items = order_items.copy()

    # Convert to datetime
    items['shipping_limit_date'] = pd.to_datetime(items['shipping_limit_date'])

    # Create revenue column
    items['total_revenue'] = items['price'] + items['freight_value']

    return items
