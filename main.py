import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Year": [1980, 1985, 1990, 1995, 2000, 2004, 2010, 2014, 2018, 2024],
    "Population": [1000, 1114, 1200, 1350, 1450, 1596, 1700, 1864, 1880, 1900],
    "Habitat_Area_km2": [18000, 20000, 21000, 22000, 22500, 23000, 24500, 26000, 26500, 27000],
    "Threat_Level": [5, 5, 4, 4, 4, 4, 3, 3, 3, 3]  # 5 = הכי מסוכן, 1 = פחות מסוכן
}

df = pd.DataFrame(data)
print(df.head())
print(df.describe())

feature_x = "Habitat_Area_km2"
feature_y = "Population"

df["Population"].hist(rwidth=0.8, color="skyblue")
plt.title("Panda population histogram")
plt.xlabel("population")
plt.ylabel("frequency")
plt.savefig("population_hist.png")
plt.show()

df["Habitat_Area_km2"].hist(rwidth=0.8, color="skyblue")
plt.title("Histogram of habitat area (km2)")
plt.xlabel("habitat area")
plt.ylabel("frequency")
plt.savefig("habitat_hist.png")
plt.show()

plt.scatter(df[feature_x], df[feature_y], alpha=0.7)
plt.xlabel("Habitat area (km2)")
plt.ylabel("population")
plt.title("Scatter graph: habitat area versus panda population")
plt.savefig("scatter.png")
plt.show()

