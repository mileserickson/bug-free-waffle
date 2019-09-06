from data_loader import load_sales_data

MEAN_PRICE = 320124


def predict_sale_price(parcel_id: str, MEAN_PRICE=MEAN_PRICE) -> int:
    """Predicts the sale price for a given parcel."""
    return MEAN_PRICE