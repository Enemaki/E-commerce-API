
````markdown
# 🛒 E-Commerce API

A simple yet robust API built with Django to manage **products**, **orders**, and **authentication**. This project is designed to help developers understand and apply REST API concepts using Django and Django REST Framework.

---

## 📦 Overview

- **API Version**: 1.0.0  
- **Purpose**: Manage products and orders with secure JWT-based authentication.  
- **Framework**: Django + DRF  
- **Auth Methods**: JWT & Cookie Authentication

---

## 🔐 Authentication

### Obtain JWT Token

**POST** `/api/token/`

> Submit valid credentials to get an access and refresh token pair.

```json
{
  "username": "your_username",
  "password": "your_password"
}
````

**Response:**

```json
{
  "access": "jwt-access-token",
  "refresh": "jwt-refresh-token"
}
```

### Refresh JWT Token

**POST** `/api/token/refresh/`

```json
{
  "refresh": "your_refresh_token"
}
```

**Response:**

```json
{
  "access": "new-access-token"
}
```

---

## 🛍️ Product Endpoints

### List Products

**GET** `/products/`
**Auth:** Required

### Create Product

**POST** `/products/`
**Auth:** Required

```json
{
  "name": "Wireless Mouse",
  "description": "Ergonomic and responsive",
  "price": "29.99",
  "stock": 150
}
```

### Retrieve Product

**GET** `/products/{product_id}/`
**Auth:** Required

### Update Product

**PUT** `/products/{product_id}/`
**PATCH** `/products/{product_id}/`
**Auth:** Required

### Delete Product

**DELETE** `/products/{product_id}/`
**Auth:** Required

### Get Product Info

**GET** `/products/info/`
**Auth:** Required

---

## 📦 Order Endpoints

### List All Orders

**GET** `/orders/`
**Auth:** Required

### List Current User's Orders

**GET** `/user-orders/`
**Auth:** Required

---

## 🧱 Schemas

### Product

```json
{
  "name": "Laptop Stand",
  "description": "Adjustable aluminum laptop stand",
  "price": "49.99",
  "stock": 40
}
```

### Order

```json
{
  "order_id": "uuid",
  "created_at": "2025-06-24T10:00:00Z",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  },
  "status": "Pending",
  "items": [
    {
      "quantity": 2,
      "product_name": "Wireless Mouse",
      "product_price": "29.99",
      "item_subtotal": "59.98"
    }
  ],
  "total_price": "59.98"
}
```

---

## 🔐 Security Schemes

* **JWT Auth:** Bearer tokens in `Authorization` header.
* **Cookie Auth:** Session-based (for web clients).

```http
Authorization: Bearer <access_token>
```

---

## 🚀 Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/ecommerce-api.git
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the server:

   ```bash
   python manage.py runserver
   ```

---

## 🧪 Testing the API

You can test this API using:

* [Postman](https://www.postman.com/)
* [Insomnia](https://insomnia.rest/)
* `curl` or `httpie` via terminal

---

## 📄 License

This project is licensed under the **MIT License**.
Feel free to use, learn from, or contribute to it.

---


