# Social Media API

A Django REST Framework-based API for a social media platform.

## Setup
1. Clone the repo: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Run server: `python manage.py runserver`

## User Authentication
- **Register**: POST `/api/register/`  
  - Body: `{"username": "string", "email": "string", "password": "string"}`
  - Returns: Token on success.
- **Login**: POST `/api/login/`  
  - Body: `{"username": "string", "password": "string"}`
  - Returns: Token on success.
- **Profile**: GET `/api/profile/`  
  - Header: `Authorization: Token <token>`
  - Returns: User data.

## User Model
- `username`, `email`, `password` (from `AbstractUser`).
- Custom fields: `bio`, `profile_picture`, `followers`.
