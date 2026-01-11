# Blog Management System 📝

A **Django-based Blog Management System** that allows users to create, manage, and view blog posts. This project is designed to demonstrate Django fundamentals such as models, views, templates, authentication, and admin management.

---

## 🚀 Features

- User authentication (Login / Logout)
- Create, edit, and delete blog posts
- View blog posts
- Admin dashboard for managing posts
- Responsive templates
- Django admin integration

---

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

Blog_management/
├── manage.py
├── Blog_management/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── templates/
├── static/
├── apps/
├── db.sqlite3
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

Follow the steps below to run the project locally.

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/Blog_management.git
cd Blog_management
2️⃣ Create and activate virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install django
4️⃣ Apply migrations
bash
Copy code
python manage.py migrate
5️⃣ Create superuser (optional)
bash
Copy code
python manage.py createsuperuser
6️⃣ Run the development server
bash
Copy code
python manage.py runserver
Open your browser and visit:

cpp
Copy code
http://127.0.0.1:8000/
🔐 Admin Panel
Access the Django admin panel at:

arduino
Copy code
http://127.0.0.1:8000/admin/
📌 Future Enhancements
User registration

Comments on blog posts

Like and share features

Pagination and search

Rich text editor

👨‍💻 Author
Yash

📜 License
This project is intended for learning and educational purposes.

yaml
Copy code

---

### ✅ Optional (Highly Recommended)
Create a `requirements.txt` file:
```bash
pip freeze > requirements.txt
