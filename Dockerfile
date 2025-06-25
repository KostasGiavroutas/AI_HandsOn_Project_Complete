# Dockerfile για FastAPI εφαρμογή
FROM python:3.10-slim

# Ορισμός working directory
WORKDIR /app

# Αντιγραφή των απαραίτητων αρχείων
COPY . /app

# Εγκατάσταση απαιτούμενων πακέτων
RUN pip install --no-cache-dir -r requirements.txt

# Άνοιγμα του port 8000
EXPOSE 8000

# Εκκίνηση της εφαρμογής FastAPI με Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]