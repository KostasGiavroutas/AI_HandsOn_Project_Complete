
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.ensemble import RandomForestClassifier

# Load data and model
df = pd.read_csv("synthetic_ecommerce_data.csv")
model = joblib.load("model.joblib")
preprocessor = joblib.load("preprocessor.joblib")

# Preprocess data
X = df.drop("Purchase", axis=1)
y = df["Purchase"]
X_transformed = preprocessor.transform(X)

# Predictions
y_pred = model.predict(X_transformed)
y_proba = model.predict_proba(X_transformed)[:, 1]

# Classification report
report = classification_report(y, y_pred)
with open("classification_report.txt", "w") as f:
    f.write(report)

# Confusion matrix
conf_matrix = confusion_matrix(y, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("confusion_matrix.png")
plt.close()

# ROC curve
fpr, tpr, _ = roc_curve(y, y_proba)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0, 1], [0, 1], "k--")
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.savefig("roc_curve.png")
plt.close()

# Feature importances
if hasattr(model, "feature_importances_"):
    importances = model.feature_importances_
    feature_names = preprocessor.get_feature_names_out()
    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Importance", y="Feature", data=importance_df)
    plt.title("Feature Importances")
    plt.tight_layout()
    plt.savefig("feature_importance.png")
    plt.close()

# Distributions
for col in ["Purchase", "Product_Category", "Payment_Method", "gender", "size", "age_category"]:
    plt.figure(figsize=(6, 4))
    df[col].value_counts().plot(kind="bar")
    plt.title(f"Κατανομή {col}")
    plt.xlabel(col)
    plt.ylabel("Συχνότητα")
    plt.tight_layout()
    plt.savefig(f"katanomi_{col}.png")
    plt.close()
