import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "Price": 49.99,
    "Quantity": 2,
    "Customer_Rating": 4.5,
    "Discount_Applied": 1,
    "Product_Category": "Bottoms",
    "Payment_Method": "Credit Card",
    "gender": "female",
    "age_category": "adult",
    "size": "M",
    "Delivery_Time_Days": 3,
    "Previous_Purchases": 5,
    "Category_Tops": 0,
    "Category_Bottoms": 1,
    "Category_Accessories": 0
}

response = requests.post(url, json=data)

print("Response status code:", response.status_code)
print("Response body:", response.json())
