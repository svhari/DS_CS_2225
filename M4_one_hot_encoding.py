# M4_one_hot_encoding.py
import pandas as pd

data = pd.DataFrame({"Color": ["Red", "Blue", "Green", "Blue", "Red"]})
print("Original Data:")
print(data)

# One-hot encoding using sklean
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False)
encoded_array = encoder.fit_transform(data[["Color"]])  # Input must be 2D

# Convert to DataFrame
encoded_df = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out())
print("\nOne-Hot Encoded (sklearn):")
print(encoded_df)