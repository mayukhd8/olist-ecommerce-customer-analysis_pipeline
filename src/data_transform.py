import pandas as pd

def merge_data(orders:pd.DataFrame,items:pd.DataFrame,customers:pd.DataFrame) -> pd.DataFrame:
    
    order_items = pd.merge(orders,items,on='order_id',validate='one_to_many')
    dataset = pd.merge(order_items,customers,on='customer_id',validate='many_to_one')

    return dataset