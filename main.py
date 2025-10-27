import pandas as pd
from data_collection import df_obesity, df_malnutrition
from data_cleaning import clean_dataset

# Clean the datasets
df_obesity_cleaned = clean_dataset(df_obesity, 'obesity')
df_malnutrition_cleaned = clean_dataset(df_malnutrition, 'malnutrition')

# Save cleaned data to CSV for later use
df_obesity_cleaned.to_csv('obesity_cleaned.csv', index=False)
df_malnutrition_cleaned.to_csv('malnutrition_cleaned.csv', index=False)

print("Data cleaned and saved.")
print(f"Obesity cleaned shape: {df_obesity_cleaned.shape}")
print(f"Malnutrition cleaned shape: {df_malnutrition_cleaned.shape}")
