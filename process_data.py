import pandas as pd
import glob

# Load all 3 CSV files, manually set column names since there's no header
files = glob.glob("data/*.csv")
df = pd.concat([
    pd.read_csv(f, header=None, names=["product", "price", "quantity", "date", "region"])
    for f in files
], ignore_index=True)

# Keep only pink morsels
df = df[df["product"] == "pink morsel"]

# Strip the $ from price and convert to float
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
df["quantity"] = df["quantity"].astype(int)

# Calculate sales
df["sales"] = df["quantity"] * df["price"]

# Keep only the columns we need
df = df[["sales", "date", "region"]]

# Save to output file
df.to_csv("data/output.csv", index=False)

print("Done! output.csv created.")