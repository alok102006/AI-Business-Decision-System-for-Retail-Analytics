import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Convert date
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

    # Clean numeric columns
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
    df['profit'] = pd.to_numeric(df['profit'], errors='coerce')
    df['discount'] = pd.to_numeric(df['discount'], errors='coerce')

    return df