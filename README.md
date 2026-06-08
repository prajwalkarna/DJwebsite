# DJwebsite

A Django web application with user authentication built with PostgreSQL.

## Features
- User Registration with role selection (Admin/User)
- Email-based Login with session management
- Role-based Dashboard
- Custom Middleware for route protection

## Tech Stack
- Python 3.13
- Django 6.0
- PostgreSQL 18
- psycopg2

## Setup Instructions

### 1. Clone the repository
```bash
git clone git@github.com:prajwalkarna/DJwebsite.git
cd DJwebsite
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django psycopg2-binary python-dotenv
```

### 4. Create .env file
```
SECRET_KEY=your-secret-key
DB_NAME=djwebsite_db
DB_USER=djwebsite_user
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Start server
```bash
python manage.py runserver
```
