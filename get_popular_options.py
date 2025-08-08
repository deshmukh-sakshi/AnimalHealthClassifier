import pandas as pd
import json
from collections import Counter

# Load the dataset
df = pd.read_csv('Animal_Health.csv')

# Get most common options for each field
popular_data = {}

# Most common animals (top 10)
animal_counts = df['AnimalName'].value_counts().head(10)
popular_data['animals'] = [{'label': animal, 'count': count} for animal, count in animal_counts.items()]

# Most common symptoms for each category (top 15 each)
for col in ['symptoms1', 'symptoms2', 'symptoms3', 'symptoms4', 'symptoms5']:
    symptom_counts = df[col].value_counts().head(15)
    popular_data[col] = [{'label': symptom, 'count': count} for symptom, count in symptom_counts.items()]

# Save popular options
with open('popular_options.json', 'w') as f:
    json.dump(popular_data, f, indent=2)

print("Popular options generated!")
print(f"Top animals: {[item['label'] for item in popular_data['animals'][:5]]}")
print(f"Top symptoms1: {[item['label'] for item in popular_data['symptoms1'][:5]]}")