# Quick Start Guide - Admin Panel & Authentication

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Django 5.2+
- SQLite (included)

---

## ⚙️ Setup Instructions

### 1. Run Migrations
```bash
python manage.py migrate
```

### 2. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Then follow the prompts to create your admin account:
- Username: `admin`
- Email: `admin@example.com`
- Password: (secure password)

### 3. Start Development Server
```bash
python manage.py runserver
```

Server runs at: `http://127.0.0.1:8000/`

---

## 📌 Important URLs

| Feature | URL | Access |
|---------|-----|--------|
| Home | `/` | Public |
| Login | `/accounts/login/` | Public |
| Register | `/accounts/register/` | Public |
| Job List | `/jobs/` | Public |
| Job Seeker Dashboard | `/accounts/dashboard/` | Job Seekers Only |
| Company Dashboard | `/applications/company-dashboard/` | Companies Only |
| **Admin Dashboard** | `/accounts/admin/dashboard/` | **Admins Only** |
| **Manage Users** | `/accounts/admin/users/` | **Admins Only** |
| **Manage Companies** | `/accounts/admin/companies/` | **Admins Only** |

---

## 👥 Testing Different Roles

### Test as Job Seeker
1. Go to `/accounts/register/`
2. Select "Job Seeker"
3. Fill in details (username, email, password, etc.)
4. Submit → Redirected to Login
5. Login with credentials → Redirected to Job Seeker Dashboard

**Can Do:**
- Browse jobs
- Apply for jobs
- View applications status
- Edit profile
- Access dashboard

---

### Test as Company
1. Go to `/accounts/register/`
2. Select "Company"
3. Fill in company details (company name, industry, location, etc.)
4. Submit → Redirected to Login
5. Login with credentials → Redirected to Company Dashboard

**Can Do:**
- Post jobs
- View job applications
- Manage job postings
- Track recruitment
- Edit company profile

---

### Test as Admin
1. Use the superuser account created during setup
2. Login at `/accounts/login/`
3. See "Admin" button in navbar (warning color)
4. Click Admin → Access Admin Dashboard

**Can Do:**
- View all users (job seekers + companies)
- Add new users manually
- Edit user information
- Delete users
- Toggle user active/inactive status
- View all companies
- Edit company details
- Delete companies
- Toggle company verification
- View platform statistics

---

## 🎯 Admin Panel Features

### Admin Dashboard (`/accounts/admin/dashboard/`)
**Overview Stats:**
- Total Users Count
- Active Users Count
- Total Job Seekers
- Total Companies
- Recent Users Widget
- Recent Companies Widget
- Quick Action Buttons

### Manage Users (`/accounts/admin/users/`)
**Features:**
- Search users by username or email
- Filter by role (job seeker / company)
- Pagination (20 users per page)
- Quick actions:
  - Edit user details
  - Toggle active/inactive status
  - Delete user (with confirmation)

**Can Edit:**
- Username (disabled - read only)
- Email
- First Name
- Last Name
- Phone Number
- Active/Inactive status
- Job Seeker info (location, skills)
- Company info (name, industry, location, description)

### Add User (`/accounts/admin/users/add/`)
Manually create users:
- Select user type (job seeker / company)
- Enter credentials (username, email, password)
- Enter personal info
- Enter role-specific info
- System creates user and related profile

### Manage Companies (`/accounts/admin/companies/`)
**Features:**
- Search companies by name
- Filter by status (active / inactive / suspended)
- Filter by verification (verified / unverified)
- Pagination (20 companies per page)
- Quick actions:
  - Edit company details
  - Toggle verification status
  - Delete company (with confirmation)

---

## 🔑 User Roles & Permissions

### Job Seeker
```
Role: 'job_seeker'
Access: Browse jobs, apply, view dashboard
Cannot: Post jobs, manage companies
```

### Company
```
Role: 'company'
Access: Post jobs, view applications, manage jobs, view dashboard
Cannot: Apply for jobs, access admin
```

### Admin/Superuser
```
Status: is_superuser=True, is_staff=True
Access: Full platform management, all panels
Can: Do everything, manage all users/companies
```

---

## 🔄 Authentication Flow Diagram

```
┌─────────────────┐
│   User Visit    │
│  /accounts/     │
│   register/     │
└────────┬────────┘
         │
         ▼
  ┌──────────────┐
  │  Select Role │
  │  Job Seeker  │
  │  or Company  │
  └──────┬───────┘
         │
         ▼
  ┌──────────────────┐
  │  Fill Details &  │
  │  Submit Form     │
  └──────┬───────────┘
         │
         ▼
  ┌──────────────────┐
  │  Validate Data   │
  │  Create User     │
  │  Create Profile  │
  └──────┬───────────┘
         │
         ▼
  ┌──────────────────┐
  │  REDIRECT TO     │
  │  /accounts/login/│
  └──────┬───────────┘
         │
         ▼
  ┌──────────────────┐
  │  User Logs In    │
  │  Username/Pass   │
  └──────┬───────────┘
         │
         ▼
  ┌──────────────────────┐
  │  Check User Role     │
  └──────┬───────────────┘
         │
    ┌────┴─────────────────────┐
    │                          │
    ▼                          ▼
┌──────────────┐        ┌──────────────────┐
│ Job Seeker   │        │ Company          │
│ Dashboard    │        │ Dashboard        │
│ /accounts/   │        │ /applications/   │
│ dashboard/   │        │ company-         │
└──────────────┘        │ dashboard/       │
                        └──────────────────┘
                        
                   (Admin automatically
                    sees Admin Button)
```

---

## 🐛 Troubleshooting

### Issue: "This page is for X only" Error
**Solution:** Check you're logged in as the correct role. Logout and re-login if needed.

### Issue: Can't see Admin button
**Solution:** Your account must be a superuser. Create one with:
```bash
python manage.py createsuperuser
```

### Issue: Registration doesn't redirect to login
**Solution:** Check `accounts/views.py` line ~55 - should have `return redirect('accounts:login')`

### Issue: Login doesn't redirect to correct dashboard
**Solution:** Check `accounts/views.py` login_view() - should check `user.is_company()` and redirect accordingly

### Issue: Admin pages show 403 error
**Solution:** Only superusers can access admin pages. The user_passes_test decorator enforces this.

---

## 📝 Database Schema

### Users Table (`accounts_user`)
- username (unique)
- email (unique)
- password (hashed)
- first_name
- last_name
- phone_number
- role (job_seeker / company)
- is_active
- is_superuser
- is_staff
- created_at
- updated_at

### Job Seekers Table (`accounts_jobseeker`)
- user (OneToOne)
- location
- skills
- experience_years
- bio
- profile_picture
- resume
- created_at
- updated_at

### Companies Table (`companies_company`)
- user (OneToOne)
- company_name (unique)
- industry
- location
- description
- website
- logo
- status (active/inactive/suspended)
- verified (Boolean)
- created_at
- updated_at

---

## ✅ Verification Checklist

After setup, verify everything works:

- [ ] Superuser created successfully
- [ ] Can login with admin credentials
- [ ] Can see "Admin" button in navbar
- [ ] Can access `/accounts/admin/dashboard/`
- [ ] Can view users and companies lists
- [ ] Can add a new user (manual)
- [ ] Can edit user details
- [ ] Can delete user (with confirmation)
- [ ] Can add a new company
- [ ] Can manage companies
- [ ] Register as Job Seeker works
- [ ] Register as Company works
- [ ] Job Seeker redirects to job_seeker_dashboard after login
- [ ] Company redirects to company_dashboard after login
- [ ] Admin can access both management panels

---

## 🔗 Related Files Modified

```
✅ accounts/admin_views.py       (Fixed Q object query)
✅ templates/base.html           (Added Admin navbar link)
✅ JobPortal/settings.py         (Updated LOGIN_REDIRECT_URL comment)
✓ accounts/views.py             (No changes needed - already correct)
✓ accounts/urls.py              (No changes needed - already correct)
✓ application/views.py          (No changes needed - company_dashboard exists)
✓ accounts/models.py            (No changes needed - helper methods exist)
```

---

## 📞 Contact & Support

If you encounter issues:

1. Check browser console for JavaScript errors
2. Check Django terminal for Python errors
3. Check database migrations: `python manage.py showmigrations`
4. Review this guide for your specific issue
5. Check the SYSTEM_FIXES_SUMMARY.md file for detailed info

---

**Created:** December 1, 2025
**Status:** ✅ Ready to Use
