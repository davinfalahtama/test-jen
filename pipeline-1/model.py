import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

csv_path = os.path.join(os.path.dirname(__file__), "data.csv")

# Load dataset
data = pd.read_csv(csv_path)

# Preprocessing
data['jenis_kelamin'] = data['jenis_kelamin'].map({'Pria': 0, 'Wanita': 1})
X = data[['tinggi', 'berat']]
y = data['jenis_kelamin']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Akurasi: {accuracy}')

# Save model
# joblib.dump(model, 'model.pkl')