# Elevate Workforce Solutions - Job Portal

A comprehensive web-based employment agency platform built with Django that connects job seekers with companies, providing equal opportunities, transparency, and easy access to job opportunities across Nepal.

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Technology Stack](#technology-stack)
4. [Installation & Setup](#installation--setup)
5. [Usage Guide](#usage-guide)
6. [Architecture & Design](#architecture--design)
7. [Database Schema](#database-schema)
8. [API Endpoints](#api-endpoints)
9. [Deployment](#deployment)

---

## Features

### 1. **Secure Authentication System**
- User registration for both job seekers and companies
- Secure login/logout functionality
- Role-based access control (Job Seeker vs Company)
- Session management and CSRF protection
- Password validation and hashing

### 2. **Job Listings & Management**
- Display all active job listings with pagination (10 jobs per page)
- Advanced search and filtering:
  - Search by job title, company name, or description
  - Filter by job type (Full-time, Part-time, Contract, Internship)
  - Filter by experience level (Entry, Mid, Senior, Executive)
  - Filter by location
- Company ability to:
  - Create new job postings
  - Update existing job postings
  - Delete job postings
  - Activate/deactivate jobs

### 3. **Job Application System**
- Job seekers can apply for jobs with optional cover letters
- Application status tracking:
  - Pending
  - Reviewed
  - Shortlisted
  - Rejected
  - Accepted
  - Withdrawn
- Application deadline enforcement
- Ability to withdraw applications

### 4. **Company Dashboard**
- View all posted jobs and their statistics
- View applications for all jobs
- Update application statuses
- Track application metrics (pending, reviewed, shortlisted, rejected, accepted)
- Quick access to post new jobs

### 5. **User Profiles**
- Job seeker profiles with:
  - Skills list
  - Experience years
  - Location
  - Bio
  - Resume upload capability
  - Profile picture
- Company profiles with:
  - Company description
  - Industry type
  - Location
  - Website URL
  - Company size
  - Logo upload capability
  - Verification status

---

## Project Structure

```
ElevateWorkspaceSolution/
├── JobPortal/                 # Main project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   ├── views.py              # Project-level views (home page)
│   ├── wsgi.py               # WSGI application
│   └── asgi.py               # ASGI application
│
├── accounts/                  # User authentication app
│   ├── models.py             # User and JobSeeker models
│   ├── views.py              # Auth views (register, login, logout, profile)
│   ├── urls.py               # Account URL routes
│   ├── admin.py              # Admin configuration
│   └── migrations/           # Database migrations
│
├── jobs/                      # Job management app
│   ├── models.py             # Job model
│   ├── views.py              # Job views (list, detail, create, edit, delete)
│   ├── urls.py               # Job URL routes
│   ├── admin.py              # Admin configuration
│   └── migrations/           # Database migrations
│
├── companies/                 # Company management app
│   ├── models.py             # Company model
│   ├── views.py              # Company views
│   ├── urls.py               # Company URL routes
│   ├── admin.py              # Admin configuration
│   └── migrations/           # Database migrations
│
├── application/               # Job application app
│   ├── models.py             # JobApplication model
│   ├── views.py              # Application views (apply, dashboard, status update)
│   ├── urls.py               # Application URL routes
│   ├── admin.py              # Admin configuration
│   └── migrations/           # Database migrations
│
├── templates/                 # HTML templates
│   ├── base.html             # Base template with navigation and styling
│   ├── home.html             # Home page with featured jobs
│   ├── accounts/
│   │   ├── register.html     # Registration form
│   │   ├── login.html        # Login form
│   │   ├── profile.html      # User profile view
│   │   └── profile_edit.html # Profile edit form
│   ├── jobs/
│   │   ├── job_list.html     # Job listings page with filters
│   │   ├── job_detail.html   # Job detail page
│   │   ├── create_job.html   # Create job form (company)
│   │   └── edit_job.html     # Edit job form (company)
│   └── application/
│       ├── apply_job.html    # Job application form
│       ├── my_applications.html # Job seeker's applications list
│       ├── application_detail.html # Application details
│       └── company_dashboard.html # Company dashboard
│
├── static/                    # Static files (CSS, JS, images)
├── media/                     # User uploaded files (resumes, logos, pictures)
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script
├── requirement.txt           # Python dependencies
└── README.md                 # This file
```

---

## Technology Stack

### Backend
- **Framework**: Django 5.2.8
- **Database**: SQLite (Development), PostgreSQL (Production recommended)
- **Language**: Python 3.x
- **ORM**: Django ORM

### Frontend
- **HTML5 / CSS3**: Template-based rendering
- **CSS Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.0.0
- **JavaScript**: Vanilla JS for client-side interactions

### Server
- **Development Server**: Django Development Server
- **Production Server**: Gunicorn / Waitress (recommended)

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/ElevateWorkspaceSolution.git
cd ElevateWorkspaceSolution
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv myenv
myenv\Scripts\activate

# On macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirement.txt
```

### Step 4: Apply Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Admin)
```bash
python manage.py createsuperuser
# Follow the prompts to set username, email, and password
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

### Step 7: Access Admin Panel
Navigate to: `http://127.0.0.1:8000/admin/`
- Login with your superuser credentials
- Manage users, jobs, applications, and companies

---

## Usage Guide

### For Job Seekers

1. **Registration**
   - Click "Register" → Select "Job Seeker"
   - Fill in your details (name, email, skills, location)
   - Create a secure password

2. **Browse Jobs**
   - Navigate to "Jobs" section
   - Use filters to search by:
     - Job title/company name
     - Job type (Full-time, Part-time, etc.)
     - Experience level
     - Location
   - Click "View Details" to see full job information

3. **Apply for Jobs**
   - On job detail page, click "Apply Now"
   - Optionally add a cover letter
   - Submit application

4. **Track Applications**
   - Click "My Applications" in navigation
   - View all your applications and their statuses
   - Withdraw applications if needed

5. **Update Profile**
   - Click on your username → "Edit Profile"
   - Update skills, experience, bio, etc.

### For Companies

1. **Registration**
   - Click "Register" → Select "Company"
   - Fill in company details (name, industry, location, description)
   - Create a secure password

2. **Post Jobs**
   - Click "Post a Job" button
   - Fill in job details:
     - Job title and description
     - Job type and experience level
     - Location and salary range
     - Requirements and deadline
   - Submit to post the job

3. **Manage Jobs**
   - Go to Dashboard
   - View all your posted jobs
   - Edit or delete jobs as needed
   - Activate/deactivate jobs

4. **Review Applications**
   - View all applications received in Dashboard
   - Filter by status (Pending, Reviewed, Shortlisted, etc.)
   - Click on application to view candidate details
   - Update application status:
     - Reviewed
     - Shortlisted
     - Rejected
     - Accepted

5. **Track Metrics**
   - Dashboard shows:
     - Total jobs posted
     - Active jobs
     - Total applications
     - Pending applications
     - Status breakdown

---

## Architecture & Design

### MVC Design Pattern

The application strictly follows the Model-View-Controller (MVC) architecture:

#### **Models (M)**
- `User`: Custom user model extending Django's AbstractUser
- `JobSeeker`: Profile model for job seekers
- `Company`: Profile model for companies
- `Job`: Job posting model with all job details
- `JobApplication`: Application model linking job seekers to jobs

#### **Views (V)**
- Templates for all pages using Django Template Language
- Bootstrap-based responsive UI
- Form rendering and error display
- User authentication checks and redirects

#### **Controllers (C)**
- View functions handle business logic
- URL routing via Django's URL configuration
- Request/response handling
- Database operations through ORM

### Object-Oriented Design

All models follow OOP principles:
- **Encapsulation**: Models encapsulate data and related methods
- **Abstraction**: Complex operations abstracted into model methods
- **Inheritance**: JobSeeker and Company extend User model relationships
- **Polymorphism**: Different user roles (job seeker vs company) with different behaviors

---

## Database Schema

### User Model
```
User (extends AbstractUser)
├── username (CharField, unique)
├── email (EmailField)
├── password (CharField, hashed)
├── first_name (CharField)
├── last_name (CharField)
├── phone_number (CharField, optional)
├── role (CharField: 'job_seeker' or 'company')
├── is_active (BooleanField, default=True)
├── created_at (DateTimeField, auto)
├── updated_at (DateTimeField, auto)
└── Methods:
    ├── is_company()
    ├── is_job_seeker()
    └── __str__()
```

### JobSeeker Model
```
JobSeeker
├── user (OneToOneField → User)
├── bio (TextField, optional)
├── resume (FileField, optional)
├── skills (TextField)
├── experience_years (IntegerField)
├── location (CharField)
├── profile_picture (ImageField, optional)
├── created_at (DateTimeField, auto)
├── updated_at (DateTimeField, auto)
└── Methods:
    ├── get_skills_list()
    └── __str__()
```

### Company Model
```
Company
├── user (OneToOneField → User)
├── company_name (CharField, unique)
├── description (TextField)
├── website (URLField, optional)
├── industry (CharField)
├── location (CharField)
├── company_size (CharField, optional)
├── logo (ImageField, optional)
├── status (CharField: 'active', 'inactive', 'suspended')
├── verified (BooleanField, default=False)
├── created_at (DateTimeField, auto)
├── updated_at (DateTimeField, auto)
└── Methods:
    ├── is_active_company()
    ├── get_total_jobs_posted()
    ├── get_active_jobs()
    └── __str__()
```

### Job Model
```
Job
├── company (ForeignKey → Company)
├── title (CharField)
├── description (TextField)
├── requirements (TextField)
├── location (CharField)
├── salary_min (DecimalField, optional)
├── salary_max (DecimalField, optional)
├── job_type (CharField: 'full_time', 'part_time', 'contract', 'internship')
├── experience_level (CharField: 'entry', 'mid', 'senior', 'executive')
├── is_active (BooleanField, default=True)
├── posted_at (DateTimeField, auto)
├── updated_at (DateTimeField, auto)
├── deadline (DateTimeField, optional)
├── total_positions (IntegerField)
└── Methods:
    ├── is_application_deadline_passed()
    ├── get_salary_range()
    ├── get_requirements_list()
    ├── get_total_applications()
    └── __str__()
```

### JobApplication Model
```
JobApplication
├── job (ForeignKey → Job)
├── job_seeker (ForeignKey → JobSeeker)
├── status (CharField: 'pending', 'reviewed', 'shortlisted', 'rejected', 'accepted', 'withdrawn')
├── cover_letter (TextField, optional)
├── applied_at (DateTimeField, auto)
├── updated_at (DateTimeField, auto)
├── unique_together: (job, job_seeker)
└── Methods:
    ├── get_status_badge_color()
    ├── can_be_withdrawn()
    ├── get_days_since_applied()
    └── __str__()
```

---

## API Endpoints

### Authentication Endpoints
```
GET/POST   /accounts/register/          - User registration
GET/POST   /accounts/login/             - User login
POST       /accounts/logout/            - User logout
GET        /accounts/profile/           - View user profile
GET/POST   /accounts/profile/edit/      - Edit user profile
```

### Job Endpoints
```
GET        /jobs/                       - List all active jobs (with pagination)
GET        /jobs/<id>/                  - View job details
GET/POST   /jobs/create/                - Create new job (companies only)
GET/POST   /jobs/<id>/edit/             - Edit job (company owner only)
POST       /jobs/<id>/delete/           - Delete job (company owner only)
POST       /jobs/<id>/toggle-status/    - Activate/deactivate job
```

### Application Endpoints
```
GET/POST   /applications/apply/<job_id>/ - Apply for a job
GET        /applications/<id>/            - View application details
GET        /applications/my-applications/ - View job seeker's applications
POST       /applications/<id>/withdraw/   - Withdraw application
GET/POST   /applications/<id>/update-status/ - Update application status (company)
GET        /applications/company/dashboard/ - Company dashboard
```

### Home Page
```
GET        /                            - Home page with featured jobs
```

---

## Deployment

### Production Checklist

1. **Security Settings**
   - Set `DEBUG = False` in settings.py
   - Set secure `SECRET_KEY`
   - Configure `ALLOWED_HOSTS`
   - Use HTTPS only

2. **Database**
   - Migrate to PostgreSQL for production
   - Set up database backups

3. **Static Files**
   - Run `python manage.py collectstatic`
   - Serve via CDN or web server

4. **Application Server**
   - Deploy with Gunicorn
   - Use Nginx as reverse proxy

### Example Deployment with Gunicorn

```bash
# Install Gunicorn
pip install gunicorn

# Run Gunicorn
gunicorn JobPortal.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

---

## Testing

To run tests:
```bash
python manage.py test
```

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

This project is licensed under the MIT License - see LICENSE file for details.

---

## Support

For issues, questions, or suggestions, please:
- Create an issue on GitHub
- Contact: support@elevateworkforce.com
- Visit: www.elevateworkforce.com

---

## Changelog

### Version 1.0.0
- Initial release
- Complete authentication system
- Job listing and management
- Application tracking
- Company dashboard
- User profiles
- Advanced search and filtering

---

## Future Enhancements

- Email notifications for applications
- Resume parsing and matching
- Interview scheduling system
- Skill verification badges
- Advanced analytics and reporting
- Mobile application
- Multi-language support
- Video interview integration
- AI-powered job recommendations
- Salary insights and trends

---

**Last Updated**: November 29, 2025
