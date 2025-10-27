import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df_obesity = pd.read_csv('obesity_cleaned.csv')
df_malnutrition = pd.read_csv('malnutrition_cleaned.csv')

# Basic EDA
print("Obesity Data Info:")
print(df_obesity.info())
print("\nMalnutrition Data Info:")
print(df_malnutrition.info())

print("\nObesity Data Description:")
print(df_obesity.describe())

print("\nMalnutrition Data Description:")
print(df_malnutrition.describe())

# Check for missing values
print("\nMissing values in Obesity data:")
print(df_obesity.isnull().sum())

print("\nMissing values in Malnutrition data:")
print(df_malnutrition.isnull().sum())

# Visualizations
plt.figure(figsize=(12, 8))

# 1. Distribution of Mean_Estimate
plt.subplot(2, 2, 1)
sns.histplot(df_obesity['Mean_Estimate'], kde=True)
plt.title('Distribution of Obesity Mean Estimates')

plt.subplot(2, 2, 2)
sns.histplot(df_malnutrition['Mean_Estimate'], kde=True)
plt.title('Distribution of Malnutrition Mean Estimates')

# 2. Trends over time (Global average)
obesity_yearly = df_obesity.groupby('Year')['Mean_Estimate'].mean()
malnutrition_yearly = df_malnutrition.groupby('Year')['Mean_Estimate'].mean()

plt.subplot(2, 2, 3)
obesity_yearly.plot()
plt.title('Global Obesity Trend Over Time')
plt.ylabel('Mean Estimate')

plt.subplot(2, 2, 4)
malnutrition_yearly.plot()
plt.title('Global Malnutrition Trend Over Time')
plt.ylabel('Mean Estimate')

plt.tight_layout()
plt.savefig('eda_visualizations.png')
plt.show()

# Additional visualizations
# Top 10 countries by obesity in 2022
top_obesity_2022 = df_obesity[df_obesity['Year'] == 2022].nlargest(10, 'Mean_Estimate')
plt.figure(figsize=(10, 6))
sns.barplot(x='Mean_Estimate', y='Country', data=top_obesity_2022)
plt.title('Top 10 Countries by Obesity in 2022')
plt.savefig('top_obesity_countries.png')
plt.show()

# Box plot by region
plt.figure(figsize=(12, 6))
sns.boxplot(x='Region', y='Mean_Estimate', data=df_obesity)
plt.title('Obesity Distribution by Region')
plt.xticks(rotation=45)
plt.savefig('obesity_by_region.png')
plt.show()

print("EDA completed. Visualizations saved.")
