
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Φόρτωση δεδομένων
df = pd.read_csv("synthetic_ecommerce_data.csv")

# Δημιουργία στήλης-στόχου αν δεν υπάρχει
if 'Purchase' not in df.columns:
    df['Purchase'] = (df['Customer_Rating'] >= 3).astype(int)

target = 'Purchase'
X = df.drop(columns=[target])
y = df[target]

# Προετοιμασία μετασχηματιστών
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])

# Δημιουργία pipeline
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', MLPClassifier(random_state=42, max_iter=500))])

# Εκπαίδευση μοντέλου
clf.fit(X, y)

# Αποθήκευση preprocessor και μοντέλου
joblib.dump(clf.named_steps['preprocessor'], 'preprocessor.joblib')
joblib.dump(clf.named_steps['classifier'], 'model.joblib')
