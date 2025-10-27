import sqlite3
import pandas as pd

conn = sqlite3.connect('nutrition_data.db')

# Obesity Queries (10)
print("=== OBESITY QUERIES ===")

# 1. Top 5 regions with highest average obesity in 2022
query1 = """
SELECT Region, AVG(Mean_Estimate) as avg_obesity
FROM obesity
WHERE Year = 2022
GROUP BY Region
ORDER BY avg_obesity DESC
LIMIT 5
"""
print("1. Top 5 regions with highest average obesity in 2022:")
print(pd.read_sql_query(query1, conn))

# 2. Top 5 countries with highest obesity estimates
query2 = """
SELECT Country, MAX(Mean_Estimate) as max_obesity
FROM obesity
GROUP BY Country
ORDER BY max_obesity DESC
LIMIT 5
"""
print("\n2. Top 5 countries with highest obesity estimates:")
print(pd.read_sql_query(query2, conn))

# 3. Obesity trend in India over the years
query3 = """
SELECT Year, Mean_Estimate
FROM obesity
WHERE Country = 'India'
ORDER BY Year
"""
print("\n3. Obesity trend in India over the years:")
print(pd.read_sql_query(query3, conn))

# 4. Average obesity by gender
query4 = """
SELECT Gender, AVG(Mean_Estimate) as avg_obesity
FROM obesity
GROUP BY Gender
"""
print("\n4. Average obesity by gender:")
print(pd.read_sql_query(query4, conn))

# 5. Country count by obesity level and age group
query5 = """
SELECT obesity_level, age_group, COUNT(DISTINCT Country) as country_count
FROM obesity
GROUP BY obesity_level, age_group
ORDER BY obesity_level, age_group
"""
print("\n5. Country count by obesity level and age group:")
print(pd.read_sql_query(query5, conn))

# 6. Top 5 least reliable countries (highest CI_Width) and most consistent
query6a = """
SELECT Country, AVG(CI_Width) as avg_ci
FROM obesity
GROUP BY Country
ORDER BY avg_ci DESC
LIMIT 5
"""
print("\n6a. Top 5 least reliable countries (highest CI_Width):")
print(pd.read_sql_query(query6a, conn))

query6b = """
SELECT Country, AVG(CI_Width) as avg_ci
FROM obesity
GROUP BY Country
ORDER BY avg_ci ASC
LIMIT 5
"""
print("\n6b. Top 5 most consistent countries (lowest CI_Width):")
print(pd.read_sql_query(query6b, conn))

# 7. Average obesity by age group
query7 = """
SELECT age_group, AVG(Mean_Estimate) as avg_obesity
FROM obesity
GROUP BY age_group
"""
print("\n7. Average obesity by age group:")
print(pd.read_sql_query(query7, conn))

# 8. Top 10 countries with consistent low obesity
query8 = """
SELECT Country, AVG(Mean_Estimate) as avg_obesity, AVG(CI_Width) as avg_ci
FROM obesity
GROUP BY Country
HAVING avg_obesity < 10 AND avg_ci < 5
ORDER BY avg_obesity ASC
LIMIT 10
"""
print("\n8. Top 10 countries with consistent low obesity:")
print(pd.read_sql_query(query8, conn))

# 9. Countries where female obesity exceeds male by large margin
query9 = """
SELECT o1.Country, o1.Year, o1.Mean_Estimate as female_obesity, o2.Mean_Estimate as male_obesity,
       (o1.Mean_Estimate - o2.Mean_Estimate) as difference
FROM obesity o1
JOIN obesity o2 ON o1.Country = o2.Country AND o1.Year = o2.Year
WHERE o1.Gender = 'Female' AND o2.Gender = 'Male' AND (o1.Mean_Estimate - o2.Mean_Estimate) > 5
ORDER BY difference DESC
LIMIT 10
"""
print("\n9. Countries where female obesity exceeds male by large margin:")
print(pd.read_sql_query(query9, conn))

# 10. Global average obesity percentage per year
query10 = """
SELECT Year, AVG(Mean_Estimate) as global_avg_obesity
FROM obesity
GROUP BY Year
ORDER BY Year
"""
print("\n10. Global average obesity percentage per year:")
print(pd.read_sql_query(query10, conn))

print("\n=== MALNUTRITION QUERIES ===")

# Malnutrition Queries (10)
# 1. Avg. malnutrition by age group
query_m1 = """
SELECT age_group, AVG(Mean_Estimate) as avg_malnutrition
FROM malnutrition
GROUP BY age_group
"""
print("\n1. Avg. malnutrition by age group:")
print(pd.read_sql_query(query_m1, conn))

# 2. Top 5 countries with highest malnutrition
query_m2 = """
SELECT Country, MAX(Mean_Estimate) as max_malnutrition
FROM malnutrition
GROUP BY Country
ORDER BY max_malnutrition DESC
LIMIT 5
"""
print("\n2. Top 5 countries with highest malnutrition:")
print(pd.read_sql_query(query_m2, conn))

# 3. Malnutrition trend in African region over the years
query_m3 = """
SELECT Year, AVG(Mean_Estimate) as avg_malnutrition
FROM malnutrition
WHERE Region = 'Africa'
GROUP BY Year
ORDER BY Year
"""
print("\n3. Malnutrition trend in African region over the years:")
print(pd.read_sql_query(query_m3, conn))

# 4. Gender-based average malnutrition
query_m4 = """
SELECT Gender, AVG(Mean_Estimate) as avg_malnutrition
FROM malnutrition
GROUP BY Gender
"""
print("\n4. Gender-based average malnutrition:")
print(pd.read_sql_query(query_m4, conn))

# 5. Malnutrition level-wise average CI_Width by age group
query_m5 = """
SELECT malnutrition_level, age_group, AVG(CI_Width) as avg_ci
FROM malnutrition
GROUP BY malnutrition_level, age_group
ORDER BY malnutrition_level, age_group
"""
print("\n5. Malnutrition level-wise average CI_Width by age group:")
print(pd.read_sql_query(query_m5, conn))

# 6. Yearly malnutrition change in specific countries
query_m6 = """
SELECT Country, Year, Mean_Estimate
FROM malnutrition
WHERE Country IN ('India', 'Nigeria', 'Brazil')
ORDER BY Country, Year
"""
print("\n6. Yearly malnutrition change in India, Nigeria, Brazil:")
print(pd.read_sql_query(query_m6, conn))

# 7. Regions with lowest malnutrition averages
query_m7 = """
SELECT Region, AVG(Mean_Estimate) as avg_malnutrition
FROM malnutrition
GROUP BY Region
ORDER BY avg_malnutrition ASC
LIMIT 5
"""
print("\n7. Regions with lowest malnutrition averages:")
print(pd.read_sql_query(query_m7, conn))

# 8. Countries with increasing malnutrition
query_m8 = """
SELECT Country, MIN(Mean_Estimate) as min_mal, MAX(Mean_Estimate) as max_mal,
       (MAX(Mean_Estimate) - MIN(Mean_Estimate)) as increase
FROM malnutrition
GROUP BY Country
HAVING increase > 0
ORDER BY increase DESC
LIMIT 10
"""
print("\n8. Countries with increasing malnutrition:")
print(pd.read_sql_query(query_m8, conn))

# 9. Min/Max malnutrition levels year-wise
query_m9 = """
SELECT Year, MIN(Mean_Estimate) as min_mal, MAX(Mean_Estimate) as max_mal
FROM malnutrition
GROUP BY Year
ORDER BY Year
"""
print("\n9. Min/Max malnutrition levels year-wise:")
print(pd.read_sql_query(query_m9, conn))

# 10. High CI_Width flags for monitoring
query_m10 = """
SELECT Country, Year, CI_Width
FROM malnutrition
WHERE CI_Width > 5
ORDER BY CI_Width DESC
LIMIT 10
"""
print("\n10. High CI_Width flags for monitoring:")
print(pd.read_sql_query(query_m10, conn))

print("\n=== COMBINED QUERIES ===")

# Combined Queries (5)
# 1. Obesity vs malnutrition comparison by country (5 countries)
query_c1 = """
SELECT o.Country, AVG(o.Mean_Estimate) as avg_obesity, AVG(m.Mean_Estimate) as avg_malnutrition
FROM obesity o
JOIN malnutrition m ON o.Country = m.Country
WHERE o.Country IN ('India', 'China', 'United States', 'Brazil', 'Nigeria')
GROUP BY o.Country
"""
print("\n1. Obesity vs malnutrition comparison (5 countries):")
print(pd.read_sql_query(query_c1, conn))

# 2. Gender-based disparity in both obesity and malnutrition
query_c2 = """
SELECT o.Gender, AVG(o.Mean_Estimate) as avg_obesity, AVG(m.Mean_Estimate) as avg_malnutrition
FROM obesity o
JOIN malnutrition m ON o.Gender = m.Gender
GROUP BY o.Gender
"""
print("\n2. Gender-based disparity in obesity and malnutrition:")
print(pd.read_sql_query(query_c2, conn))

# 3. Region-wise avg estimates side-by-side (Africa and America)
query_c3 = """
SELECT o.Region, AVG(o.Mean_Estimate) as avg_obesity, AVG(m.Mean_Estimate) as avg_malnutrition
FROM obesity o
JOIN malnutrition m ON o.Region = m.Region
WHERE o.Region IN ('Africa', 'Americas Region')
GROUP BY o.Region
"""
print("\n3. Region-wise avg estimates (Africa and America):")
print(pd.read_sql_query(query_c3, conn))

# 4. Countries with obesity up & malnutrition down
query_c4 = """
SELECT o.Country,
       (MAX(o.Mean_Estimate) - MIN(o.Mean_Estimate)) as obesity_increase,
       (MAX(m.Mean_Estimate) - MIN(m.Mean_Estimate)) as malnutrition_decrease
FROM obesity o
JOIN malnutrition m ON o.Country = m.Country
GROUP BY o.Country
HAVING obesity_increase > 0 AND malnutrition_decrease < 0
ORDER BY obesity_increase DESC
LIMIT 10
"""
print("\n4. Countries with obesity up & malnutrition down:")
print(pd.read_sql_query(query_c4, conn))

# 5. Age-wise trend analysis
query_c5 = """
SELECT o.age_group, o.Year, AVG(o.Mean_Estimate) as avg_obesity, AVG(m.Mean_Estimate) as avg_malnutrition
FROM obesity o
JOIN malnutrition m ON o.age_group = m.age_group AND o.Year = m.Year
GROUP BY o.age_group, o.Year
ORDER BY o.age_group, o.Year
"""
print("\n5. Age-wise trend analysis:")
print(pd.read_sql_query(query_c5, conn))

conn.close()
