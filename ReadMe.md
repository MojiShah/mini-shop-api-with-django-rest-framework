# 🛒 Online Shop REST API

A production-oriented **REST API for an online shop**, built with **Django** and **Django REST Framework (DRF)**.

This project is being developed as a practical learning project with a focus on understanding how to design, implement, test, optimize, and prepare a real-world REST API for production.

---

## 🚀 Tech Stack

* Python
* Django
* Django REST Framework
* JWT Authentication
* PostgreSQL
* Pillow
* django-filter
* OpenAPI / Swagger
* Docker
* Redis

> Some technologies will be introduced gradually as the project evolves.

---

## 📌 Project Goals

The main goal of this project is to build a complete and maintainable REST API for an online shop while learning the concepts behind each layer of a real DRF application.

The project covers:

* REST API design
* APIView and Class-Based Views
* Serializers
* CRUD operations
* Authentication
* JWT
* Authorization & Permissions
* Object-level permissions
* Product and category relationships
* Reviews
* Favorites
* Cart
* Orders
* File and image uploads
* Filtering
* Searching
* Ordering
* Pagination
* API documentation
* Automated testing
* Query optimization
* Caching
* Throttling
* Security
* Docker
* Production deployment

---

## 📂 Project Structure

```text
shop_api/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   └── tests.py
│
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   └── tests.py
│
├── orders/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   └── tests.py
│
├── favorites/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧩 Main Domain Models

The application is built around the following entities:

```text
User
 │
 ├── Profile
 │
 ├── Favorite
 │
 ├── Review
 │
 └── Order
        │
        └── OrderItem
                │
                └── Product
                       │
                       └── Category
```

Products can also have one or more images.

---

## 🔐 Authentication

Authentication will be implemented using JWT.

The planned authentication flow is:

```text
Register
   ↓
User
   ↓
Login
   ↓
Access Token + Refresh Token
   ↓
Authenticated API Requests
```

Example:

```http
Authorization: Bearer <access_token>
```

Authentication and authorization are treated as separate concepts:

```text
Authentication
    ↓
Who is the user?

Authorization
    ↓
What is the user allowed to do?
```

---

## 🛡️ Permissions

The API will support different levels of access.

For example:

```text
Guest
 └── Can browse products

Authenticated User
 ├── Can manage own cart
 ├── Can create orders
 ├── Can manage own favorites
 └── Can review products

Admin
 ├── Can create products
 ├── Can update products
 ├── Can delete products
 └── Can manage categories
```

Object-level permissions will also be used where necessary.

For example:

```text
User A → Can modify Order A
User A → Cannot modify Order B
```

---

## 📦 Main API Endpoints

### Authentication

```text
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/token/refresh/
GET  /api/auth/me/
POST /api/auth/change-password/
```

### Categories

```text
GET    /api/categories/
POST   /api/categories/

GET    /api/categories/<id>/
PATCH  /api/categories/<id>/
DELETE /api/categories/<id>/
```

### Products

```text
GET    /api/products/
POST   /api/products/

GET    /api/products/<id>/
PATCH  /api/products/<id>/
DELETE /api/products/<id>/
```

### Reviews

```text
GET  /api/products/<id>/reviews/
POST /api/products/<id>/reviews/
```

### Favorites

```text
GET    /api/favorites/
POST   /api/favorites/
DELETE /api/favorites/<id>/
```

### Cart

```text
GET    /api/cart/
POST   /api/cart/items/
PATCH  /api/cart/items/<id>/
DELETE /api/cart/items/<id>/
```

### Orders

```text
GET  /api/orders/
POST /api/orders/

GET  /api/orders/<id>/
```

> Endpoints may change as the project architecture evolves.

---

## 🔎 Filtering, Searching & Ordering

The products API will eventually support query parameters such as:

```text
/api/products/?category=mobile
/api/products/?search=iphone
/api/products/?ordering=-price
/api/products/?min_price=500
```

Multiple filters will also be supported.

---

## 📄 Pagination

Large result sets will not be returned in a single response.

The API will use DRF pagination mechanisms such as:

* Page Number Pagination
* Limit/Offset Pagination
* Cursor Pagination

The appropriate strategy will be selected based on the endpoint.

---

## 🖼️ File & Image Upload

Products will support image uploads.

The API will eventually handle:

```text
multipart/form-data
        ↓
Image Upload
        ↓
Product Image
        ↓
Media Storage
```

The project will also demonstrate how to handle multiple images for a single product.

---

## 🧪 Testing

The API will include automated tests for:

* Models
* Serializers
* API Views
* Authentication
* Permissions
* Validation
* CRUD operations
* Object-level authorization
* Important business rules

Testing will be implemented using Django and Django REST Framework testing utilities.

---

## ⚡ Performance

The project will also cover common performance problems in Django/DRF.

Topics include:

* N+1 Query Problem
* `select_related()`
* `prefetch_related()`
* Query optimization
* Database indexing
* Caching
* Redis
* API throttling

Example:

```python
Product.objects.select_related("category")
```

and:

```python
Product.objects.prefetch_related("images")
```

will be used where appropriate.

---

## 📚 API Documentation

The API will eventually provide OpenAPI-based documentation.

Planned documentation interfaces:

* Swagger UI
* ReDoc

The documentation will describe:

* Endpoints
* Request parameters
* Request bodies
* Authentication
* Responses
* Error responses

---

## 🐳 Production

The final project will be prepared for production with:

* PostgreSQL
* Environment variables
* Docker
* Gunicorn
* Redis
* Logging
* Security settings
* Static/media configuration
* Database configuration
* Production deployment

---

## ⚙️ Local Development

### 1. Clone the repository

```bash
git clone <repository-url>
cd shop_api
```

### 2. Create a virtual environment

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Environment Variables

Sensitive configuration should not be committed to Git.

Create a `.env` file for local development.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DATABASE_NAME=shop_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

A `.env.example` file can be committed to the repository without containing real secrets.

---

## 🗺️ Learning Roadmap

The project is developed progressively:

```text
01. Project Setup
02. Models
03. Serializers
04. Class-Based APIViews
05. CRUD
06. Authentication
07. JWT
08. Register / Login / Refresh
09. Permissions
10. Object-Level Permissions
11. Relationships
12. Filtering / Searching / Ordering
13. Pagination
14. File & Image Upload
15. Cart
16. Orders
17. Exception Handling
18. API Documentation
19. Testing
20. Query Optimization
21. Caching
22. Throttling
23. Security
24. Docker
25. PostgreSQL
26. Production Deployment
```

---

## 🎯 Learning Philosophy

This project is not intended to be just a collection of copied DRF code.

The goal is to understand:

```text
Request
   ↓
URL Routing
   ↓
Authentication
   ↓
Permission
   ↓
APIView
   ↓
Serializer
   ↓
Validation
   ↓
Business Logic
   ↓
ORM
   ↓
Database
   ↓
Serializer
   ↓
Response
```

The implementation starts with explicit **Class-Based APIViews** to make the underlying DRF flow clear.

Generic Views and ViewSets can be introduced later once the underlying mechanisms are understood.

---

## 📌 Project Status

🚧 **In Development**

Current focus:

* Project setup
* Custom User
* Product & Category models
* Serializers
* Class-Based APIViews

Upcoming:

* Authentication
* JWT
* Permissions
* Relationships
* Filtering
* Pagination
* Cart & Orders
* Testing
* Production setup
