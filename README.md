# 🎓 Contri Tracker

> A powerful **dual-portal academic project management system** — built for teachers to manage and students to collaborate seamlessly.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-5.2-green?style=flat-square&logo=django)
![DRF](https://img.shields.io/badge/REST_API-DRF-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 📌 Overview

**Contri Tracker** solves a real problem in academic institutions — the lack of a structured system for managing student projects. Built as a full-stack web platform, it bridges the gap between teachers and students by providing dedicated portals for each role.

Teachers get complete control to create projects, assign tasks, and track every student's contribution. Students get a clean workspace to join projects, collaborate in groups, submit work, and evaluate peers — making the entire academic project lifecycle transparent, organized, and efficient.

---

## ✨ Features

### 🎓 Teacher Portal
* Create and manage academic projects
* Generate unique join codes for students
* Assign tasks to student groups with deadlines
* Monitor submissions and progress in real-time
* Post project-level announcements

### 📚 Student Portal
* Join projects via unique 8-character code
* Create and manage groups within projects
* Track assigned tasks and deadlines
* Submit individual work and final project files
* Rate team members (contribution, communication, collaboration)
* View personal progress dashboard

### 🔌 REST API
* Full RESTful API built with Django REST Framework
* Endpoints for Projects, Tasks, and Groups
* Clean JSON response format
* Authentication-ready endpoints

### 🔐 Authentication System
* Separate login/register for Teachers and Students
* Role-based access control
* Secure session management

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django 5.2, Python 3.10+ |
| REST API | Django REST Framework |
| Database | SQLite |
| Static Files | Whitenoise |
| Frontend | HTML, CSS, JavaScript |

---

## ⚙️ Installation & Setup

**1️⃣ Clone the repository**
```bash
git clone https://github.com/01-Harshit/Contri-tracker.git
cd Contri-tracker
```

**2️⃣ Create virtual environment**
```bash
python -m venv venv
```

**👉 Activate environment**

Windows:
```bash
venv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

**4️⃣ Add rest_framework to INSTALLED_APPS in settings.py**
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'core',
]
```

**5️⃣ Run migrations**
```bash
python manage.py migrate
```

**6️⃣ Collect static files**
```bash
python manage.py collectstatic
```

**7️⃣ Create superuser (admin)**
```bash
python manage.py createsuperuser
```

**8️⃣ Start server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser 🚀

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/projects/` | List all projects |
| POST | `/api/projects/` | Create a new project |
| GET | `/api/projects/<id>/` | Get project details |
| PUT | `/api/projects/<id>/` | Update a project |
| DELETE | `/api/projects/<id>/` | Delete a project |
| GET | `/api/tasks/` | List all tasks |

---

## 📂 Project Structure

```
Contri-Tracker/
├── contritracker/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                   # Main application
│   ├── models.py           # Database models
│   ├── views_teacher.py    # Teacher portal views
│   ├── views_student.py    # Student portal views
│   ├── api_views.py        # REST API views
│   ├── serializers.py      # DRF serializers
│   └── forms.py
├── templates/              # HTML templates
│   ├── teacher/
│   └── student/
├── static/                 # CSS, JS, assets
├── requirements.txt
└── manage.py
```

---

## 💡 Key Highlights

* Full-stack Django project with REST API
* Dual portal system — separate dashboards for Teachers & Students
* Unique join code system for project enrollment
* Peer rating system for team contribution tracking
* Real-world academic problem solving application

---

## 📸 Screenshots

### 🏠 Home Page
<img width="1366" height="1594" alt="home" src="https://github.com/user-attachments/assets/7d6cda5b-b1ab-4f34-8b11-f2e8a151ce00" />


### 🎓 Teacher Registration & Login
![Teacher Register](screenshot_link_yahan)
![Uploading techlogin.png…]()


### 🎓 Teacher Dashboard
![Teacher Dashboard](screenshot_link_yahan)

### 📋 Project Detail (Teacher View)
![Project Detail](screenshot_link_yahan)

### ✅ Task Management
![Task Management](screenshot_link_yahan)

### 📚 Student Registration & Login
![Student Register](screenshot_link_yahan)
![Student Login](screenshot_link_yahan)

### 📚 Student Dashboard
![Student Dashboard](screenshot_link_yahan)

### 📁 File Submission
![File Submission](screenshot_link_yahan)

### ⭐ Team Rating
![Team Rating](screenshot_link_yahan)

### 🔌 REST API
![REST API](screenshot_link_yahan)

---

## 🔮 Future Enhancements

* 🔔 Real-time notifications
* 💬 WebSocket-based live chat
* 📊 Analytics dashboard for teachers
* 📲 Mobile app version
* ☁️ Full cloud deployment

---

## 👨‍💻 Author

**Harshit Pandey**

* 2nd Year CSE Student
* Passionate about Backend Development & Problem Solving
* Building real-world projects to grow 🚀

---

⭐ If you like this project, consider giving it a **Star** on GitHub!
