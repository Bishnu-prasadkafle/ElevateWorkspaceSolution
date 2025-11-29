# 🚀 Quick Start Guide - Elevate Workforce Solutions

## Step 1: Start the Development Server

Open PowerShell in the project directory and run:

```powershell
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

Then open your browser and go to: **http://127.0.0.1:8000/**

---

## Step 2: Register as a Company

### 2a. Go to Registration Page
- Click **"Create New Account"** on the login page, or
- Direct URL: http://127.0.0.1:8000/accounts/register/

### 2b. Fill Registration Form
1. **Select:** "Company" (toggle button at top)
2. **Enter:**
   - First Name: e.g., "John"
   - Last Name: e.g., "Doe"
   - Username: e.g., "techcorp_admin"
   - Email: e.g., "admin@techcorp.com"
   - Phone: e.g., "+977-9841234567"
   - Company Name: e.g., "Tech Solutions Inc"
   - Industry: e.g., "Technology"
   - Location: e.g., "Kathmandu"
   - Company Description: e.g., "We develop innovative software"
   - Password: e.g., "SecurePass123" (min 8 chars)
   - Confirm Password: Same as above

3. **Click:** "Create Account"

### 2c. What Happens Next
✅ You will be **automatically logged in**  
✅ You will be redirected to the **Company Dashboard**

---

## Step 3: Post Your First Job

### 3a. Two Ways to Post a Job

**Method 1: From Dashboard**
1. Click the green **"Post New Job"** button (top right of dashboard)
2. Or click "Post New Job" button on the dashboard card

**Method 2: From Navigation**
- After login, click **"Post Job"** in the navbar (green button)

**Direct URL:** http://127.0.0.1:8000/jobs/create/

### 3b. Fill the Job Form

Required Fields (marked with *):
- **Job Title:** e.g., "Senior Python Developer"
- **Job Description:** e.g., "We are looking for an experienced Python developer..."
- **Job Type:** Select from dropdown (Full-Time, Part-Time, Contract, etc.)
- **Experience Level:** Select from dropdown (Entry, Mid, Senior, etc.)
- **Location:** e.g., "Kathmandu"
- **Number of Positions:** e.g., "2"
- **Requirements:** Enter each on a new line:
  ```
  5+ years Python experience
  Django framework expertise
  PostgreSQL knowledge
  ```

Optional Fields:
- **Minimum Salary:** e.g., "100000"
- **Maximum Salary:** e.g., "200000"
- **Application Deadline:** Pick a date (or leave blank for no deadline)

### 3c. Submit
Click **"Post Job"** button → Job is posted and visible to job seekers!

---

## Step 4: Manage Your Jobs from Dashboard

After posting, go back to **Company Dashboard**: http://127.0.0.1:8000/applications/company/dashboard/

### Dashboard Features:

**Top Section - "Post New Job"**
- Green button to add more jobs

**Stats Cards**
- Total Jobs posted
- Total Applications received
- Company Verification Status
- Edit Profile link

**Your Jobs Section** (left)
- Lists your 5 most recent jobs
- Click any job to view details
- See application count per job

**View All Applications Section** (bottom)
- All applications you've received
- Filter by status (Pending, Reviewed, Shortlisted, etc.)
- Click "View" to see full application details

---

## Step 5: Edit, Delete, or Deactivate Jobs

### View Job Details
1. Go to your **Dashboard**
2. Click on any job title in "Your Jobs" section
3. Or go to: http://127.0.0.1:8000/jobs/

### On Job Detail Page (Company Owner Only)
Three buttons appear in a card:

**Edit Job** (Yellow Button)
- Click to modify job details
- Change title, description, requirements, salary, etc.
- Click "Update" to save changes

**Delete Job** (Red Button)
- Permanently removes the job posting
- Click will ask for confirmation
- All associated applications are deleted

**Activate/Deactivate Job** (Blue Button)
- Toggle to hide/show the job from listings
- Deactivated jobs don't appear to job seekers
- Useful to pause hiring temporarily

---

## Step 6: View & Manage Applications

### View All Applications
- From **Dashboard:** Scroll to "All Applications" table at bottom
- Or filter by status dropdown

### Open an Application
1. Click **"View"** button next to any application
2. See full application details:
   - Applicant name and email
   - Applied job position
   - Cover letter (if provided)
   - Application status

### Update Application Status
1. On application detail page
2. You will see a status dropdown (company only)
3. Change from:
   - Pending → Reviewed → Shortlisted → Accepted/Rejected

---

## Step 7: Register as a Job Seeker (Optional Test)

### Registration
1. Go to: http://127.0.0.1:8000/accounts/register/
2. Select **"Job Seeker"** toggle
3. Fill in fields (location, skills, etc.)
4. Click "Create Account"

### After Login
- Click **"Jobs"** in navbar to see all posted jobs
- Click any job to view details
- Click **"Apply Now"** to submit application
- Go to **"My Applications"** to track status

---

## Troubleshooting

### Issue: Cannot access dashboard after registration
**Solution:** 
- Make sure you selected "Company" on registration form
- Refresh the page (Ctrl+R)
- Check browser console (F12 → Console) for errors

### Issue: "Company profile not found" error
**Solution:**
- Re-register as company with all required fields filled
- Or manually create via admin panel:
  1. Go to http://127.0.0.1:8000/admin/
  2. Login with superuser account
  3. Click "Companies" → "Add Company"
  4. Fill in and save

### Issue: Admin panel login fails
**Solution:**
- Reset superuser password:
  ```powershell
  python manage.py changepassword <username>
  ```
- Or create new superuser:
  ```powershell
  python manage.py createsuperuser
  ```

### Issue: Jobs not appearing in listings
**Solution:**
- Make sure job status is **"Active"** (blue toggle button)
- Check job creation succeeded (no error messages)
- Refresh page (Ctrl+R)
- Check application deadline hasn't passed

---

## Admin Panel (Optional)

Access admin for managing users, jobs, applications:

**URL:** http://127.0.0.1:8000/admin/

**Login with superuser account** created during setup.

### Admin Features:
- View all users, companies, jobs
- Create/edit/delete any record
- View all applications
- Filter and search

---

## Key URLs Reference

| Page | URL |
|------|-----|
| Home | http://127.0.0.1:8000/ |
| Register | http://127.0.0.1:8000/accounts/register/ |
| Login | http://127.0.0.1:8000/accounts/login/ |
| Browse Jobs | http://127.0.0.1:8000/jobs/ |
| Company Dashboard | http://127.0.0.1:8000/applications/company/dashboard/ |
| Post Job | http://127.0.0.1:8000/jobs/create/ |
| My Applications (Seeker) | http://127.0.0.1:8000/applications/my-applications/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## Testing Workflow

### Complete Flow Test (15 minutes):

1. **Register Company** (2 min)
   - Go to register page
   - Fill company form
   - Submit → Auto-login → Dashboard appears ✓

2. **Post a Job** (3 min)
   - Click "Post Job"
   - Fill job details
   - Submit → Redirected to job detail ✓

3. **View on Dashboard** (2 min)
   - Back to dashboard
   - See job in "Your Jobs" section ✓

4. **Register as Job Seeker** (3 min)
   - New browser tab or logout
   - Register as job seeker
   - Submit → Auto-login → Job list appears ✓

5. **Apply for Job** (2 min)
   - Search for your posted job
   - Click "Apply Now"
   - Fill cover letter
   - Submit → Confirmation message ✓

6. **Check Application** (3 min)
   - Switch back to company account (or new tab logged in as company)
   - Go to Dashboard
   - See application in "All Applications"
   - Click "View" to see details ✓

---

## Notes

- 🔒 Passwords must be at least 8 characters
- 📧 Email must be unique per account
- 👤 Username must be unique
- 💼 Job requirements should be one per line
- 📅 Application deadlines are optional
- 🔄 You can edit or deactivate jobs anytime
- 📊 Dashboard updates automatically

---

## Support

For issues or errors, check:
1. Server console output (terminal where `runserver` runs)
2. Browser console (F12 → Console tab)
3. Database logs for migration issues

If stuck, restart the server:
```powershell
# Stop current server (Ctrl+C in PowerShell)
python manage.py runserver
```

---

**Happy Job Posting! 🎉**
