import pandas as pd

def monthly_revenue(data:pd.DataFrame) -> pd.DataFrame:
    """
    Returns total revenue per month (sorted descending)
    """

    data_for_analysis = data.copy()

    monthly_sales = data_for_analysis.groupby(['month'],as_index=False)['total_revenue'].sum().sort_values(by='total_revenue',ascending=False)

    return monthly_sales
    

def top_cities_by_revenue(data:pd.DataFrame) -> pd.DataFrame:
    """
    Returns total revenue per city (sorted descending)
    """

    df = data.groupby(['customer_city'],as_index=False)['total_revenue'].sum().sort_values(by='total_revenue',ascending=False)

    return df

def top_cities_per_month(df:pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(['month','customer_city'],as_index=False)['total_revenue'].sum().sort_values(by=['month','total_revenue'],ascending=[True,False])
    df = df.groupby(['month']).head(3)

    return df
    
def city_consistency(top_cities_df:pd.DataFrame) -> pd.DataFrame:
    top_cities = top_cities_df.groupby(['customer_city'],as_index=False).agg(city_count=('customer_city','count')).sort_values(by='city_count',ascending=False)

    return top_cities