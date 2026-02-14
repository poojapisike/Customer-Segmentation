import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("superstore.csv", encoding="latin-1")
print(df.head())

customer_features = df.groupby("Customer ID").agg(
    TotalSpend=("Sales", "sum"),
    Frequency=("Order ID", "nunique")
).reset_index()

print(customer_features)

plt.scatter(
    customer_features["Frequency"],
    customer_features["TotalSpend"]
)

plt.xlabel("Purchase Frequency")
plt.ylabel("Total Spend")
plt.title("Customer Segmentation")
plt.show()


