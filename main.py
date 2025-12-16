import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Population": [1114, 1596, 1864, 1900], 
    "Habitat_Area_km2": [20000, 23000, 26000, 27000],
    "Threat_Level": [5, 4, 3, 3],  # 5 = הכי מסוכן, 1 = פחות מסוכן
    "Year": [1985, 2004, 2014, 2024]
}

df = pd.DataFrame(data)
print(df.head())
print(df.describe())

feature_x = "Habitat_Area_km2"
feature_y = "Population"

df["Population"].hist()
plt.title("היסטוגרמה של אוכלוסיית פנדה")
plt.xlabel("אוכלוסייה")
plt.ylabel("תדירות")
plt.savefig("population_hist.png")
plt.clf()

df["Habitat_Area_km2"].hist()
plt.title("היסטוגרמה של שטח בית גידול (קמ\"ר)")
plt.xlabel("שטח בית גידול")
plt.ylabel("תדירות")
plt.savefig("habitat_hist.png")
plt.clf()

plt.scatter(df[feature_x], df[feature_y], alpha=0.7)
plt.xlabel("שטח בית גידול (קמ\"ר)")
plt.ylabel("אוכלוסייה")
plt.title("גרף פיזור: שטח בית גידול מול אוכלוסיית פנדה")
plt.savefig("scatter.png")
plt.clf()


