# UML Diagrams - Elevate Workforce Solutions

## Table of Contents
1. [Class Diagram](#class-diagram)
2. [Entity Relationship Diagram](#entity-relationship-diagram)
3. [Use Case Diagram](#use-case-diagram)
4. [Sequence Diagrams](#sequence-diagrams)

---

## Class Diagram

### Overview
The application follows an object-oriented design with clear separation of concerns.

```
┌─────────────────────────────────────────────────────────────────────┐
│                          CLASSES HIERARCHY                         │
└─────────────────────────────────────────────────────────────────────┘

                        ┌──────────────────┐
                        │   AbstractUser   │ (Django built-in)
                        │   (from Django)  │
                        └────────┬─────────┘
                                 │
                                 │ extends
                                 ▼
                        ┌──────────────────────────────┐
                        │         User                │
                        ├──────────────────────────────┤
                        │ Attributes:                  │
                        │ - username: str              │
                        │ - email: str                 │
                        │ - password: str (hashed)     │
                        │ - first_name: str            │
                        │ - last_name: str             │
                        │ - phone_number: str [0..1]   │
                        │ - role: str (job_seeker|...) │
                        │ - is_active: bool            │
                        │ - created_at: datetime       │
                        │ - updated_at: datetime       │
                        ├──────────────────────────────┤
                        │ Methods:                     │
                        │ + is_company(): bool         │
                        │ + is_job_seeker(): bool      │
                        │ + __str__(): str             │
                        └────────┬─────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │ has_one                │ has_one
                    ▼                        ▼
        ┌──────────────────────┐  ┌──────────────────────┐
        │    JobSeeker         │  │    Company           │
        ├──────────────────────┤  ├──────────────────────┤
        │ Attributes:          │  │ Attributes:          │
        │ - user: User [1]     │  │ - user: User [1]     │
        │ - bio: str           │  │ - company_name: str  │
        │ - resume: File       │  │ - description: str   │
        │ - skills: str        │  │ - website: URL       │
        │ - experience_years:  │  │ - industry: str      │
        │   int                │  │ - location: str      │
        │ - location: str      │  │ - company_size: str  │
        │ - profile_picture:   │  │ - logo: Image        │
        │   Image              │  │ - status: str        │
        │ - created_at:        │  │ - verified: bool     │
        │   datetime           │  │ - created_at:        │
        │ - updated_at:        │  │   datetime           │
        │   datetime           │  │ - updated_at:        │
        ├──────────────────────┤  │   datetime           │
        │ Methods:             │  ├──────────────────────┤
        │ + get_skills_list(): │  │ Methods:             │
        │   List[str]          │  │ + is_active_..():    │
        │ + __str__(): str     │  │   bool               │
        └──────────────────────┘  │ + get_total_jobs..:  │
                                   │   int                │
                                   │ + get_active_jobs(): │
                                   │   Query              │
                                   │ + __str__(): str     │
                                   └──────┬───────────────┘
                                          │
                                          │ posts (ForeignKey)
                                          ▼
                                   ┌──────────────────────────┐
                                   │        Job               │
                                   ├──────────────────────────┤
                                   │ Attributes:              │
                                   │ - company: Company [1]   │
                                   │ - title: str             │
                                   │ - description: str       │
                                   │ - requirements: str      │
                                   │ - location: str          │
                                   │ - salary_min: decimal    │
                                   │ - salary_max: decimal    │
                                   │ - job_type: str          │
                                   │ - experience_level: str  │
                                   │ - is_active: bool        │
                                   │ - posted_at: datetime    │
                                   │ - updated_at: datetime   │
                                   │ - deadline: datetime     │
                                   │ - total_positions: int   │
                                   ├──────────────────────────┤
                                   │ Methods:                 │
                                   │ + is_application_...():  │
                                   │   bool                   │
                                   │ + get_salary_range():    │
                                   │   str                    │
                                   │ + get_requirements_...():│
                                   │   List[str]              │
                                   │ + get_total_...():       │
                                   │   int                    │
                                   │ + __str__(): str         │
                                   └──────┬──────────────────┘
                                          │
                                          │ has_many (ForeignKey)
                                          ▼
                                   ┌──────────────────────────┐
                                   │   JobApplication         │
                                   ├──────────────────────────┤
                                   │ Attributes:              │
                                   │ - job: Job [1]           │
                                   │ - job_seeker:            │
                                   │   JobSeeker [1]          │
                                   │ - status: str            │
                                   │ - cover_letter: str      │
                                   │ - applied_at: datetime   │
                                   │ - updated_at: datetime   │
                                   ├──────────────────────────┤
                                   │ Methods:                 │
                                   │ + get_status_badge...(): │
                                   │   str                    │
                                   │ + can_be_withdrawn():    │
                                   │   bool                   │
                                   │ + get_days_since_...():  │
                                   │   int                    │
                                   │ + __str__(): str         │
                                   └──────────────────────────┘
```

---

## Entity Relationship Diagram

### ER Diagram (Chen Notation)

```
                                    ┌─────────────────┐
                                    │      User       │
                                    ├─────────────────┤
                            ┌───────┤ username (PK)   │◄─────┐
                            │       │ email           │      │
                            │       │ password        │      │
                            │       │ phone_number    │      │
                            │       │ role            │      │
                            │       │ is_active       │      │
                            │       │ created_at      │      │
                            │       │ updated_at      │      │
                            │       └────────┬────────┘      │
                            │              │                │
                            │ 1 ┌──────────┴─────────┐ 1     │
                            │   │                   │       │
                            ▼   ▼                   ▼       │
                    ┌──────────────────┐    ┌──────────────┐ │
                    │   JobSeeker      │    │  Company     │ │
                    ├──────────────────┤    ├──────────────┤ │
                    │ user_id (FK,PK)  │    │ user_id      │ │
                    │ bio              │    │ (FK,PK)      │ │
                    │ resume           │    │ company_name │ │
                    │ skills           │    │ description  │ │
                    │ experience_years │    │ website      │ │
                    │ location         │    │ industry     │ │
                    │ profile_picture  │    │ location     │ │
                    └──────┬───────────┘    │ company_size │ │
                           │                │ logo         │ │
                           │                │ status       │ │
                           │                │ verified     │ │
                           │                └──────┬───────┘ │
                           │                       │         │
                           │                 1 ┌───┴─────────┤
                           │                   │ creates    │
                           │                   │ (FK)       │
                           │                   ▼            │
                           │            ┌──────────────┐    │
                           │            │     Job      │    │
                           │            ├──────────────┤    │
                           │            │ job_id (PK)  │    │
                           │            │ company_id   │    │
                           │            │ title        │    │
                           │            │ description  │    │
                           │            │ requirements │    │
                           │            │ location     │    │
                           │            │ salary_min   │    │
                           │            │ salary_max   │    │
                           │            │ job_type     │    │
                           │            │ experience.. │    │
                           │            │ is_active    │    │
                           │            │ posted_at    │    │
                           │            │ updated_at   │    │
                           │            │ deadline     │    │
                           │            │ total_..     │    │
                           │            └──────┬───────┘    │
                           │                   │            │
                           │   applies N ┌─────┴─────┐ 1    │
                           │   to        │           │      │
                           │   ┌─────────┴────┐      │      │
                           │   │              │      │      │
                           │   ▼              ▼      ▼      │
                           │ ┌──────────────────────┐       │
                           └─┤ JobApplication      │       │
                             ├──────────────────────┤       │
                             │ app_id (PK)          │       │
                             │ job_id (FK)          │       │
                             │ job_seeker_id (FK)   │       │
                             │ status               │       │
                             │ cover_letter         │       │
                             │ applied_at           │       │
                             │ updated_at           │       │
                             └──────────────────────┘       │
                                                            │
                                                   (user_id) │
                                                            │
                                                            ▼
                                        (link back to User entity)
```

### Relationships Summary

| Relationship | From | To | Type | Cardinality |
|---|---|---|---|---|
| Profile | User | JobSeeker | OneToOne | 1:1 |
| Profile | User | Company | OneToOne | 1:1 |
| Posts | Company | Job | OneToMany | 1:N |
| Applies | JobSeeker | JobApplication | OneToMany | 1:N |
| For | Job | JobApplication | OneToMany | 1:N |

---

## Use Case Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ELEVATE WORKFORCE SYSTEM                        │
│                                                                      │
│                    ┌─────────────────────┐                          │
│                    │   Job Seeker User   │                          │
│                    └──────────┬──────────┘                          │
│                               │                                     │
│                ┌──────────────┼──────────────┐                      │
│                ▼              ▼              ▼                      │
│          ┌──────────┐  ┌────────────┐ ┌───────────┐               │
│          │Register  │  │   Login    │ │  Logout   │               │
│          └──────────┘  └────────────┘ └───────────┘               │
│                │              │              │                     │
│                └──────────────┬──────────────┘                      │
│                               │                                     │
│                ┌──────────────┴──────────────┐                      │
│                ▼                             ▼                      │
│        ┌──────────────┐            ┌──────────────────┐            │
│        │Browse Jobs   │            │View My Profile   │            │
│        └──────┬───────┘            └──────────────────┘            │
│               │                                                     │
│        ┌──────┴─────────────────┐                                  │
│        ▼                        ▼                                  │
│  ┌──────────────┐      ┌─────────────────┐                        │
│  │ Search/Filter│      │ View Job Detail │                        │
│  └──────────────┘      └─────────┬───────┘                        │
│                                  │                                 │
│                   ┌──────────────┴──────────────┐                  │
│                   ▼                             ▼                  │
│            ┌──────────────┐        ┌────────────────────┐          │
│            │   Apply Job  │        │ Update Profile     │          │
│            └──────┬───────┘        └────────────────────┘          │
│                   │                                                │
│                   ▼                                                │
│            ┌──────────────────┐                                    │
│            │ View Applications │                                   │
│            │ & Track Status    │                                   │
│            └──────────────────┘                                    │
│                                                                    │
│                                                                    │
│                    ┌─────────────────────┐                        │
│                    │   Company User      │                        │
│                    └──────────┬──────────┘                        │
│                               │                                   │
│                ┌──────────────┼──────────────┐                    │
│                ▼              ▼              ▼                    │
│          ┌──────────┐  ┌────────────┐ ┌───────────┐             │
│          │Register  │  │   Login    │ │  Logout   │             │
│          └──────────┘  └────────────┘ └───────────┘             │
│                │              │              │                   │
│                └──────────────┬──────────────┘                    │
│                               │                                   │
│        ┌──────────────────────┴────────────────────────┐          │
│        ▼                      ▼                        ▼          │
│  ┌──────────────┐      ┌──────────────┐     ┌────────────────┐ │
│  │View Dashboard│      │  Post Job    │     │ View My Profile │ │
│  └──────┬───────┘      └──────┬───────┘     └────────────────┘ │
│         │                     │                                  │
│    ┌────┴──────────┐          │                                  │
│    ▼               ▼          ▼                                  │
│ ┌──────────┐  ┌──────────┐ ┌──────────────┐                     │
│ │View Stats│  │Edit Job  │ │Update Profile│                     │
│ └──────────┘  └─────┬────┘ └──────────────┘                     │
│                     │                                            │
│                ┌────┴────────────┐                               │
│                ▼                 ▼                               │
│           ┌──────────┐    ┌───────────────┐                     │
│           │Delete Job│    │Toggle Status  │                     │
│           └──────────┘    └───────────────┘                     │
│                                                                 │
│        ┌────────────────────────────────────┐                   │
│        ▼                                    ▼                   │
│  ┌───────────────┐              ┌────────────────────┐          │
│  │View Applications              View Application Detail          │
│  │& Applications Statistics      & Update Status    │          │
│  └───────────────┘              └────────────────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Sequence Diagrams

### 1. Job Seeker Registration and Job Search Flow

```
Job Seeker         Web App              Django Views          Database
    │                  │                      │                   │
    │─ Register ──────>│                      │                   │
    │                  │─ POST /register ────>│                   │
    │                  │                      │─ Create User ────>│
    │                  │                      │                   │
    │                  │                      │<─ User Created ───│
    │                  │                      │                   │
    │                  │<─ Redirect to Home ──│                   │
    │<─ Registered ────│                      │                   │
    │                  │                      │                   │
    │─ Login ─────────>│                      │                   │
    │                  │─ POST /login ───────>│                   │
    │                  │                      │─ Authenticate ───>│
    │                  │                      │                   │
    │                  │<─ Session Created ───│                   │
    │<─ Logged In ─────│                      │                   │
    │                  │                      │                   │
    │─ Browse Jobs ───>│                      │                   │
    │                  │─ GET /jobs/ ────────>│                   │
    │                  │                      │─ Query Jobs ─────>│
    │                  │                      │                   │
    │                  │<─ Render Job List ───│<─ Active Jobs ───│
    │<─ Job List ──────│                      │                   │
    │                  │                      │                   │
    │─ Search/Filter ─>│                      │                   │
    │                  │─ GET /jobs/?filter ─>│                   │
    │                  │                      │─ Query Filtered ─>│
    │                  │                      │                   │
    │<─ Filtered List ─│<─ Render Results ────│<─ Results ───────│
```

### 2. Job Application Flow

```
Job Seeker         Web App              Django Views          Database
    │                  │                      │                   │
    │─ View Job ──────>│                      │                   │
    │                  │─ GET /jobs/<id> ───>│                   │
    │                  │                      │─ Query Job ──────>│
    │                  │                      │                   │
    │<─ Job Details ───│<─ Render Job ────────│<─ Job Details ───│
    │                  │                      │                   │
    │─ Apply Job ──────>│                      │                   │
    │                  │─ GET /apply/<id> ───>│                   │
    │                  │                      │─ Render Form ────>
    │<─ Application ───│<─ Show Form ─────────│                   │
    │   Form           │                      │                   │
    │                  │                      │                   │
    │─ Fill Cover ─────>│                      │                   │
    │   Letter & Submit │                      │                   │
    │                  │─ POST /apply/<id> ──>│                   │
    │                  │                      │─ Validate Data ──>
    │                  │                      │                   │
    │                  │                      │─ Create ─────────>│
    │                  │                      │   Application     │
    │                  │                      │                   │
    │                  │<─ Redirect Success ──│<─ Applied OK ─────│
    │<─ Success ───────│                      │                   │
    │   Message        │                      │                   │
    │                  │                      │                   │
    │─ View Status ───>│                      │                   │
    │                  │─ GET /my-apps ──────>│                   │
    │                  │                      │─ Query Apps ─────>│
    │                  │                      │                   │
    │<─ Applications ──│<─ Render List ───────│<─ Applications ───│
    │   List           │                      │                   │
```

### 3. Company Job Posting and Application Review Flow

```
Company User       Web App              Django Views          Database
    │                  │                      │                   │
    │─ Login ─────────>│                      │                   │
    │                  │─ POST /login ───────>│                   │
    │                  │                      │─ Authenticate ───>│
    │                  │                      │                   │
    │<─ Logged In ─────│<─ Session Created ───│                   │
    │                  │                      │                   │
    │─ Dashboard ──────>│                      │                   │
    │                  │─ GET /dashboard ────>│                   │
    │                  │                      │─ Query Stats ────>│
    │                  │                      │                   │
    │<─ Dashboard ─────│<─ Render Dashboard ──│<─ Stats Data ─────│
    │                  │                      │                   │
    │─ Post Job ───────>│                      │                   │
    │                  │─ GET /post-job ─────>│                   │
    │<─ Form ─────────>│<─ Render Form ───────│                   │
    │                  │                      │                   │
    │─ Fill & Submit ──>│                      │                   │
    │   Job Details    │                      │                   │
    │                  │─ POST /create-job ──>│                   │
    │                  │                      │─ Validate ───────>
    │                  │                      │                   │
    │                  │                      │─ Create Job ─────>│
    │                  │                      │                   │
    │<─ Success ───────│<─ Redirect Detail ───│<─ Job Created ────│
    │                  │                      │                   │
    │─ View Apps ──────>│                      │                   │
    │                  │─ GET /all-apps ─────>│                   │
    │                  │                      │─ Query Appls ────>│
    │                  │                      │                   │
    │<─ Applications ──│<─ Render List ───────│<─ Applications ───│
    │                  │                      │                   │
    │─ Update Status ──>│                      │                   │
    │                  │─ POST /update-stat ─>│                   │
    │                  │                      │─ Update App ─────>│
    │                  │                      │                   │
    │<─ Updated ───────│<─ Success Message ───│<─ Updated OK ─────│
```

---

## State Diagram for JobApplication

```
                              ┌─────────────┐
                              │   PENDING   │ (Initial state)
                              │ New app rec │
                              └──────┬──────┘
                                     │
                           Review    │
                         Application │
                                     ▼
                              ┌─────────────┐
                              │   REVIEWED  │
                              └──────┬──────┘
                                     │
                        ┌────────────┴─────────────┐
                        │                          │
                   Shortlist            Reject
                        │                │
                        ▼                ▼
                ┌─────────────┐  ┌─────────────┐
                │ SHORTLISTED │  │   REJECTED  │ (Terminal state)
                └──────┬──────┘  └─────────────┘
                       │
                    Hire │
                       │
                       ▼
                ┌─────────────┐
                │   ACCEPTED  │ (Terminal state)
                └─────────────┘

                Also possible:
                ┌─────────────┐
                │  WITHDRAWN  │ (Terminal state)
                └─────────────┘
                (Can withdraw from PENDING or REVIEWED states)
```

---

## Data Flow Diagram (DFD)

```
LEVEL 0 - CONTEXT DIAGRAM

                ┌───────────────┐
                │ Job Seeker    │
                │ User          │
                └───────┬───────┘
                        │
                   ┌────┴──────────┐
                   │               │
                   ▼               ▼
              ┌──────┐        ┌──────┐
              │ Jobs │        │ Apps │
              └──────┘        └──────┘
                   │               │
                   └────┬──────────┘
                        │
                ┌───────▼────────┐
                │  Elevate Job   │
                │  Portal System │
                └───────┬────────┘
                        │
                   ┌────┴──────────┐
                   │               │
                   ▼               ▼
              ┌──────┐        ┌──────┐
              │ Jobs │        │ Apps │
              └──────┘        └──────┘
                   │               │
                   └────┬──────────┘
                        │
                ┌───────▼────────┐
                │  Company User  │
                └────────────────┘
```

---

**Document Generated**: November 29, 2025
**Version**: 1.0
