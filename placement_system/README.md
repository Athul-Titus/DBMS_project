<h1 align="center">🎓 Placement Management System</h1>

<p align="center">
  <strong>A comprehensive, modern web application bridging the gap between students, institutions, and recruitment companies.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Flask-lightgrey.svg" alt="Flask">
  <img src="https://img.shields.io/badge/Database-SQLite-green.svg" alt="SQLite">
  <img src="https://img.shields.io/badge/Frontend-Bootstrap_5-purple.svg" alt="Bootstrap">
</p>

---

## 📖 Overview

The **Placement Management System** is a robust, full-stack web application designed to streamline the campus recruitment lifecycle. It serves as a centralized portal for students to discover opportunities and apply for roles, while empowering administrators and placement officers to manage companies, job postings, and interview schedules seamlessly.

Designed with scalability, security, and user experience in mind, this project demonstrates proficiency in backend architecture, relational database design, and responsive frontend UI.

---

## ✨ Key Features

### 👨‍🎓 Student Portal
- **Intuitive Dashboard**: Real-time overview of application statuses, upcoming interviews, and available job postings.
- **Smart Eligibility Checking**: Automated CGPA and criteria validation before allowing application submissions.
- **Application Tracking**: End-to-end visibility into the recruitment pipeline (Applied ➔ Rounds ➔ Selected/Rejected).
- **Profile Management**: Maintain academic records, contact details, and upload resumes seamlessly.
- **Interview Tracking**: View scheduled technical/HR rounds, offline/online venues, and feedback.

### 🛡️ Administrator Portal (Placement Cell)
- **Analytics Dashboard**: High-level statistics of placed students, active companies, and open positions.
- **Company Management**: Onboard new recruiting partners, manage company profiles, and track hiring history.
- **Job Lifecycle Management**: Post detailed job descriptions, set eligibility criteria (min CGPA, skills), and manage deadlines.
- **Applicant Processing**: Review student applications, update pipeline statuses, and leave administrative remarks.
- **Interview Scheduling**: Coordinate multi-round interviews, assign interviewers, and record final scores and feedback.

---

## 🛠️ Technology Stack

| Layer | Technology | Description |
|-------|------------|-------------|
| **Backend** | Python, Flask | Robust server-side logic, routing, and RESTful API endpoints. |
| **Database** | SQLite | Serverless, self-contained relational database management. |
| **Frontend** | HTML5, CSS3, JS | Clean, semantic structure with interactive components. |
| **Styling** | Bootstrap | Responsive, mobile-first CSS framework for a polished UI. |
| **Templating** | Jinja2 | Dynamic HTML generation and secure data injection. |
| **Security** | Werkzeug, Sessions | Secure session handling, route protection, and authentication. |

---

## 🗄️ Database Architecture

The system utilizes a normalized relational database schema comprising 6 core entities:

1. **`Student`**: Academic records, credentials, and placement status.
2. **`Company`**: Recruiting partners and their contact configurations.
3. **`Job`**: Postings linked to companies, including salary packages and strict eligibility rules.
4. **`Application`**: The junction linking Students and Jobs, tracking the current progression state.
5. **`Interview_Rounds`**: Detailed tracking of individual assessment stages (Round 1, Tech, HR).
6. **`Admin`**: System administrators and placement officers with RBAC roles.

---

## 🚦 Getting Started (Local Setup)

The project is designed to be completely portable and runs out-of-the-box using SQLite. **No external database server configuration is required.**

### Prerequisites
- Python 3.7 or higher
- Git

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Athul-Titus/DBMS_project.git
   cd DBMS_project/placement_system
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```
   *(Ensure `flask` and `python-dotenv` are installed)*

3. **Run the application:**
   The SQLite database (`placement.db`) is already tracked and pre-populated with demo data.
   ```bash
   python app.py
   ```

4. **Access the portal:**
   Open your browser and navigate to: **`http://127.0.0.1:5000`**

---

## 🔐 Demo Credentials

The pre-configured SQLite database includes the following demo accounts to explore the system:

**Student Access:**
- **Email:** `alice@student.com`
- **Password:** `alice123`

**Admin/Placement Officer Access:**
- **Username:** `admin` (or `placement_officer`)
- **Password:** `admin123` (or `officer123`)

---

## 🚀 Future Roadmap & Enhancements
- **Email Integration**: Automated SMTP emails for interview scheduling and offer rollouts.
- **Advanced Analytics**: Visual graphs and exportable CSV reports for placement season statistics.
- **Company Portal**: A dedicated 3rd-party interface for recruiters to shortlist candidates directly.

---

<p align="center">
  <i>Developed to streamline and modernize campus recruitment workflows.</i>
</p>