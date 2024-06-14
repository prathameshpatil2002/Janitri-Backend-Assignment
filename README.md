# Janitri-Backend-Assignment

## Overview
This project is a simplified backend for a system that monitors patient heart rate data. It includes user management, patient management, and heart rate data recording functionalities. The project is built using Django and Django REST Framework.

## Setup and Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prathameshpatil2002/Janitri-Backend-Assignment.git
   cd Janitri-Backend-Assignment
   ```
2. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Apply migrations and run the server:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```
4. **Create a superuser to access the admin panel:**
   ```bash
   python manage.py createsuperuser
   ```
## Data Models
### User
#### Fields:
1. email (EmailField, unique)
2. password (CharField)
3. is_active (BooleanField, default=True)
4. is_admin (BooleanField, default=False)
   
### Patient
#### Fields:
1. user (ForeignKey to User)
2. name (CharField)
3. age (IntegerField)

### HeartRateData
#### Fields:
1. patient (ForeignKey to Patient)
2. heart_rate (IntegerField)
3. timestamp (DateTimeField, auto_now_add=True)

# Assumptions and Decisions
- No authentication or authorization protocols are used beyond simple email and password validation.
- Relationships are established using foreign keys to link users with patients and patients with heart rate data.
