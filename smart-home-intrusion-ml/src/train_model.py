import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv("data/events.csv")

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=150, max_depth=8, random_state=42)
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))

joblib.dump(model, "model/intrusion_model.pkl")
print("Model trained and saved.")
