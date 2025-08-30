# studymate
# 📚 StudyMate API

A backend API built with **Django REST Framework** that helps students collaborate through study groups, tutoring sessions, file sharing, and messaging.

This project was developed as part of my backend development program to demonstrate authentication, permissions, and RESTful API design.

---

## 🚀 Features

* **User Authentication**

  * JWT-based authentication for secure access.
  * Only authenticated users can create, update, or delete data.

* **Study Groups**

  * Create, view, update, and delete study groups.
  * Join/leave groups with dedicated endpoints.
  * Only group creators can delete groups.

* **Group Messages**

  * Post and view messages within groups.
  * Only group members can send messages.
  * Validation ensures content and membership rules are respected.

* **Notes Upload**

  * Upload study notes as files.
  * Notes are linked to the uploading user.
  * Validation prevents missing or invalid uploads.

* **Tutoring Sessions**

  * Schedule, update, and cancel tutoring sessions.
  * Session status tracked with choices (`scheduled`, `completed`, `cancelled`).

* **Profiles**

  * Each user has a profile with optional fields like availability times.

* **Validation & Permissions**

  * Strict input validation on required fields.
  * Role-based restrictions (e.g., only group members can post messages).

---

## 📡 API Documentation

### Authentication

**Register User**
`POST /api/accounts/register/`

```json
{
  "username": "Stella",
  "email": "stella@example.com",
  "password": "password123"
}
```

**Get JWT Token**
`POST /api/accounts/token/`

```json
{
  "username": "stella",
  "password": "password123"
}
```

**Response:**

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}
```

---

### Study Groups

**List Groups**
`GET /api/groups/groups/`

**Response:**

```json
[
  {
    "id": 1,
    "name": "Algebra Study Group",
    "subject": "Math",
    "created_by": 1,
    "members": [1, 2]
  }
]
```

**Create Group**
`POST /api/groups/groups/`

```json
{
  "name": "Swahili Enthusiasts",
  "subject": "swahili"
}
```

**Join Group**
`POST /api/groups/groups/{id}/join/`

**Response:**

```json
{
  "detail": "Joined group successfully"
}
```

**Leave Group**
`POST /api/groups/groups/{id}/leave/`

**Response:**

```json
{
  "detail": "Left group successfully"
}
```

---

### Messages

**Post Message**
`POST /api/groups/messages/`

```json
{
  "group": 7,
  "content": "Hey team, shall we revise chapter 5 tomorrow?"
}
```

**Response:**

```json
{
  "id": 1,
  "group": 1,
  "sender": 1,
  "content": "Hey team, shall we revise chapter 5 tomorrow?",
  "timestamp": "2025-08-29T11:30:00Z"
}
```

**List Messages (Group 1)**
`GET /api/groups/messages/?group=1`

---

### Notes

**Upload Note**
`POST /api/notes/notes/` (form-data)

| Key         | Value                | Type |
| ----------- | -------------------- | ---- |
| file        | algebra\_notes.pdf   | File |
| title       | Algebra Chapter 3    | Text |
| description | Key formulas summary | Text |

**Response:**

```json
{
  "id": 5,
  "title": "Algebra Chapter 3",
  "description": "Key formulas summary",
  "file": "http://127.0.0.1:8000/media/notes/algebra_notes.pdf",
  "uploaded_by": 1,
  "uploaded_at": "2025-08-29T12:15:00Z"
}
```

---

### Tutoring

**Create Session**
`POST /api/tutoring/sessions/`

```json
{
  
  "subject": "Calculus Basics",
  "date_time": "2025-09-05T14:00:00Z",
  "status": "scheduled",
  "tutor": 1,
  "student": 3

}
```

**Response:**

```json
{
  
  "subject": "Calculus Basics",
  "date_time": "2025-09-05T14:00:00Z",
  "status": "scheduled",
  "tutor": 1,
  "student": 3,
  "created_by": 1
}
```

---

### Profiles

**Get Profile**
`GET /api/accounts/profiles/1/`

**Response:**

```json
{
  "id": 1,
  "user": "student1",
  "bio": "Math enthusiast",
  "available_times": "Weekdays after 5PM"
}
```

**Update Profile**
`PATCH /api/accounts/profiles/1/`

```json
{
  "available_times": "Weekends only"
}
```

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** SQLite (for development)
* **Auth:** JWT via `djangorestframework-simplejwt`
* **Deployment:** (Planned) Heroku or PythonAnywhere

---

## 📋 Next Steps

* Add pagination & filters for large datasets (e.g., groups, sessions, notes).
* Polish API documentation with more examples.
* Deploy publicly for testing.
* Final round of testing with multiple roles.

---

## 📽️ Demo

* A Loom demo walkthrough is included in this repository.
* The demo covers authentication, group management, messaging, notes, and tutoring sessions.

---

## 🔗 Links

* **GitHub Repo:** \(https://github.com/nafulacindy/studymate.git)
* **Demo Video:** \(https://www.loom.com/share/91710068d86749518ef13b6ddc1bcb61?sid=d61c9770-b6a9-4447-b3d0-cb42dfe0b6f6)

* **Live Demo:**
The project is deployed and can be accessed here: [StudyMate Live](https://studymate-ehuh.onrender.com/)

You can test the APIs directly via the live endpoints, for example:

- **Register:** `POST /api/accounts/register/`
- **Obtain Token:** `POST /api/accounts/token/`
- **Refresh Token:** `POST /api/accounts/token/refresh/`
- **Groups API:** `GET /api/groups/groups/`  *(requires authentication)*

---

✨ Built with ❤️ using Django REST Framework.

---
