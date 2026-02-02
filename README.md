# 🎓 Student Nexus API

A powerful, high-performance backend built with **FastAPI** and **Firebase**. This API serves as the "brain" for a cross-platform productivity suite designed specifically for students to manage tasks, submissions, and collaborative group discussions.

## 🚀 Key Features

- **Infinite Nested Folders:** Organize your work with folders-inside-folders logic.
- **Task Management:** Create, update, and track "Tick/Untick" tasks.
- **Real-time Sync:** Powered by Firebase Firestore for instant updates across Web, Mobile, and Desktop.
- **Group Collaboration:** "Circles" feature for friend-group discussions and shared task folders.

## 🛠 Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Database & Auth:** [Firebase](https://firebase.google.com/) (Firestore)
- **Environment:** Python 3.10+
- **Validation:** Pydantic Models

## 📁 Project Structure

```text
student-nexus-api/
├── app/
│   ├── api/          # Route handlers
│   ├── models/       # Pydantic data schemas
│   ├── services/     # Firebase logic
│   └── main.py       # FastAPI entry point
├── .gitignore        # Security for private keys
├── requirements.txt  # Project dependencies
└── README.md         # Documentation
```
