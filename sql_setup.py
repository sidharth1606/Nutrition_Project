import sqlite3
import pandas as pd

# Load cleaned data
df_obesity = pd.read_csv('obesity_cleaned.csv')
df_malnutrition = pd.read_csv('malnutrition_cleaned.csv')

# Create SQLite database
conn = sqlite3.connect('nutrition_data.db')
cursor = conn.cursor()

# Create obesity table
cursor.execute('''
CREATE TABLE IF NOT EXISTS obesity (
    Region TEXT,
    Gender TEXT,
    Year INTEGER,
    LowerBound REAL,
    UpperBound REAL,
    Mean_Estimate REAL,
    Country TEXT,
    age_group TEXT,
    CI_Width REAL,
    obesity_level TEXT
)
''')

# Create malnutrition table
cursor.execute('''
CREATE TABLE IF NOT EXISTS malnutrition (
    Region TEXT,
    Gender TEXT,
    Year INTEGER,
    LowerBound REAL,
    UpperBound REAL,
    Mean_Estimate REAL,
    Country TEXT,
    age_group TEXT,
    CI_Width REAL,
    malnutrition_level TEXT
)
''')

# Insert data into obesity table
df_obesity.to_sql('obesity', conn, if_exists='replace', index=False)

# Insert data into malnutrition table
df_malnutrition.to_sql('malnutrition', conn, if_exists='replace', index=False)

print("Database created and data inserted successfully.")

# Close connection
conn.close()
