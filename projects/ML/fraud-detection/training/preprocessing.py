import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('../data/creditcard.csv')

X = df.drop('Class', axis=1)
y = df['Class']
print("X shape:", X.shape)
print("y shape:", y.shape, end="\n\n")

# Stratified splitting preserves the original class distribution in every split.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape, end="\n\n")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Scaled shapes:")
print(X_train_scaled.shape, X_test_scaled.shape, end="\n\n")

# Handle imbalance
from sklearn.utils.class_weight import compute_class_weight
import numpy as np

weights = compute_class_weight(class_weight="balanced", classes=np.unique(y_train), y=y_train)
class_weights = {0: weights[0], 1: weights[1]}

# Save processed data
import joblib

joblib.dump(X_train_scaled, "../data/X_train.pkl")
joblib.dump(X_test_scaled, "../data/X_test.pkl")
joblib.dump(y_train, "../data/y_train.pkl")
joblib.dump(y_test, "../data/y_test.pkl")
joblib.dump(scaler, "../models/scaler.pkl")
