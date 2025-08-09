import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    'knee_angle': [160, 150, 170, 120, 110, 140, 125],
    'hip_angle' : [130, 120, 135, 100, 90, 115, 105],
    'movement'  : [45, 50, 60, 30, 20, 35, 25],
    'label'     : [0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)
print("Data ", df)

X = df[['knee_angle', 'hip_angle', 'movement']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)
print("Model training complete.")

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

new_data = [[155, 125, 47.5]]
prediction = model.predict(new_data)
print("New data for prediction:", new_data)

if prediction[0] == 0:
    print("Joint is Normal")
else:
    print("Joint is Abnormal")
    