# M4_imputation.py
# 17 Jun 2025
# How to handle missing data

import pandas as pd
import numpy as np

# Generate data
df = pd.DataFrame({'grades': [78, 95, 83, np.nan, 88, 91, np.nan, 76, 82]})

# Replace missing values with mean
df.fillna(df.mean(), inplace=True)
print
print(df)
print