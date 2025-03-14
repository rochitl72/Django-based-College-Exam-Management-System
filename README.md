📌 Django-based College Exam Management System
An API-driven system for managing college exams, user authentication, and role-based access control.
🚀 Project Overview
This project is a Django-based Exam Management System that provides API endpoints for managing users, authentication, and exam-related functionalities.

The system allows admin users to create and manage exams, while authenticated students can access exam details. The system uses JWT authentication for secure login and role-based permissions for different user types.

✨ Features Implemented
✔ User Registration & Authentication
✔ JWT-based Login System
✔ Admin Role for Exam Management
✔ CRUD Operations for Exams
✔ Role-Based Permissions
✔ Django Admin Panel for User Management
✔ RESTful API with Django Rest Framework
✔ Database Migrations & ORM Queries
✔ Git Version Control Setup

📂 Project Structure
bash
Copy
Edit
backend/
│── users/                 # User Authentication & Management
│   ├── models.py          # User model definitions
│   ├── views.py           # User API views
│   ├── serializers.py     # User data serialization
│   ├── urls.py            # User API routes
│
│── exams/                 # Exam Management Module
│   ├── models.py          # Exam model
│   ├── views.py           # Exam-related API views
│   ├── serializers.py     # Exam data serialization
│   ├── permissions.py     # Custom permissions for role-based access
│   ├── urls.py            # Exam API routes
│
│── printing/              # Printing Exam Papers (To be implemented)
│
│── backend/               # Project settings and configurations
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI configuration for deployment
│
│── db.sqlite3             # SQLite Database
│── manage.py              # Django command-line utility
│── requirements.txt       # Python dependencies
⚙️ Installation Guide
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/rochitl72/Django-based-College-Exam-Management-System.git
cd Django-based-College-Exam-Management-System/backend
2️⃣ Create a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Apply Database Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5️⃣ Create a Superuser
bash
Copy
Edit
python manage.py createsuperuser
(Follow the prompt to create an admin user)

6️⃣ Run the Development Server
bash
Copy
Edit
python manage.py runserver
Visit: http://127.0.0.1:8000/admin/ to access the Django Admin Panel.

🛠️ API Endpoints
🔹 User Authentication
Method	Endpoint	Description
POST	/api/users/register/	Register a new user
POST	/api/users/login/	Login and get JWT tokens
GET	/api/users/profile/	View authenticated user's profile
POST	/api/users/logout/	Logout and blacklist JWT token
🔹 Exam Management
Method	Endpoint	Description
GET	/api/exams/	List all exams
POST	/api/exams/	Create a new exam (Admin only)
GET	/api/exams/{id}/	Retrieve a specific exam
PUT	/api/exams/{id}/	Update exam details (Admin only)
DELETE	/api/exams/{id}/	Delete an exam (Admin only)
🛠️ Technologies Used
✅ Django – Web framework
✅ Django REST Framework (DRF) – API development
✅ PostgreSQL/SQLite – Database
✅ JWT Authentication – Secure login system
✅ Git & GitHub – Version control
✅ Django Admin Panel – User & data management

📌 What I Have Learned
✅ Setting up Django with REST APIs
✅ User authentication using JWT (JSON Web Tokens)
✅ Handling database migrations and ORM queries
✅ Role-based access control with custom permissions
✅ Building CRUD APIs for exam management
✅ Version control using Git & GitHub

🔜 Next Steps & Features to Implement
🚀 Upload & Analyze Question Papers
🚀 Error Detection in Exam Papers
🚀 Exam Paper Printing & Supply Chain System
🚀 Real-time Dashboard & Reporting
🚀 Deployment to Cloud (Heroku/Railway)

👨‍💻 Contributors
👤 @rochitl72 – Lead Developer

🔗 GitHub Repo: Django-based College Exam Management System

📌 Steps to Upload this README.md to GitHub
1️⃣ Create a README.md file:

bash
Copy
Edit
touch README.md
nano README.md
2️⃣ Copy & paste the above content.
3️⃣ Save the file (CTRL + X → Y → ENTER)
4️⃣ Push to GitHub:

bash
Copy
Edit
git add README.md
git commit -m "Added detailed project documentation"
git push origin main
