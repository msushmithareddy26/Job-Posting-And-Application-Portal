# 💼 Job Posting and Application Portal

A full-stack web application built with **React**, **Django**, and **MySQL** that enables recruiters to post job openings and applicants to apply. This project demonstrates real-world CRUD operations, secure authentication, role-based access control, and API documentation using Swagger.

---

## 🚀 Features

### 👩‍💼 Recruiters can:
- Post new job openings
- Edit or delete job postings
- View a list of applicants for each job

### 🧑‍💻 Applicants can:
- Create an account and log in
- View all active job postings
- Apply for jobs with their details
- Track application status

### 🔐 System Features:
- Secure authentication system
- Role-based access control
- Responsive UI built with React
- RESTful API powered by Django
- Persistent data storage using MySQL
- Interactive API documentation with Swagger
- Unit tests for backend and frontend components

---

## 🛠️ Tech Stack

| Layer       | Technology                     |
|-------------|--------------------------------|
| Frontend    | React 18, Axios, Bootstrap     |
| Backend     | Django 4.2, Django REST Framework |
| Database    | MySQL                          |
| API Docs    | Swagger (via drf-yasg)         |
| Testing     | Pytest, React Testing Library  |
| Versioning  | Git & GitHub                   |

---

## 📁 Project Structure

job-posting-and-application-portal/ 
├── backend/ 
│ └── jobportal/
        # Django backend (API + business logic) 
        ├── frontend/ # React frontend (UI)
        └── README.md # Project documentation

Code:

## ⚙️ Installation & Setup:

### 🔹 Backend Setup (Django + MySQL):

```bash
# Navigate to backend folder
cd backend/jobportal

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt

# Configure MySQL in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jobportal_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
🔹 Frontend Setup (React):
bash
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start development server
npm start
📡 API Overview:
Method	Endpoint                      	Description
GET	/api/jobs/	                  List all job postings
POST	/api/jobs/	                  Create a new job (Recruiter only)
GET	/api/applications/	      View applications (Recruiter only)
POST	/api/apply/	                  Apply to a job (Applicant only)
Interactive API documentation available at: http://localhost:8000/swagger/

✅ Testing:
🔹 Backend Tests:
bash
python manage.py test
Tests include:

-Job listing and creation

-Application submission

-Role-based access control

🔹 Frontend Tests:
bash
npm test
Tests include:

-Component rendering (e.g., CandidateForm)

-Form validation

-API call mocking

📸 Screenshots:
![Screenshot](https://github.com/user-attachments/assets/915305b7-f210-4fb2-b164-4d97006ef88d)

![Job Portal UI 1](https://github.com/user-attachments/assets/ab724c4e-198a-4ec3-b92d-4401e9c1f7ea)

![Job Portal UI 2](https://github.com/user-attachments/assets/a985e5ff-c8fc-43b3-a286-897e90d75b99)
![ss](https://github.com/user-attachments/assets/7f7f2fae-5856-4021-bc24-495591df11d1)


💡 Design Decisions & Challenges:
-Chose Django for its built-in admin and rapid API development.

-Used MySQL for relational integrity and scalability.

-Implemented role-based access using custom permissions in Django REST Framework.

-Faced challenges with form validation across frontend and backend — resolved by syncing error messages and using consistent schemas.

-Swagger was added to improve API visibility and testing during development.

🤝 Contributing:
Contributions are welcome!

bash
# Fork the repository
# Create a new branch (e.g., feature/job-filter)
# Commit your changes
# Push to your branch
# Open a Pull Request
📜 License
This project is licensed under the MIT License.

👩‍💻 Author
Sushmitha Reddy
GitHub: msushmithareddy26
