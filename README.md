# 📝 QA Python To-Do List

A personal To-Do List web application built with Flask following clean architecture principles.

This project was created as part of my Python backend learning path to practice object-oriented programming, CRUD operations, Flask routing, persistent storage, Git workflow, and clean project organization.

## 📸 Screenshots

### Home

![Home](docs/images/home.png)

---

### Creating a Task

![Create Task](docs/images/create-task.png)

---

### Completed Tasks

![Completed Task](docs/images/completed-task.png)

---

### Mobile View

![Mobile](docs/images/mobile.png)


## ✨ Features

- Create new tasks
- Mark tasks as completed
- Restore completed tasks
- Delete tasks
- Persistent JSON storage
- Responsive layout
- Clean and modern UI
- Task counter

## 🛠 Tech Stack

- Python 3
- Flask
- HTML5
- CSS3
- Jinja2
- JSON
- Lucide Icons

qa-python-to-do-list/

│

├── models/

│ ├── task.py

│ └── task_manager.py

│

├── routes/

│ └── web.py

│

├── services/

│ └── storage.py

│

├── templates/

│ ├── base.html

│ └── index.html

│

├── static/

│ ├── css/

│ └── js/

│

├── data/

│ └── tasks.json

│

├── app.py

└── requirements.txt


## 🚀 Getting Started

### Clone repository

```bash
git clone <repository-url>

### Install dependencies
```bash
pip install -r requirements.txt

### Run
```bash
python app.py

Application will be available at: 
http://127.0.0.1:5000


---


```markdown
## 📌 Roadmap

### Completed

- [x] Task model
- [x] Task manager
- [x] JSON storage
- [x] Flask routes
- [x] CRUD operations
- [x] Responsive UI
- [x] Task counter

### Backlog

- [ ] SQLite support
- [ ] Docker
- [ ] REST API
- [ ] Search tasks
- [ ] Task filters
- [ ] Categories
- [ ] Due dates
- [ ] Dark mode
- [ ] AJAX (Fetch API)
- [ ] Toast notifications
- [ ] Unit tests
- [ ] GitHub Actions

## 📚 What I Learned

During this project I practiced:

- Object-Oriented Programming
- Flask application structure
- CRUD operations
- JSON persistence
- Clean Architecture
- Git workflow
- Responsive CSS
- Jinja2 templates

## 👨‍💻 Author

Julio Soto


---

## 🛤️ Development Journey

This project was intentionally developed in small, incremental phases instead of building everything at once. The goal was not only to create a functional application, but also to practice software architecture, clean code, and Git workflow following a structured development process.

### Phase 1 – Project Setup

- Designed the project architecture
- Created the initial folder structure
- Configured the Python virtual environment
- Initialized the Git repository

---

### Phase 2 – Domain Model

- Implemented the `Task` class
- Applied Object-Oriented Programming principles
- Added serialization (`to_dict` / `from_dict`)
- Tested the model independently

---

### Phase 3 – Business Logic

- Implemented the `TaskManager`
- Added CRUD operations
- Created temporary validation scripts
- Improved code organization

---

### Phase 4 – Persistence Layer

- Designed the `Storage` service
- Implemented JSON persistence
- Loaded and saved tasks automatically
- Prepared the project for future storage providers

---

### Phase 5 – Flask Application

- Created the application entry point
- Added Blueprints
- Connected backend services
- Implemented HTML rendering with Jinja2

---

### Phase 6 – CRUD Features

- Created task creation form
- Added task completion toggle
- Implemented task deletion
- Connected all actions with persistent storage

---

### Phase 7 – UI / UX

- Redesigned the interface
- Added responsive layout
- Improved spacing and typography
- Integrated Lucide icons
- Added task statistics
- Enhanced user experience

---

### Phase 8 – Documentation

- Created a complete README
- Added screenshots
- Documented the architecture
- Defined the project roadmap
- Organized future improvements into a backlog

---

This phased approach allowed the project to evolve in a controlled manner while keeping the codebase clean, maintainable, and easy to extend.