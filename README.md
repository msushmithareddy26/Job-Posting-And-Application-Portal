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

bash
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

##📸 Screenshots:


<img width="2074" height="1154" alt="image" src="https://github.com/user-attachments/assets/4f468b00-9f34-4ceb-948a-55f188e31ed3" />
<img width="1419" height="1183" alt="image" src="https://github.com/user-attachments/assets/bab2c404-5ce8-4ed4-90a4-e54ab156496a" />
<img width="2489" height="1132" alt="image" src="https://github.com/user-attachments/assets/c087115e-695d-4774-8616-df560695851d" />



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

