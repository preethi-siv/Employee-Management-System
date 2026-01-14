# 📌Employee Management System (Console-Based, MySQL)

## 🔍 Project Overview

This is a console-based Employee Management System built using Python and MySQL, designed with a layered architecture to simulate a real-world backend system.

The project focuses on:
- clean code structure
  
- database efficiency
  
- input validation
  
- performance-aware design

Unlike GUI-heavy projects, this system emphasizes logic, scalability, and backend best practices.

## 🧠 Key Concepts Demonstrated

- CRUD operations with MySQL
  
- Layered architecture (UI → Service → Repository → DB)
  
- Database-level pagination
  
- Indexing for performance optimization
  
- Soft delete strategy
  
- Input validation at multiple layers
  
- Logging and error handling

## 🛠 Tech Stack

- **Language:** Python

- **Database:** MySQL

- **Connector**: mysql-connector-python

- **Architecture:** Layered (Repository, Service, UI)

- **Version Control:** Git & GitHub

## 📁 Project Structure
Employee-Management/

│

├── db/

│ └── connection.py # MySQL connection handling

│

├── repository/
│ └── employee_repo.py # SQL queries & database operations
│
├── service/
│ └── employee_service.py # Business logic and validations
│
├── ui/
│ └── console.py # Console-based user interface
│
├── utils/
│ ├── logger.py # Application logging
│ └── validator.py # (Reserved for future validation reuse)
│
├── main.py # Application entry point
└── README.md

## ✨ Features
### ✅ Employee Operations

- Add employee
- Update employee details
- Soft delete employee (is_active flag)
- Search employee by:
    - ID
    - Name
    - Department
- List employees with pagination

### ✅ Data Validation

- Prevents numeric or empty names/departments

- Validates email format

- Handles invalid salary inputs

- Early validation in UI + final validation in service layer

### ✅ Performance-Oriented Design

- Database-level pagination using LIMIT & OFFSET

- Indexing on frequently searched columns

- Avoids loading large datasets into memory

### ✅ Soft Delete Strategy

Employees are not permanently deleted.
Instead:
        is_active = FALSE

This ensures:    
- data safety
- auditability
- realistic enterprise behavior

## ⚡ Database Schema

CREATE TABLE employee (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10,2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

### Indexes Used

CREATE INDEX idx_emp_id ON employee(emp_id);
CREATE INDEX idx_emp_name ON employee(name);
CREATE INDEX idx_emp_department ON employee(department);

## 🚀 How to Run the Project
### 1️⃣ Clone the repository
git clone <your-repo-url>
cd Employee-Management

### 2️⃣ Install dependencies
pip install mysql-connector-python

### 3️⃣ Configure database

Update credentials in:

db/connection.py

### 4️⃣ Run the application
python main.py

## 🧪 Sample Console Menu
Employee Management System
1. Add Employee
2. Search by ID
3. Search by Name
4. Search by Department
5. Update Employee
6. Delete Employee
7. List Employees
0. Exit

## 🧩 Design Decisions

- **Repository layer** contains only SQL queries

- **Service layer** enforces business rules and validation

- **UI layer** handles user interaction and early feedback

- **Database** handles pagination and indexing for efficiency

This separation improves maintainability and scalability.

## 📌 What This Project Shows to Recruiters

- Strong backend fundamentals

- Real MySQL integration (not mock data)

- Performance-aware coding

- Clean architecture and separation of concerns

- Production-style error handling

## 🔮 Future Enhancements

- REST API using Flask / FastAPI

- Authentication & role-based access

- Advanced email validation

- Unit testing

- Export reports (CSV / PDF)

## 👤 Author

**Preethi**

Final Year BE CSE

Software Development Enthusiast

