import pandas as pd
import numpy as np
from analysis_packages.data import get_data

def test_data():
    df = get_data()
    assert all(df.columns == ['Total', 'West', 'East'])
    assert isinstance(df.index, pd.DatetimeIndex)
    assert len(np.unique(df.index.time) == 24)
