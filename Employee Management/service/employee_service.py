from repository.employee_repo import (
    add_employee,
    get_employee_by_id,
    get_employees_by_name,
    get_employees_by_department,
    get_employees_paginated,
    update_employee,
    deactivate_employee
)

def create_employee(name, department, email, salary):
    # Trim whitespace
    name = name.strip()
    department = department.strip()
    email = email.strip()

    # Name validation
    if not name or name.isdigit():
        return False, "Invalid name"

    # Department validation
    if not department or department.isdigit():
        return False, "Invalid department"

    # Email validation (basic)
    if not email or "@" not in email or "." not in email:
        return False, "Invalid email"

    # Salary validation
    if salary < 0:
        return False, "Salary cannot be negative"

    success = add_employee(name, department, email, salary)

    if not success:
        return False, "Employee with this email already exists"

    return True, "Employee created successfully"



def search_employee_by_id(emp_id):
    if emp_id <= 0:
        return False, "Invalid employee ID"

    employee = get_employee_by_id(emp_id)

    if employee is None:
        return False, "Employee not found"

    return True, employee



def search_employee_by_name(name):
    if not name:
        return False, "Name cannot be empty"

    employees = get_employees_by_name(name)

    if not employees:
        return False, "No employees found"

    return True, employees



def search_employee_by_department(department):
    if not department:
        return False, "Department cannot be empty"

    employees = get_employees_by_department(department)

    if not employees:
        return False, "No employees found in this department"

    return True, employees



def list_employees(page, page_size):
    if page <= 0 or page_size <= 0:
        return False, "Invalid pagination parameters"

    offset = (page - 1) * page_size
    employees = get_employees_paginated(page_size, offset)

    if not employees:
        return False, "No employees found"

    return True, employees



def update_employee_details(emp_id, name, department, email, salary):
    if emp_id <= 0:
        return False, "Invalid employee ID"

    if not name or not department:
        return False, "Name and Department are required"

    if salary is not None and salary < 0:
        return False, "Salary cannot be negative"

    success = update_employee(emp_id, name, department, email, salary)

    if not success:
        return False, "Employee not found or inactive"

    return True, "Employee updated successfully"



def delete_employee(emp_id):
    if emp_id <= 0:
        return False, "Invalid employee ID"

    success = deactivate_employee(emp_id)

    if not success:
        return False, "Employee not found or already inactive"

    return True, "Employee deactivated successfully"
