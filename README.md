Eyesalve - Eye Care Appointment CRM

A comprehensive Customer Relationship Management (CRM) system designed specifically for eye care clinics to manage patient appointments, records, and optical prescriptions.

Overview

Eyesalve is developed with Django and provides a complete solution for eye care practices to streamline their appointment scheduling and patient management processes. The system helps optometrists and clinic staff efficiently manage patient information, track appointments, and maintain optical records.

Features

Appointment Scheduling
- Schedule, reschedule, and cancel appointments
- Calendar view for daily/weekly/monthly appointments
- Appointment reminders and notifications
- Appointment types (eye exams, contact lens fitting, follow-ups, etc.)

Prescription Management
- Store optical prescriptions with detailed parameters
- Track prescription history for each patient
- Set expiration alerts for prescriptions
- Manage lens types and frame selections

User Management
- Role-based access control (Admin, Receptionist, Doctor)
- Secure authentication and authorization
- Activity logging for compliance

Technology Stack

- Backend: Django 6.x
- Database: SQLite 
- Frontend: HTML5, Bootstrap 5
- Additional Libraries:
  - Django Crispy Forms
  - Django Allauth for authentication
  - Django Guardian for object-level permissions

eyesalve/
├── manage.py
├── eyesalve/ # Project configuration
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── patients/ # Patient management app
├── appointments/ # Appointment scheduling app
├── prescriptions/ # Prescription management app
├── accounts/ # User authentication app
├── dashboard/ # Dashboard and analytics
├── static/ # Static files (CSS, JS, images)
├── media/ # User uploaded files
├── templates/ # Project templates
└── requirements.txt # Python dependencies


- Installation & Setup

Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

Step-by-Step Installation

1. Clone the repository
   # bash
   git clone https://github.com/sonicsibanda/Eyesalve-CRM.git
   cd eyesalve

2. Create virtual environment

python -m venv virt
s
Now Activate it:
Windows:
virt\Scripts\activate

macOS/Linux:
source virt/bin/activate
