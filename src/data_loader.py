def load_data():
    import pandas as pd

    orders = pd.read_csv('data/olist_orders_dataset.csv')
    items = pd.read_csv('data/olist_order_items_dataset.csv')
    customers = pd.read_csv('data/olist_customers_dataset.csv')

    return orders,items,customers

