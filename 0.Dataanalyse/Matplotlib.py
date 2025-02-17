import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Indlæs data fra CSV-filen
data = pd.read_csv('./Data/MatPlotLib-Data/sales.csv')
print(data.head())

fig, ax = plt.subplots()
ax.plot(data["month_number"], data["total_profit"])
ax.set(xlabel="Month", ylabel="Profit", title="Total profit per month")
ax.grid()

fig, ax = plt.subplots()
ax.plot(data["month_number"], data["facecream"], label="Face cream")
ax.plot(data["month_number"], data["facewash"], label="Face wash")
ax.plot(data["month_number"], data["toothpaste"], label="Toothpaste")
ax.plot(data["month_number"], data["bathingsoap"], label="Bathing soap")
ax.plot(data["month_number"], data["shampoo"], label="Shampoo")
ax.plot(data["month_number"], data["moisturizer"], label="Moisturizer")
ax.set(xlabel="Month", ylabel="Units", title="Sale of products per month")
ax.grid()
ax.legend()

fig, ax = plt.subplots()
ax.pie(
    [
        np.sum(data["facecream"]),
        np.sum(data["facewash"]),
        np.sum(data["toothpaste"]),
        np.sum(data["bathingsoap"]),
        np.sum(data["shampoo"]),
        np.sum(data["moisturizer"])
    ],
    labels=["Face cream", "Face wash", "Toothpaste", "Bathing soap", "Shampoo", "Moisturizer"]
)

fig, ax = plt.subplots()
ax.stackplot(
    data["month_number"], data["facecream"], data["facewash"], data["toothpaste"], data["bathingsoap"], data["shampoo"], data["moisturizer"],
    labels=["Face cream", "Face wash", "Toothpaste", "Bathing soap", "Shampoo", "Moisturizer"]
)
ax.set(xlabel="Month", ylabel="Units", title="Sale of products per month")
ax.legend()

plt.show()

