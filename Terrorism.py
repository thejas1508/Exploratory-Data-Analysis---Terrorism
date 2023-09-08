import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('globalterrorismdb_0718dist.csv', encoding='ISO-8859-1')

print(data.info())
print(data.head())
print(data.describe())

plt.figure(figsize=(12, 5))
sns.countplot(x='attacktype1_txt', data=data, order=data['attacktype1_txt'].value_counts().index)
plt.xticks(rotation=80)
plt.title('Distribution of Types oF Various ATTACKS')
plt.show()

# Number of attacks over the years
plt.figure(figsize=(12, 5))
sns.countplot(x='iyear', data=data, palette='viridis')
plt.xticks(rotation=80)
plt.title('Number of ATTACKS Over the Past Yrs')
plt.show()

# Distribution of terrorist groups
plt.figure(figsize=(12, 6))
sns.barplot(y=data['gname'].value_counts()[:10].index, x=data['gname'].value_counts()[:10].values, orient='h', palette='viridis')
plt.title('TOP 10 TERRORIST GROUPS In Specified Period')
plt.show()

# Heatmap of correlations
corr_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
