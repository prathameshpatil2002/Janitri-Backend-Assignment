# API Endpoints
## User Registration
### URL: POST /api/register
### Request Body:
```bash
{
    "email": "user1@janitri.com",
    "password": "user1@123"
}
```
### Response:
```bash
{
    "id": 1,
    "email": "user1@janitri.com"
}
```

## User Login
### URL: POST /api/login
### Request Body:
```bash
{
    "email": "user1@janitri.com",
    "password": "user1@123"
}
```
### Response:
```bash
{
    "message": "Login successful!"
}
```
### Error Response:
```bash
{
    "error": "Invalid credentials"
}
```

## Manage Patients
## Add Patient
### URL: POST /api/patients
### Request Body:
```bash
{
    "user": 1,
    "name": "patient1",
    "age": 22,
}
```
### Response:
```bash
{
    "id": 1,
    "user": 1,
    "name": "patient1",
    "age": 22
}
```
## Retrieve Patients
### URL: GET /api/patients
### Response:
```
[
    {
        "id": 1,
        "user": 1,
       "name": "patient1",
       "age": 22,
    }
]
```
## Get Single Patient Details
### URL: GET /api/patients/<patient_id>
### Response:
```
{
    "id": 1,
    "user": 1,
   "name": "patient1",
    "age": 22
}
```
### Error Response:
```
{
    "error": "Patient not found"
}
```

## Heart Rate Data
## Add Heart Rate Data
### URL: POST /api/heart-rate
### Request Body:
```
{
    "patient": 1,
    "heart_rate": 72
}
```
### Response:
```
{
    "id": 1,
    "patient": 1,
    "heart_rate": 72,
    "timestamp": "2024-06-12T12:00:00Z"
}
```
## Retrieve Heart Rate Data
### URL: GET /api/heart-rate
### Response:
```
[
    {
        "id": 1,
        "patient": 1,
        "heart_rate": 72,
        "timestamp": "2024-06-12T12:00:00Z"
    }
]
```
## Get Single Patient Heart Rate Data
### URL: GET /api/patients/<patient_id>/heart-rate
### Response:
```
[
    {
        "id": 1,
        "patient": 1,
        "heart_rate": 72,
        "timestamp": "2024-06-12T12:00:00Z"
    }
]
```
### Error Response:
```
{
    "error": "No heart rate data found for this patient"
}
```
