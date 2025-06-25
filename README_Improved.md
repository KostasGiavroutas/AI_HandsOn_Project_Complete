
# Τελική Εργασία: AI - Hands On

## 📌 Τίτλος Project:
**Πρόβλεψη Αγοραστικής Συμπεριφοράς σε Περιβάλλον Ηλεκτρονικού Εμπορίου με Χρήση Μηχανικής Μάθησης**

---

## 🔍 Περιγραφή
Η παρούσα εργασία στοχεύει στην πρόβλεψη του εάν ένας πελάτης θα πραγματοποιήσει αγορά σε ένα e-shop, βάσει χαρακτηριστικών του προϊόντος, του τρόπου πληρωμής, της τιμής, του φύλου του χρήστη, του μεγέθους, των εκπτώσεων κ.λπ.

Αξιοποιήθηκαν αλγόριθμοι Μηχανικής Μάθησης (Machine Learning) και δημιουργήθηκε REST API με χρήση FastAPI, καθώς και containerization με Docker για πλήρη αναπαραγωγιμότητα.

---

## 📁 Δομή Φακέλου
```
AI_HandsOn_Project_Complete/
│
├── main.py                    # API εφαρμογή FastAPI
├── train_model.py            # Εκπαίδευση και αποθήκευση μοντέλου
├── test_api.py               # Έλεγχος endpoint /predict
├── synthetic_ecommerce_data.csv  # Συνθετικό dataset
├── model.joblib              # Αποθηκευμένο ML μοντέλο
├── preprocessor.joblib       # Αποθηκευμένος preprocessor
├── requirements.txt          # Εξαρτήσεις Python
├── Dockerfile                # Containerization
├── final_report.pdf          # Αναλυτική τεχνική αναφορά
└── README.md                 # Τεκμηρίωση έργου (αυτό το αρχείο)
```

---

## ⚙️ Περιβάλλον & Εξαρτήσεις
Το έργο χρησιμοποιεί Python 3.10+ και τις εξής βασικές βιβλιοθήκες:

- `pandas`
- `scikit-learn`
- `joblib`
- `fastapi`
- `uvicorn`
- `requests`

Εγκατάσταση:

```bash
pip install -r requirements.txt
```

---

## 🧠 Μοντέλα που χρησιμοποιήθηκαν

- **Random Forest Classifier** (με χρήση `GridSearchCV`)
- **Logistic Regression** (ως σημείο αναφοράς)

Η Random Forest παρουσίασε **υψηλότερη ακρίβεια** και καλύτερη γενίκευση, γι' αυτό και χρησιμοποιήθηκε στο τελικό API.

---

## 🧪 Αξιολόγηση Μοντέλου
Ο αλγόριθμος εκπαιδεύτηκε και αξιολογήθηκε με τα παρακάτω metrics:

- Accuracy
- Classification Report
- Confusion Matrix
- ROC AUC Score

---

## 🌐 API Endpoint

- **POST /predict**

Αναμένει JSON payload με τα παρακάτω πεδία:

```json
{
  "Price": 49.99,
  "Quantity": 2,
  "Customer_Rating": 4.5,
  "Discount_Applied": 1,
  "Product_Category": "Bottoms",
  "Payment_Method": "Credit Card"
}
```

Ανταποκρίνεται με:

```json
{
  "prediction": 1
}
```

όπου `1` σημαίνει πρόβλεψη αγοράς και `0` σημαίνει όχι.

---

## 🐳 Docker

Το έργο περιλαμβάνει Dockerfile για εύκολη εκτέλεση:

```bash
docker build -t ecommerce-api .
docker run -d -p 8000:8000 ecommerce-api
```

---

## 🧾 Οπτικοποιήσεις & Ανάλυση

Η τεχνική αναφορά περιέχει:

- Διαγράμματα συσχέτισης μεταβλητών
- Στατιστικά περιγραφικά δεδομένων
- Καμπύλες ROC & Confusion Matrix
- Ανάλυση επιδόσεων

---

## ✍️ Συντάκτης
**Γιαβρούτας Κωνσταντίνος**  
Δ.Π.Μ.Σ. «Μαθηματική Προτυποποίηση σε Σύγχρονες Τεχνολογίες και τη Χρηματοοικονομική»  
Εθνικό Μετσόβιο Πολυτεχνείο
