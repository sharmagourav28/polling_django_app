# 🗳️ Polling Django Project

A simple Django-based web application that allows users to create polls, vote on them, and view real-time results. This project will be built step-by-step over 10 days. This README documents the progress and setup done on **Day 1**.

---

## 📅 Day 1: Project Setup & App Initialization

### ✅ Goals

- pip install django
- Created venv for the project and activate the venv
- Install Django on the virtual project
- Set up the Django project and app
- created the required project folder's for the project
- Set up basic routing and verify the server runs

## 📅 Day 2: Day 2: Design Models (Poll & Option)

### ✅ Goals

- pip install mysqlclient
- Create Poll model with question, created_by(FK), created_at,start_time,end_time
- Create Option model with option_text, votes, poll (FK)
- Create database in mysql polling
- Create model relationships
- Register models in admin
- Run migrations: makemigrations + migrate
- created admin (superuser) and set userid & password
