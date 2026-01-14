from service.employee_service import (
    create_employee,
    search_employee_by_id,
    search_employee_by_name,
    search_employee_by_department,
    update_employee_details,
    delete_employee,
    list_employees
)

def show_menu():
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Search by ID")
    print("3. Search by Name")
    print("4. Search by Department")
    print("5. Update Employee")
    print("6. Delete Employee")
    print("7. List Employees")
    print("0. Exit")

def run():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            if not name or name.isdigit():
                print("Invalid name")

            else:
                dept = input("Department: ").strip()
                if not dept or dept.isdigit():
                    print("Invalid department")

                else:
                    email = input("Email: ").strip()
                    if not email or "@" not in email or "." not in email:
                        print("Invalid email")

                    else:
                        try:
                            salary = float(input("Salary: "))
                            if salary < 0:
                                print("Salary cannot be negative")
                            else:
                                status, msg = create_employee(name, dept, email, salary)
                                print(msg)
                        except ValueError:
                            print("Invalid salary")

        elif choice == "2":
            try:
                emp_id = int(input("Employee ID: "))
                status, result = search_employee_by_id(emp_id)
                print(result)
            except ValueError:
                print("Invalid employee ID")

        elif choice == "3":
            name = input("Name: ")
            status, result = search_employee_by_name(name)
            for e in result:
                print(e)

        elif choice == "4":
            dept = input("Department: ")
            status, result = search_employee_by_department(dept)
            for e in result:
                print(e)

        elif choice == "5":
            try:
                emp_id = int(input("Employee ID: "))
                name = input("Name: ")
                dept = input("Department: ")
                email = input("Email: ")
                salary = float(input("Salary: "))
                status, msg = update_employee_details(emp_id, name, dept, email, salary)
                print(msg)
            except ValueError:
                print("Invalid input")

        elif choice == "6":
            try:
                emp_id = int(input("Employee ID: "))
                status, msg = delete_employee(emp_id)
                print(msg)
            except ValueError:
                print("Invalid employee ID")

        elif choice == "7":
            try:
                page = int(input("Page: "))
                size = int(input("Page size: "))
                status, result = list_employees(page, size)
                for e in result:
                    print(e)
            except ValueError:
                print("Invalid pagination input")

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

        input("\nPress Enter to continue...")
