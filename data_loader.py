import pandas as pd


def load_sales_data(
    rpsale_path='data/EXTR_RPSale.csv',
    resbldg_path='data/EXTR_ResBldg.csv',
):
    """Loads the King County sales data into a Pandas DF."""
    sales_df = pd.read_csv(rpsale_path, low_memory=False)
    sales_df = sales_df[['Major', 'Minor', 'DocumentDate', 'SalePrice']]
    bldg_df = pd.read_csv(resbldg_path, low_memory=False)
    sales_df['Major'] = pd.to_numeric(sales_df['Major'], errors='coerce')
    sales_df['Minor'] = pd.to_numeric(sales_df['Minor'], errors='coerce')
    sales_data = pd.merge(sales_df, bldg_df, on=['Major', 'Minor'])
    return sales_data
