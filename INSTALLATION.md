# Elevate Workforce Solutions - Quick Start Guide

## 🚀 Installation & Setup Guide

### System Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Git
- 2GB free disk space

---

## Step-by-Step Setup

### 1. Clone/Download the Repository

```bash
git clone https://github.com/Bishnu-prasadkafle/ElevateWorkspaceSolution.git
cd ElevateWorkspaceSolution
```

### 2. Create Virtual Environment

#### On Windows (PowerShell):
```powershell
python -m venv myenv
myenv\Scripts\Activate.ps1
```

#### On Windows (Command Prompt):
```cmd
python -m venv myenv
myenv\Scripts\activate.bat
```

#### On macOS/Linux:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

**Expected output:**
```
Successfully installed asgiref-3.11.0 Django-5.2.8 sqlparse-0.5.4 tzdata-2025.2
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

**Expected output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, accounts, companies, jobs, application
Running migrations:
  Applying accounts.0001_initial... OK
  Applying accounts.0002_alter_user_options... OK
  ...
  (multiple migrations)
  ...
Running final checks...
```

### 5. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

**You'll be prompted to enter:**
- Username: `admin`
- Email: `admin@elevateworkforce.com`
- Password: (Create a strong password)
- Password (again): (Confirm password)

### 6. Run Development Server

```bash
python manage.py runserver
```

**Expected output:**
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 29, 2025 - 18:30:28
Django version 5.2.8, using settings 'JobPortal.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

## 🌐 Access the Application

### Application URLs

| Purpose | URL | Notes |
|---------|-----|-------|
| **Home Page** | http://127.0.0.1:8000/ | Main landing page |
| **Registration** | http://127.0.0.1:8000/accounts/register/ | Register as Job Seeker or Company |
| **Login** | http://127.0.0.1:8000/accounts/login/ | Sign in to your account |
| **Browse Jobs** | http://127.0.0.1:8000/jobs/ | View all available jobs |
| **My Applications** | http://127.0.0.1:8000/applications/my-applications/ | View your job applications (Job Seekers) |
| **Company Dashboard** | http://127.0.0.1:8000/applications/company/dashboard/ | Manage jobs and applications (Companies) |
| **Admin Panel** | http://127.0.0.1:8000/admin/ | Admin dashboard |

---

## 👥 Test Accounts

### Option 1: Create Your Own Test Accounts

#### As Job Seeker:
1. Go to http://127.0.0.1:8000/accounts/register/
2. Select "Job Seeker"
3. Fill in details:
   - Username: `john_seeker`
   - Email: `john@example.com`
   - Password: `TestPass123`
   - Skills: `Python, JavaScript, Django`
   - Location: `Kathmandu`
4. Click "Create Account"

#### As Company:
1. Go to http://127.0.0.1:8000/accounts/register/
2. Select "Company"
3. Fill in details:
   - Username: `tech_company`
   - Email: `info@techcompany.com`
   - Password: `TestPass123`
   - Company Name: `Tech Innovations Ltd.`
   - Industry: `Information Technology`
   - Location: `Kathmandu`
4. Click "Create Account"

### Option 2: Use Admin Panel

1. Go to http://127.0.0.1:8000/admin/
2. Login with superuser credentials (created in Step 5)
3. Click "Users" → "Add User"
4. Create test accounts as needed

---

## 🎯 Quick Demo Workflow

### As Job Seeker:

1. **Register & Login**
   - Create account as Job Seeker
   - Log in with your credentials

2. **Browse Jobs**
   - Navigate to "Jobs"
   - Use filters (job type, experience level, location)
   - Search for specific keywords

3. **Apply for Jobs**
   - Click on any job
   - Click "Apply Now"
   - Add optional cover letter
   - Submit application

4. **Track Applications**
   - Click "My Applications"
   - View status (Pending, Reviewed, Shortlisted, etc.)
   - Withdraw if needed

### As Company:

1. **Register & Login**
   - Create account as Company
   - Log in with your credentials

2. **Post a Job**
   - Click "Post a Job"
   - Fill in job details:
     - Title, description, requirements
     - Job type, experience level
     - Location, salary range
     - Application deadline
   - Click "Post Job"

3. **View Dashboard**
   - Go to "Dashboard"
   - See statistics (total jobs, applications, pending, etc.)
   - View list of all your jobs

4. **Manage Applications**
   - View applications for your jobs
   - Click on application to see details
   - Update status (Reviewed, Shortlisted, Rejected, Accepted)
   - Filter by status

---

## 🛠️ Troubleshooting

### Issue: "Django is not installed"
**Solution:**
```bash
pip install Django==5.2.8
```

### Issue: "No module named 'myenv'"
**Solution:** Activate virtual environment again:
```bash
# Windows
myenv\Scripts\activate

# macOS/Linux
source myenv/bin/activate
```

### Issue: "Port 8000 is already in use"
**Solution:** Use a different port:
```bash
python manage.py runserver 8001
```

### Issue: Database migration errors
**Solution:** Reset database (development only):
```bash
# Delete db.sqlite3
rm db.sqlite3

# Re-run migrations
python manage.py migrate

# Create new superuser
python manage.py createsuperuser
```

### Issue: Static files not loading (CSS/Images)
**Solution:**
```bash
python manage.py collectstatic --noinput
```

---

## 📁 Project Structure Overview

```
ElevateWorkspaceSolution/
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── requirement.txt            # Python dependencies
├── README.md                  # Main documentation
├── UML_DIAGRAMS.md           # UML diagrams and architecture
├── INSTALLATION.md           # This file
│
├── JobPortal/                # Main project app
│   ├── settings.py           # Django configuration
│   ├── urls.py               # URL routing
│   ├── views.py              # Project-level views
│   └── wsgi.py               # WSGI application
│
├── accounts/                 # Authentication app
│   ├── models.py             # User and JobSeeker models
│   ├── views.py              # Auth views
│   ├── urls.py               # Auth URLs
│   └── admin.py              # Admin configuration
│
├── jobs/                     # Jobs app
│   ├── models.py             # Job model
│   ├── views.py              # Job views
│   ├── urls.py               # Job URLs
│   └── admin.py              # Admin configuration
│
├── companies/                # Companies app
│   ├── models.py             # Company model
│   ├── admin.py              # Admin configuration
│   └── urls.py               # Company URLs
│
├── application/              # Job applications app
│   ├── models.py             # JobApplication model
│   ├── views.py              # Application views
│   ├── urls.py               # Application URLs
│   └── admin.py              # Admin configuration
│
├── templates/                # HTML templates
│   ├── base.html             # Base layout
│   ├── home.html             # Home page
│   ├── accounts/             # Auth templates
│   ├── jobs/                 # Job templates
│   └── application/          # Application templates
│
└── static/                   # Static files
    └── (CSS, JavaScript, images)
```

---

## 📚 Features Checklist

- [x] **Authentication System**
  - [x] User registration (Job Seeker & Company)
  - [x] Login/Logout functionality
  - [x] Password hashing and validation
  - [x] Session management

- [x] **Job Listings**
  - [x] Display all active jobs
  - [x] Pagination (10 jobs per page)
  - [x] Search functionality
  - [x] Filter by job type, experience level, location

- [x] **Job Management** (Companies)
  - [x] Create new jobs
  - [x] Edit existing jobs
  - [x] Delete jobs
  - [x] Activate/Deactivate jobs

- [x] **Job Applications**
  - [x] Apply for jobs with cover letter
  - [x] Track application status
  - [x] Withdraw applications
  - [x] View application history

- [x] **Company Dashboard**
  - [x] View posted jobs
  - [x] View received applications
  - [x] Update application status
  - [x] Track metrics and statistics

- [x] **User Profiles**
  - [x] Job seeker profiles (skills, experience, bio)
  - [x] Company profiles (description, website, logo)
  - [x] Profile editing capability

- [x] **Admin Panel**
  - [x] User management
  - [x] Job management
  - [x] Application management
  - [x] Company verification

- [x] **Documentation**
  - [x] README.md (detailed documentation)
  - [x] UML_DIAGRAMS.md (architecture diagrams)
  - [x] INSTALLATION.md (this file)

---

## 🚀 Next Steps

### Development
1. Customize styling in `templates/` and `static/`
2. Add email notifications
3. Implement API endpoints
4. Add more filtering options

### Deployment
1. Set up PostgreSQL database
2. Configure Gunicorn/Waitress server
3. Set up Nginx reverse proxy
4. Enable HTTPS/SSL
5. Deploy to production server

### For More Information
- See `README.md` for detailed documentation
- See `UML_DIAGRAMS.md` for architecture details
- Check Django documentation: https://docs.djangoproject.com/

---

## 📞 Support

If you encounter any issues:
1. Check the Troubleshooting section above
2. Review Django error messages in terminal
3. Check `db.sqlite3` for database issues
4. Review logs in Django admin panel

---

**Last Updated**: November 29, 2025
**Version**: 1.0
