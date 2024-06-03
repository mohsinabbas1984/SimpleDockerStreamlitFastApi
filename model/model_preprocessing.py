import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)


joblib.dump(model, r'C:\Users\IRFAN\SimpleDockerStreamlitFastApi-main\app\model\model.joblib')

