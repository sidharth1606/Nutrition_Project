import pandas as pd
import pycountry

# Load the data (assuming data_collection.py has been run and data is available)
# For now, we'll assume df_obesity and df_malnutrition are loaded from data_collection.py
# In a real scenario, you might save and load from CSV or pickle

# Columns to retain
columns_to_keep = ['ParentLocation', 'Dim1', 'TimeDim', 'Low', 'High', 'NumericValue', 'SpatialDim', 'age_group']

# Function to clean dataset
def clean_dataset(df, dataset_type):
    # Keep only required columns
    df = df[columns_to_keep].copy()

    # Rename columns
    df.rename(columns={
        'TimeDim': 'Year',
        'Dim1': 'Gender',
        'NumericValue': 'Mean_Estimate',
        'Low': 'LowerBound',
        'High': 'UpperBound',
        'ParentLocation': 'Region',
        'SpatialDim': 'Country'
    }, inplace=True)

    # Standardize Gender values
    df['Gender'] = df['Gender'].replace({
        'MLE': 'Male',
        'FMLE': 'Female',
        'BTSX': 'Both'
    })

    # Convert country codes to names
    def convert_country_code(code):
        special_cases = {
            'GLOBAL': 'Global',
            'WB_LMI': 'Low & Middle Income',
            'WB_HI': 'High Income',
            'WB_LI': 'Low Income',
            'EMR': 'Eastern Mediterranean Region',
            'EUR': 'Europe',
            'AFR': 'Africa',
            'SEAR': 'South-East Asia Region',
            'WPR': 'Western Pacific Region',
            'AMR': 'Americas Region',
            'WB_UMI': 'Upper Middle Income'
        }
        if code in special_cases:
            return special_cases[code]
        try:
            country = pycountry.countries.get(alpha_3=code)
            return country.name if country else code
        except:
            return code

    df['Country'] = df['Country'].apply(convert_country_code)

    # Create CI_Width
    df['CI_Width'] = df['UpperBound'] - df['LowerBound']

    # Create level columns based on dataset type
    if dataset_type == 'obesity':
        df['obesity_level'] = pd.cut(df['Mean_Estimate'],
                                     bins=[-float('inf'), 25, 29.9, float('inf')],
                                     labels=['Low', 'Moderate', 'High'])
    elif dataset_type == 'malnutrition':
        df['malnutrition_level'] = pd.cut(df['Mean_Estimate'],
                                          bins=[-float('inf'), 10, 19.9, float('inf')],
                                          labels=['Low', 'Moderate', 'High'])

    return df

# Note: In practice, you'd load df_obesity and df_malnutrition here
# For this example, we'll assume they are available
# df_obesity_cleaned = clean_dataset(df_obesity, 'obesity')
# df_malnutrition_cleaned = clean_dataset(df_malnutrition, 'malnutrition')

print("Data cleaning functions defined. Run data_collection.py first, then apply these functions.")
