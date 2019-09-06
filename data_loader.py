import pandas as pd

def load_bldg_df(resbldg_path='data/EXTR_ResBldg.csv'):
    bldg_df = pd.read_csv(resbldg_path, low_memory=False)
    bldg_df['Major'] = bldg_df['Major'].apply(lambda x: f'{x:06d}')
    bldg_df['Minor'] = bldg_df['Minor'].apply(lambda x: f'{x:04d}')
    bldg_df['ParcelID'] = (
        bldg_df['Major'].str.strip() +
        bldg_df['Minor'].str.strip()
    )
    
    return bldg_df

def load_sales_data(
    rpsale_path='data/EXTR_RPSale.csv',
    resbldg_path='data/EXTR_ResBldg.csv',
):
    """Loads the King County sales data into a Pandas DF."""
    sales_df = pd.read_csv(rpsale_path, low_memory=False)
    sales_df = sales_df[['Major', 'Minor', 'DocumentDate', 'SalePrice']]
    bldg_df = load_bldg_df()
    sales_df['Major'] = pd.to_numeric(sales_df['Major'], errors='coerce')
    sales_df['Minor'] = pd.to_numeric(sales_df['Minor'], errors='coerce')
    bldg_df['Major'] = pd.to_numeric(bldg_df['Major'], errors='coerce')
    bldg_df['Minor'] = pd.to_numeric(bldg_df['Minor'], errors='coerce')
    sales_data = pd.merge(sales_df, bldg_df, on=['Major', 'Minor'])
    return sales_data


bldg_df = load_bldg_df()

def get_features(parcel_id: str) -> dict:
    """Returns the features for a specific parcel."""
    parcel_data = bldg_df[bldg_df['ParcelID'] == parcel_id]
    if len(parcel_data) != 0:
        return parcel_data.to_dict(orient='records')[0]
