import pandas as pd
from analysis_packages.data import get_data

def test_data():
    df = get_data()
    assert all(df.columns == ['Total', 'West', 'East'])
    assert isinstance(df.index, pd.DatetimeIndex)
