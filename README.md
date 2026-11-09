# Employee Leave & Asset Management System

## Project Overview

The Employee Leave & Asset Management System is a web-based application developed using Python and Django. It helps organizations manage employee information, leave requests, and company asset requests through a centralized system.

The application provides separate functionalities for employees and administrators to manage employee records, apply for leaves, approve or reject leave requests, and manage company assets.

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Django Template Language (DTL)
- Pillow (for profile photo uploads)

## Features

### 1. User Authentication
- Employee Registration
- Employee Login and Logout
- Change Password
- Employee Profile Management

### 2. Employee Management
- View Employee Profile
- Edit Profile Information
- Upload Profile Photo
- Admin can create and disable employee accounts

### 3. Leave Management
- Apply for Leave
- Available Leave Types:
  - Sick Leave
  - Casual Leave
  - Earned Leave
- View Leave History
- Cancel Pending Leave Requests
- Admin can Approve or Reject Leave Requests

### 4. Asset Management
- Request Company Assets
- Available Asset Types:
  - Laptop
  - Monitor
  - Keyboard
  - Headset
- View Asset Requests
- Admin can Approve, Reject, and Assign Assets

### 5. Dashboard
- Total Employees
- Total Leave Requests
- Approved Leaves
- Pending Asset Requests

### 6. Search and Filters
- Search Employees by Name and Department
- Filter Leave Requests by Status and Date
- Manage Employee and Leave Records through Django Admin


## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd employee_management
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## Learning Outcomes

Through this project, I gained practical experience with:

- Django project and application structure
- Django Models, Views, and Templates
- Django Forms and ModelForms
- User Authentication and Authorization
- Database relationships using Django ORM
- CRUD operations
- File uploads
- Django Admin customization
- URL routing and template rendering

## Future Enhancements

- Employee leave balance calculation
- Email notifications for leave approvals
- Role-based access control
- Improved dashboard with reports and statistics
- Deployment to a live hosting platform

## Author

**Preethi Yadav**

Python | Django | HTML | SQL

