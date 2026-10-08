import pandas as pd

data = pd.read_csv("dataset/train_test_network.csv")

print("Number of rows:", len(data))
print("Number of columns:", len(data.columns))

print("\nColumns in the dataset:")
for column in data.columns:
    print(column)

print("\nLabel distribution:")
print(data["label"].value_counts())

print("\nAttack type distribution:")
print(data["type"].value_counts())