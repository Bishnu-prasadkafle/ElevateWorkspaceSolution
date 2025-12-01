# Complete System Testing Guide

## Overview
This document provides step-by-step instructions to test all the fixed features of the Elevate Workforce Solutions job portal.

---

## Part 1: Initial Setup

### Step 1: Apply Migrations
```bash
cd c:\Users\ASUS\ElevateWorkspaceSolution
python manage.py migrate
```

### Step 2: Create Admin Account
```bash
python manage.py createsuperuser
```
Example values:
- Username: `admin`
- Email: `admin@example.com`
- Password: `AdminPassword123`

### Step 3: Start Server
```bash
python manage.py runserver
```

Open browser: `http://127.0.0.1:8000/`

---

## Part 2: Test Registration & Login

### Test Case 1: Register as Job Seeker

**Steps:**
1. Click "Register" or go to `/accounts/register/`
2. Select "Job Seeker" radio button
3. Fill form:
   - First Name: John
   - Last Name: Doe
   - Username: john_doe
   - Email: john@example.com
   - Phone: 9841234567
   - Location: Kathmandu
   - Skills: Python, Django, JavaScript
   - Password: TestPass123
   - Confirm Password: TestPass123
4. Click "Create Account"

**Expected Result:** 
- ✅ Message: "Job Seeker account created successfully!"
- ✅ Redirected to Login page (/accounts/login/)
- ❌ Should NOT auto-login

**Verification:**
- URL changed to `/accounts/login/`
- Login form is visible
- Previous form data is NOT filled

---

### Test Case 2: Login as Job Seeker

**Steps:**
1. On Login page
2. Enter Username: `john_doe`
3. Enter Password: `TestPass123`
4. Click "Sign In"

**Expected Result:**
- ✅ Message: "Welcome back, john_doe!"
- ✅ Redirected to Job Seeker Dashboard (/accounts/dashboard/)
- ✅ Page shows: "Dashboard", user applications, application stats

**Verification:**
- URL is `/accounts/dashboard/`
- Shows "Total Applications", "Pending", "Accepted", "Rejected" cards
- Shows user profile information
- Navigation shows "Dashboard" link

---

### Test Case 3: Register as Company

**Steps:**
1. Go to `/accounts/register/`
2. Select "Company" radio button
3. Fill form:
   - First Name: Tech
   - Last Name: Company
   - Username: tech_company
   - Email: tech@example.com
   - Phone: 9842345678
   - Company Name: Tech Solutions Inc
   - Industry: Technology
   - Location: Pokhara
   - Description: Leading tech company
   - Password: TestPass123
   - Confirm Password: TestPass123
4. Click "Create Account"

**Expected Result:**
- ✅ Message: "Company account created successfully!"
- ✅ Redirected to Login page

---

### Test Case 4: Login as Company

**Steps:**
1. On Login page
2. Enter Username: `tech_company`
3. Enter Password: `TestPass123`
4. Click "Sign In"

**Expected Result:**
- ✅ Message: "Welcome back, tech_company!"
- ✅ Redirected to Company Dashboard (/applications/company-dashboard/)
- ✅ Page shows: Jobs, applications, recruitment stats

**Verification:**
- URL is `/applications/company-dashboard/`
- Shows "Total Jobs", "Active Jobs", "Total Applications", "Pending" cards
- Navigation shows "Post Job" button and "Dashboard" link

---

### Test Case 5: Admin Login

**Steps:**
1. Go to `/accounts/login/`
2. Enter Username: `admin`
3. Enter Password: `AdminPassword123`
4. Click "Sign In"

**Expected Result:**
- ✅ Logged in successfully
- ✅ Check navbar for "Admin" button (warning/yellow color)
- ✅ Click "Admin" button → Goes to `/accounts/admin/dashboard/`

**Verification:**
- Navbar shows yellow "Admin" button
- Admin Dashboard visible
- Shows statistics (Total Users, Active Users, Job Seekers, Companies)

---

## Part 3: Test Admin Panel

### Admin Dashboard (/accounts/admin/dashboard/)

**Expected Features:**
1. ✅ Statistics cards showing:
   - Total Users
   - Active Users
   - Job Seekers
   - Companies

2. ✅ Recent Users widget
   - Shows last 5 users created
   - Edit button for each

3. ✅ Recent Companies widget
   - Shows last 5 companies
   - Edit button for each

4. ✅ Admin Actions buttons:
   - "Manage Users" → /accounts/admin/users/
   - "Add New User" → /accounts/admin/users/add/
   - "Manage Companies" → /accounts/admin/companies/

---

### Test Case 6: Manage Users (/accounts/admin/users/)

**Features to Test:**

**A. Search Functionality**
1. Enter search term in search box
2. Test searching by:
   - Username: "john_doe"
   - Email: "john@example.com"
3. Click "Filter"

**Expected:** ✅ Results show matching users

**B. Role Filter**
1. Select "Job Seeker" from role dropdown
2. Click "Filter"

**Expected:** ✅ Shows only job seekers

3. Select "Company"
4. Click "Filter"

**Expected:** ✅ Shows only companies

**C. User Actions**
For each user, three buttons appear:
1. ✅ Edit (pencil icon) - Edit user details
2. ✅ Toggle Status (toggle icon) - Activate/deactivate
3. ✅ Delete (trash icon) - Delete with confirmation

---

### Test Case 7: Add User Manually

**Steps:**
1. Admin Dashboard → Click "Add New User" or go to `/accounts/admin/users/add/`
2. Select User Type: "Job Seeker"
3. Fill form:
   - Username: manual_user
   - Email: manual@example.com
   - Password: ManualPass123
   - Phone: 9843456789
   - First Name: Manual
   - Last Name: User
   - Location: Bhaktapur
   - Skills: HTML, CSS
4. Click "Create User"

**Expected Result:**
- ✅ Message: "Job seeker created successfully!"
- ✅ Redirected to Manage Users page
- ✅ New user appears in list

**Verification:**
- Can login with username "manual_user"
- User is Job Seeker type
- Can access job seeker dashboard

---

### Test Case 8: Edit User

**Steps:**
1. Manage Users → Click Edit button for any user
2. Change fields:
   - Email: new@example.com
   - Phone: 9800000000
   - First Name: Updated
3. Check "Active" checkbox to toggle status
4. Click "Save Changes"

**Expected Result:**
- ✅ Message: "User updated successfully!"
- ✅ Redirected to Manage Users
- ✅ Changes reflected in user list

---

### Test Case 9: Delete User

**Steps:**
1. Manage Users → Click Delete button (trash icon)
2. Confirm modal appears
3. Click "Delete"

**Expected Result:**
- ✅ Message: "User '[username]' has been deleted successfully"
- ✅ User removed from list
- ✅ Cannot login with deleted user credentials

---

### Test Case 10: Manage Companies (/accounts/admin/companies/)

**Features to Test:**

**A. Search Companies**
1. Type company name in search box
2. Click "Filter"

**Expected:** ✅ Shows matching companies

**B. Filter by Status**
1. Select "Active" from status dropdown
2. Click "Filter"

**Expected:** ✅ Shows only active companies

**C. Filter by Verification**
1. Select "Unverified"
2. Click "Filter"

**Expected:** ✅ Shows only unverified companies

**D. Company Actions**
For each company:
1. ✅ Edit (pencil) - Edit details
2. ✅ Toggle Verification (toggle) - Verify/unverify
3. ✅ Delete (trash) - Delete with confirmation

---

### Test Case 11: Edit Company

**Steps:**
1. Manage Companies → Click Edit for any company
2. Change:
   - Company Name: Updated Company Name
   - Industry: Finance
   - Location: Lalitpur
   - Description: Updated description
3. Status: Select "Inactive"
4. Checked "Verified" checkbox
5. Click "Save Changes"

**Expected Result:**
- ✅ Message: "Company updated successfully!"
- ✅ Changes reflected in companies list

---

### Test Case 12: Toggle Company Verification

**Steps:**
1. Manage Companies
2. Click Toggle (toggle icon) for unverified company
3. Confirm

**Expected Result:**
- ✅ Message: "Company 'X' has been verified"
- ✅ Verified badge changes

**Repeat for verified company:**
- ✅ Message: "Company 'X' has been unverified"

---

## Part 4: Test Navigation & Role-Based Access

### Test Case 13: Job Seeker Navigation

**After logging in as job seeker:**

1. ✅ Navbar shows:
   - Jobs (all users)
   - Dashboard (job seeker specific)
   - My Applications (job seeker specific)
   - User dropdown with Profile options

2. ✅ Clicking Dashboard goes to `/accounts/dashboard/`

3. ✅ Cannot access:
   - `/accounts/admin/dashboard/` → Gets 403 error
   - `/accounts/admin/users/` → Gets 403 error
   - Post Job button not visible
   - Company Dashboard not accessible

---

### Test Case 14: Company Navigation

**After logging in as company:**

1. ✅ Navbar shows:
   - Jobs (all users)
   - Dashboard (company specific)
   - Post Job button (yellow)
   - User dropdown with Profile options

2. ✅ Clicking Dashboard goes to `/applications/company-dashboard/`

3. ✅ Cannot access:
   - `/accounts/admin/dashboard/` → Gets 403 error
   - Admin button not visible in navbar

---

### Test Case 15: Admin Navigation

**After logging in as admin:**

1. ✅ Navbar shows:
   - Jobs
   - Admin button (warning/yellow color) - NEW
   - User dropdown

2. ✅ Clicking Admin goes to `/accounts/admin/dashboard/`

3. ✅ Can access all management pages:
   - `/accounts/admin/users/`
   - `/accounts/admin/companies/`
   - `/accounts/admin/users/add/`

---

## Part 5: Test Error Handling

### Test Case 16: Logout Test

**Steps:**
1. Login as any user
2. Click user dropdown menu
3. Click "Logout"
4. Confirm logout

**Expected Result:**
- ✅ Message: "You have been logged out successfully"
- ✅ Redirected to Home page
- ✅ Cannot access protected pages (redirects to login)

---

### Test Case 17: Authentication Redirect

**Steps:**
1. Logout
2. Try accessing `/accounts/dashboard/` directly
3. Should redirect to login page

**Expected Result:**
- ✅ URL changes to `/accounts/login/?next=/accounts/dashboard/`
- ✅ Login form appears
- ✅ After login, redirects back to dashboard

---

### Test Case 18: Invalid Credentials

**Steps:**
1. Go to login page
2. Enter Username: `nonexistent`
3. Enter Password: `wrongpass`
4. Click Sign In

**Expected Result:**
- ✅ Message: "Invalid username or password"
- ✅ Stays on login page
- ✅ Form is empty (for security)

---

### Test Case 19: Duplicate Registration

**Steps:**
1. Try registering with existing username
2. System should show error

**Expected Result:**
- ✅ Error: "Username already exists"
- ✅ Back on register page
- ✅ Form fields preserved

**Repeat with email:**
- ✅ Error: "Email already registered"

---

### Test Case 20: Admin-Only Page Access

**Steps:**
1. Login as job seeker
2. Try accessing `/accounts/admin/dashboard/` in URL bar
3. Press Enter

**Expected Result:**
- ✅ Gets 403 Forbidden error
- ✅ Message about not having permission
- ✅ Cannot bypass with direct URL

---

## Part 6: Search Bug Verification

### Test Case 21: Search Multiple Users (Tests Fixed Q Query)

**Steps:**
1. Admin Dashboard → Manage Users
2. Search for "john" (should search username AND email)
3. Click Filter

**Expected Result:**
- ✅ Shows users with "john" in username OR email
- ✅ NOT just username matches
- ✅ Q object fix working correctly

**Technical Check:**
- Open Django shell: `python manage.py shell`
- Run query:
```python
from django.db.models import Q
from accounts.models import User
users = User.objects.filter(Q(username__icontains='john') | Q(email__icontains='john'))
print(users.count())  # Should show results
```

---

## Part 7: Navbar Enhancement Verification

### Test Case 22: Admin Button Visibility

**Steps:**
1. Login as admin
2. Check navbar

**Expected Result:**
- ✅ Yellow "Admin" button visible
- ✅ Click admin button goes to dashboard
- ✅ Button NOT visible for non-admins

---

### Test Case 23: Dashboard Link for Job Seekers

**Steps:**
1. Login as job seeker
2. Check navbar

**Expected Result:**
- ✅ "Dashboard" link visible (not just "My Applications")
- ✅ Clicking Dashboard goes to correct page

---

## Summary Checklist

### Core Functionality
- [ ] ✅ Registration redirects to login (not auto-login)
- [ ] ✅ Job seeker login → job_seeker_dashboard
- [ ] ✅ Company login → company_dashboard
- [ ] ✅ Admin can see Admin button
- [ ] ✅ Admin can manage users (add/edit/delete)
- [ ] ✅ Admin can manage companies (add/edit/delete)

### Admin Panel
- [ ] ✅ Admin dashboard shows stats
- [ ] ✅ Manage users with search/filter
- [ ] ✅ Manage companies with search/filter
- [ ] ✅ Add user manually
- [ ] ✅ Edit user details
- [ ] ✅ Delete users
- [ ] ✅ Edit companies
- [ ] ✅ Delete companies

### Navigation
- [ ] ✅ Role-based navbar links
- [ ] ✅ Admin button for superusers
- [ ] ✅ Dashboard links for job seekers
- [ ] ✅ Post Job button for companies

### Bug Fixes
- [ ] ✅ Search query uses Q objects correctly
- [ ] ✅ Pagination works
- [ ] ✅ Filters work correctly

### Error Handling
- [ ] ✅ Logout works
- [ ] ✅ Protected pages redirect to login
- [ ] ✅ Invalid credentials show error
- [ ] ✅ Duplicate registration prevented
- [ ] ✅ Admin-only pages enforce access control

---

## Test Data Setup Commands

If you need to create test data quickly:

```bash
python manage.py shell

# Create multiple job seekers
from accounts.models import User, JobSeeker
user1 = User.objects.create_user('seeker1', 'seeker1@test.com', 'pass123', role='job_seeker')
JobSeeker.objects.create(user=user1, location='Kathmandu', skills='Python')

user2 = User.objects.create_user('seeker2', 'seeker2@test.com', 'pass123', role='job_seeker')
JobSeeker.objects.create(user=user2, location='Pokhara', skills='JavaScript')

# Create multiple companies
from companies.models import Company
user3 = User.objects.create_user('company1', 'company1@test.com', 'pass123', role='company')
Company.objects.create(user=user3, company_name='Company A', industry='Tech', location='Kathmandu', description='Tech company')

user4 = User.objects.create_user('company2', 'company2@test.com', 'pass123', role='company')
Company.objects.create(user=user4, company_name='Company B', industry='Finance', location='Pokhara', description='Finance company')

# Exit shell
exit()
```

---

## Performance Notes

- Admin pages paginate at 20 items per page
- Dashboard pages paginate at 10 items per page
- Search is case-insensitive
- Filters are additive (search AND role filter)

---

**Last Updated:** December 1, 2025
**Test Status:** Ready for Comprehensive Testing
