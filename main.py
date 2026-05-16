from src.data_loader import load_data
from src.data_cleaning import clean_orders,clean_items
from src.data_transform import merge_data
from src.analysis import monthly_revenue,top_cities_by_revenue,top_cities_per_month,city_consistency

def run_pipeline():

    orders,items,customers = load_data()

    cleaned_orders = clean_orders(orders)
    cleaned_items = clean_items(items)

    df = merge_data(cleaned_orders,cleaned_items,customers)

    sales_month = monthly_revenue(df)
    sales_city = top_cities_by_revenue(df)
    sales_for_city_month = top_cities_per_month(df)
    city_count = city_consistency(sales_for_city_month) 

    return {
        'sales_monthly':sales_month,
        'sales_Per_city':sales_city,
        'sales_per_city_each_month':sales_for_city_month,
        'city_repeated':city_count

    }



if __name__ == "__main__":

    results = run_pipeline()

    print(f"\nMonthly Revenue:\n {results['sales_monthly']}")
    print(f"\nCity Wise Revenue:\n {results['sales_Per_city']}")
    print(f"\nMonthly Revenue Per City:\n {results['sales_per_city_each_month']}")
    print(f"\nCity Count in Top 3:\n {results['city_repeated']}")






