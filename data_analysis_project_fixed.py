# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset
dataframe = pd.read_csv("Test.csv")

# Display basic info
print(dataframe.head())
print(dataframe.shape)
print(dataframe.columns)

# Step 3: Dataset Info
print("----- Dataset Info -----")
dataframe.info()

print("----- Dataset Describe -----")
print(dataframe.describe())

# Step 4: Missing Values
print("----- Missing Values -----")
print(dataframe.isnull().sum())

# Step 5: Data Cleaning

# Fill missing values
dataframe['Item_Weight'].fillna(dataframe['Item_Weight'].mean(), inplace=True)
dataframe['Outlet_Size'].fillna(dataframe['Outlet_Size'].mode()[0], inplace=True)

# Fix Item_Fat_Content
dataframe['Item_Fat_Content'] = dataframe['Item_Fat_Content'].replace({
    'low fat': 'Low Fat',
    'LF': 'Low Fat',
    'reg': 'Regular'
})

print("----- After Cleaning -----")
print(dataframe.isnull().sum())

# Step 6: Understanding Spread of Data 

# 1. Item MRP Distribution
plt.figure(figsize=(8,5))
sns.histplot(dataframe['Item_MRP'], bins=20, kde=True)
plt.title("Distribution of Item MRP")
plt.xlabel("Item MRP")
plt.ylabel("Frequency")
plt.show()

# 2. Item Visibility Distribution
plt.figure(figsize=(8,5))
sns.histplot(dataframe['Item_Visibility'], bins=20, kde=True)
plt.title("Distribution of Item Visibility")
plt.xlabel("Item Visibility")
plt.ylabel("Frequency")
plt.show()

# 3. Boxplot (MRP vs Outlet Type)
plt.figure(figsize=(8,5))
sns.boxplot(x='Outlet_Type', y='Item_MRP', data=dataframe)
plt.xticks(rotation=45)
plt.title("MRP across Outlet Type")
plt.show()

# Step 7: Univariate Analysis

plt.figure(figsize=(10,5))
sns.countplot(x='Item_Type', data=dataframe)
plt.xticks(rotation=90)
plt.title("Item Type Count")
plt.show()

# Step 8: Categorical Analysis

sns.countplot(x='Item_Fat_Content', data=dataframe)
plt.title("Fat Content Count")
plt.show()



sns.countplot(x='Outlet_Location_Type', data=dataframe)
plt.show()
plt.title("Outlet Location Type Count")

# Step 9: Bivariate Analysis

plt.figure()
sns.scatterplot(x='Item_Visibility', y='Item_MRP', data=dataframe)
plt.title("Visibility vs MRP")
plt.show()

# Step 10: Aggregation

avg_mrp = dataframe.groupby('Item_Type')['Item_MRP'].mean()
avg_mrp.plot(kind='bar')
plt.title("Average MRP by Item Type")
plt.show()

# Step 11: Time Analysis

sns.countplot(x='Outlet_Establishment_Year', data=dataframe)
plt.xticks(rotation=45)
plt.title("Outlet Establishment Year Distribution")
plt.show()

# Step 12: Correlation Heatmap

numeric_data = dataframe.select_dtypes(include=[np.number])
corr = numeric_data.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
