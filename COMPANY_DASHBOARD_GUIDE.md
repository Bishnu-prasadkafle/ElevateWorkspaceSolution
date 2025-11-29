# Company Dashboard & Job Management Workflow

## 📊 Company Dashboard Overview

**URL:** `http://127.0.0.1:8000/applications/company/dashboard/`

After logging in as a company, you land on this dashboard with everything you need to manage jobs and applications.

---

## Dashboard Layout

### 1️⃣ Header Section
```
┌─────────────────────────────────────────────┐
│  Dashboard - [Company Name]  | Post New Job │
└─────────────────────────────────────────────┘
```
- **Left:** Shows your company name
- **Right:** Green "Post New Job" button → goes to `/jobs/create/`

---

### 2️⃣ Statistics Cards (4 Cards)

#### Card 1: Total Jobs
- Shows total number of jobs you posted
- Shows how many are currently active

#### Card 2: Total Applications
- Shows total applications received from all your jobs
- Shows how many are still pending

#### Card 3: Company Status
- Shows if company is "Verified" or "Pending"
- Only unverified companies show "Pending"

#### Card 4: Profile
- "Edit" button to update company details
- Links to: `/accounts/profile/edit/`

---

### 3️⃣ Your Jobs Section (Left Side)

**Shows:** Your 5 most recent jobs

**Each job displays:**
- Job title (clickable link)
- Active/Inactive status badge
- Number of applications received

**What you can do:**
- Click job title → See full job details page
- On detail page → Edit, Delete, or Activate/Deactivate
- View applications for that specific job

---

### 4️⃣ Application Status Breakdown (Right Side)

**Shows stats for applications:**
- Pending
- Reviewed
- Shortlisted
- Accepted
- Rejected

Each displayed as a colored box with count.

---

### 5️⃣ All Applications Table (Bottom)

**Lists all applications** received for any of your jobs.

**Columns:**
| Column | What it shows |
|--------|--------------|
| **Applicant** | Name and email of job seeker |
| **Job Position** | Which job they applied for |
| **Applied** | When they applied (date and days ago) |
| **Status** | Color-coded badge (Pending, Reviewed, etc.) |
| **Action** | "View" button |

**Features:**
- **Filter by Status:** Top right dropdown to show only specific status
- **Pagination:** If you have 10+ applications, pages appear at bottom
- Shows 10 applications per page

---

## 🔧 Job Management Workflow

### Step A: POST A NEW JOB

**Two entry points:**
1. Click green "**Post New Job**" button on dashboard
2. Or from navbar when logged in as company

**Goes to:** `/jobs/create/`

**Form Fields:**
```
Required (*):
  - Job Title
  - Job Description
  - Job Type (dropdown)
  - Experience Level (dropdown)
  - Location
  - Requirements (text, one per line)

Optional:
  - Number of Positions
  - Minimum Salary
  - Maximum Salary
  - Application Deadline
```

**After Submit:**
- ✅ Job created and visible to job seekers
- ✅ Redirected to job detail page
- ✅ Application count shows "0"
- ✅ Status is "Active"

---

### Step B: EDIT AN EXISTING JOB

**How to reach:**
1. Go to Dashboard
2. Click on job title in "Your Jobs" section
3. Or visit `/jobs/[job-id]/`
4. As the company owner, you'll see "Edit Job" yellow button
5. Click it → goes to `/jobs/[job-id]/edit/`

**What you can change:**
- Title
- Description
- Requirements
- Location
- Job Type
- Experience Level
- Salary (min/max)
- Number of positions
- Application deadline

**After Save:**
- ✅ Job details updated
- ✅ All changes visible to new applicants
- ✅ Existing applications unchanged
- ✅ Redirected back to job detail

---

### Step C: DELETE A JOB

**How to reach:**
1. View job detail page (from dashboard or job list)
2. Click red "**Delete Job**" button
3. Browser asks for confirmation: "Are you sure?"
4. Click OK

**What happens:**
- ❌ Job is permanently removed
- ❌ All applications for this job are deleted
- ✅ Redirected back to company dashboard

**Note:** This is permanent! No undo.

---

### Step D: ACTIVATE/DEACTIVATE A JOB

**How to reach:**
1. View job detail page
2. Click blue "**Activate** / **Deactivate**" button
3. No confirmation needed - changes immediately

**States:**
- **Active (Green Badge)** → Visible to all job seekers in listings
- **Inactive (Gray Badge)** → Hidden from listings (but still accessible via direct link)

**Use case:**
- Deactivate when you've filled all positions
- Deactivate to pause hiring temporarily
- Reactivate when hiring resumes

---

## 📋 Application Management Workflow

### Step 1: VIEW APPLICATION LIST

**From dashboard:**
1. Scroll to bottom → "All Applications" table
2. See all applications from all your jobs
3. Filter by status using dropdown (top right)
4. Use pagination if more than 10

---

### Step 2: OPEN AN APPLICATION

**Click:**
- Green "**View**" button in the Action column

**Goes to:**
- `/applications/[app-id]/` (application detail page)

---

### Step 3: REVIEW APPLICATION DETAILS

**You will see:**

**Applicant Info:**
- Name and email
- Resume (if uploaded)
- Cover letter (if provided)
- Experience level
- Skills (if provided)

**Application Info:**
- Job position they applied for
- When they applied
- Current status

---

### Step 4: UPDATE APPLICATION STATUS

**Only as company (company owner):**

1. On application detail page
2. Look for "**Update Status**" section
3. Dropdown shows options:
   - Pending
   - Reviewed
   - Shortlisted
   - Rejected
   - Accepted
   - Withdrawn (applicant-only)

4. Select new status
5. Click "**Update**"
6. Status changes immediately

**Status Flow (Suggested):**
```
Received → Reviewed → Shortlisted → Accepted
                   ↓
                 Rejected
```

---

## 🎯 Best Practices

1. **Post Clear Requirements**
   - Be specific about what you're looking for
   - List skills/experience needed

2. **Set Application Deadlines**
   - Helps you manage applicant volume
   - Optional but recommended

3. **Review Applications Promptly**
   - Update status to "Reviewed" within 24 hours
   - Helps applicants know you've seen their application

4. **Communicate Clearly**
   - Use status updates to keep applicants informed
   - Only accept when you're ready to interview

5. **Archive/Deactivate When Full**
   - Deactivate jobs once positions are filled
   - Prevents job seekers from applying to closed positions

---

## ⚠️ Common Issues & Solutions

**Issue:** Can't see "Post Job" button in navbar
- **Solution:** Make sure you're logged in as a company user
- Job seekers don't see this button

**Issue:** After posting a job, it doesn't appear in job list
- **Solution:** Refresh page (Ctrl+R) or navigate to `/jobs/`
- Check if job status is "Active" (not "Inactive")

**Issue:** Can't edit/delete a job
- **Solution:** Only the company that posted the job can edit/delete
- If logged in as different company, you won't see those buttons

**Issue:** Applications not showing on dashboard
- **Solution:** Make sure job is "Active"
- Check the date range (past applications also show)

**Issue:** Can't update application status
- **Solution:** Only company owner can change status
- Job seekers can only view their own applications

---

## 📈 Workflow Summary

```
1. Register as Company
   ↓
2. Auto-login to Dashboard
   ↓
3. Click "Post New Job"
   ↓
4. Fill job form + Submit
   ↓
5. Job appears in listing
   ↓
6. Job seekers apply
   ↓
7. Go to Dashboard
   ↓
8. View all applications
   ↓
9. Click "View" on any application
   ↓
10. Update status (Reviewed → Shortlisted → Accepted)
   ↓
11. Interview and hire!
```

---

## 🔐 Permissions Summary

| Action | Company Owner | Other Company | Job Seeker |
|--------|---------------|--------------|-----------|
| Post Job | ✅ Yes | ❌ No | ❌ No |
| Edit Own Job | ✅ Yes | ❌ No | ❌ No |
| Delete Own Job | ✅ Yes | ❌ No | ❌ No |
| View Own Applications | ✅ Yes | ❌ No | ❌ No |
| Update App Status | ✅ Yes | ❌ No | ❌ No |
| Apply to Jobs | ❌ No | ❌ No | ✅ Yes |
| View Applications | ❌ No | ❌ No | ✅ Own only |
| Withdraw Application | ❌ No | ❌ No | ✅ Yes |

---

## 📞 Need Help?

- Check browser console: Press F12, look at "Console" tab
- Check server logs: Look at terminal where `runserver` runs
- See QUICK_START.md for step-by-step setup
- See README.md for technical details
