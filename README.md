# AI Code Review Assistant

## Overview

AI Code Review Assistant is a backend web application built using Django and Django REST Framework that allows authenticated users to submit source code and receive AI-generated code reviews using the Google Gemini API.

The application securely stores previous reviews, supports complete CRUD operations, and maintains review history for each authenticated user.

---

## Features

- User Authentication using JWT
- Submit source code for AI review
- AI-powered code analysis using Google Gemini API
- View all previous reviews
- View a single review
- Update code and regenerate AI review
- Delete reviews
- PostgreSQL database integration
- RESTful APIs
- Secure API key management using .env

---

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Google Gemini API
- JWT Authentication
- Postman

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a .env file

```
GEMINI_API_KEY=your_api_key_here
```

Run migrations

```bash
python manage.py migrate
```

Run the server

```bash
python manage.py runserver
```

---

## API Endpoints

POST

```
/api/submitreview/
```

GET

```
/api/reviewlist/
```

GET

```
/api/singlereview/<id>/
```

PUT

```
/api/updatereview/<id>/
```

DELETE

```
/api/deletereview/<id>/
```

---

## Author

Tanvi