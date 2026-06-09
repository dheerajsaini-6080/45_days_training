import matplotlib.pyplot as plt
import seaborn as sns


# Histogram
plt.hist(merged["revenue"])
plt.title("Revenue Distribution")
plt.show()

# Scatter Plot
plt.scatter(
    merged["quantity"],
    merged["revenue"]
)
plt.title("Quantity vs Revenue")
plt.show()

# Bar Chart
merged.groupby(
    "category"
)["revenue"].sum().plot(kind="bar")

plt.title("Revenue by Category")
plt.show()

# Line Chart
monthly = merged.groupby(
    "month"
)["revenue"].sum()

monthly.plot(kind="line")
plt.title("Monthly Revenue")
plt.show()

# Box Plot
sns.boxplot(
    x="category",
    y="revenue",
    data=merged
)
plt.show()

# Heatmap
sns.heatmap(
    pivot1,
    annot=True
)
plt.show()
