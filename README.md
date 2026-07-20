
![GitHub Actions](https://github.com/tanvi259/AI-Code-Review-Assistant/actions/workflows/django.yml/badge.svg)

# 🤖 AI Code Review Assistant

## Overview

AI Code Review Assistant is a backend web application built using **Django** and **Django REST Framework** that allows authenticated users to submit source code and receive AI-generated code reviews using the **Google Gemini API**.

The application securely stores previous reviews, supports complete CRUD operations, and maintains review history for each authenticated user. The project is containerized using Docker and deployed on Render with PostgreSQL.

---

## 🚀 Features

- User Authentication using JWT
- User Registration & Login
- Submit source code for AI review
- AI-powered code analysis using Google Gemini API
- View all previous reviews
- View a single review
- Update code and regenerate AI review
- Delete reviews
- PostgreSQL database integration
- RESTful APIs
- Swagger API Documentation
- ReDoc Documentation
- Django Admin Panel
- Docker support
- Render deployment
- Secure environment variable management using `.env`

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Google Gemini API
- JWT Authentication
- Swagger (drf-yasg)
- ReDoc
- Render

---

## 📂 Project Structure

```text
AI-Code-Review-Assistant
│
├── accounts/
├── reviews/
├── aicodereview/
├── templates/
├── static/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create your environment file

For local development:

```text
.env
```

Required variables:

```text
SECRET_KEY=
DEBUG=True

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_SSLMODE=

ALLOWED_HOSTS=127.0.0.1,localhost

GEMINI_API_KEY=
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

---

## 🐳 Run with Docker

```bash
docker compose up --build
```

---

## 🔐 Authentication

This project uses **JWT Authentication**.

Workflow:

1. Signup
2. Login
3. Copy the Access Token
4. Click **Authorize** in Swagger
5. Test protected APIs

---

## 📖 API Documentation

Swagger

```text
/swagger/
```

ReDoc

```text
/redoc/
```

---

## 📌 API Endpoints

### Authentication

**POST**

```text
/api/signup/
```

**POST**

```text
/api/login/
```

---

### Code Reviews

**POST**

```text
/api/submitreview/
```

Submit source code for AI review.

---

**GET**

```text
/api/reviewlist/
```

Retrieve all reviews for the authenticated user.

---

**GET**

```text
/api/singlereview/<id>/
```

Retrieve a specific review.

---

**PUT**

```text
/api/updatereview/<id>/
```

Update source code and regenerate the AI review.

---

**DELETE**

```text
/api/deletereview/<id>/
```

Delete a review.

---

## 🌐 Live Demo

Homepage

```text
https://ai-code-review-assistant-7utu.onrender.com/
```

Swagger

```text
https://ai-code-review-assistant-7utu.onrender.com/swagger/
```

ReDoc

```text
https://ai-code-review-assistant-7utu.onrender.com/redoc/
```

---

## 👩‍💻 Author

**Tanvi**
