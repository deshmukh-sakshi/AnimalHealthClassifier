import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
import json

# Load and encode the data the same way as training
df = pd.read_csv('Animal_Health.csv')
df['Dangerous'].fillna(df['Dangerous'].mode()[0], inplace=True)

# Create encoders for each column (same as training process)
encoders = {}
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Generate form data
form_data = {}

# Get all unique values for each feature
for col in ['AnimalName', 'symptoms1', 'symptoms2', 'symptoms3', 'symptoms4', 'symptoms5']:
    options = []
    for encoded_value, original_label in enumerate(encoders[col].classes_):
        options.append({
            'value': encoded_value,
            'label': original_label
        })
    form_data[col] = options

# Save form data as JSON for use in Flask app
with open('form_data.json', 'w') as f:
    json.dump(form_data, f, indent=2)

print("Form data generated successfully!")
print(f"AnimalName options: {len(form_data['AnimalName'])}")
print(f"symptoms1 options: {len(form_data['symptoms1'])}")
print(f"symptoms2 options: {len(form_data['symptoms2'])}")
print(f"symptoms3 options: {len(form_data['symptoms3'])}")
print(f"symptoms4 options: {len(form_data['symptoms4'])}")
print(f"symptoms5 options: {len(form_data['symptoms5'])}")

# Show first few options for each
print("\nSample options:")
for col in form_data:
    print(f"\n{col} (first 5):")
    for option in form_data[col][:5]:
        print(f"  {option['value']}: {option['label']}")