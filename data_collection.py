import requests
import pandas as pd

# URLs for the datasets
urls = {
    'obesity_adult': 'https://ghoapi.azureedge.net/api/NCD_BMI_30C',
    'obesity_child': 'https://ghoapi.azureedge.net/api/NCD_BMI_PLUS2C',
    'malnutrition_adult': 'https://ghoapi.azureedge.net/api/NCD_BMI_18C',
    'malnutrition_child': 'https://ghoapi.azureedge.net/api/NCD_BMI_MINUS2C'
}

def load_dataset(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['value'])
        return df
    else:
        print(f"Failed to load data from {url}")
        return pd.DataFrame()

# Load all datasets
df_obesity_adult = load_dataset(urls['obesity_adult'])
df_obesity_child = load_dataset(urls['obesity_child'])
df_malnutrition_adult = load_dataset(urls['malnutrition_adult'])
df_malnutrition_child = load_dataset(urls['malnutrition_child'])

# Add age_group column
df_obesity_adult['age_group'] = 'Adult'
df_obesity_child['age_group'] = 'Child/Adolescent'
df_malnutrition_adult['age_group'] = 'Adult'
df_malnutrition_child['age_group'] = 'Child/Adolescent'

# Combine obesity datasets
df_obesity = pd.concat([df_obesity_adult, df_obesity_child], ignore_index=True)

# Combine malnutrition datasets
df_malnutrition = pd.concat([df_malnutrition_adult, df_malnutrition_child], ignore_index=True)

# Filter for years 2012 to 2022
df_obesity = df_obesity[df_obesity['TimeDim'].between(2012, 2022)]
df_malnutrition = df_malnutrition[df_malnutrition['TimeDim'].between(2012, 2022)]

print("Data collection completed.")
print(f"Obesity data shape: {df_obesity.shape}")
print(f"Malnutrition data shape: {df_malnutrition.shape}")
