import pandas as pd

def build_features():
    """Build features from raw data."""
    data = pd.read_csv('data/raw/data.csv')
    # No feature engineering for now
    data.to_csv('data/processed/data.csv', index=False)

if __name__ == '__main__':
    build_features()
