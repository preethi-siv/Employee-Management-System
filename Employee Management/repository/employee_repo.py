from utils.logger import get_logger
logger = get_logger()
from db.connection import get_connection

def add_employee(name, department, email, salary):
    connection = get_connection()
    
    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        query = """
        INSERT INTO employee (name, department, email, salary)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (name, department, email, salary))
        connection.commit()

        return True

    except Exception as e:
        logger.error(f"Error inserting employee: {e}")
        return False

    finally:
        cursor.close()
        connection.close()



def get_employee_by_id(emp_id):
    connection = get_connection()

    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM employee WHERE emp_id = %s AND is_active = TRUE"
        cursor.execute(query, (emp_id,))

        result = cursor.fetchone()
        return result

    except Exception as e:
        logger.error(f"Error fetching employee: {e}")
        return None

    finally:
        cursor.close()
        connection.close()


def get_employees_by_name(name):
    connection = get_connection()

    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT * FROM employee
        WHERE name LIKE %s AND is_active = TRUE
        """
        cursor.execute(query, (f"%{name}%",))
        return cursor.fetchall()

    except Exception as e:
        logger.error(f"Error searching by name: {e}")
        return []

    finally:
        cursor.close()
        connection.close()


def get_employees_by_department(department):
    connection = get_connection()

    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT * FROM employee
        WHERE department = %s AND is_active = TRUE
        """
        cursor.execute(query, (department,))

        return cursor.fetchall()

    except Exception as e:
        logger.error(f"Error searching by department: {e}")
        return []

    finally:
        cursor.close()
        connection.close()


def get_employees_paginated(limit, offset):
    connection = get_connection()

    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT * FROM employee
        WHERE is_active = TRUE
        ORDER BY emp_id
        LIMIT %s OFFSET %s
        """
        cursor.execute(query, (limit, offset))

        return cursor.fetchall()

    except Exception as e:
        logger.error(f"Error fetching paginated employees: {e}")
        return []

    finally:
        cursor.close()
        connection.close()


def update_employee(emp_id, name, department, email, salary):
    connection = get_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        query = """
        UPDATE employee
        SET name = %s,
            department = %s,
            email = %s,
            salary = %s
        WHERE emp_id = %s AND is_active = TRUE
        """

        cursor.execute(query, (name, department, email, salary, emp_id))
        connection.commit()

        if cursor.rowcount == 0:
            return False

        return True

    except Exception as e:
        logger.error(f"Error updating employee: {e}")
        return False

    finally:
        cursor.close()
        connection.close()


def deactivate_employee(emp_id):
    connection = get_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        query = """
        UPDATE employee
        SET is_active = FALSE
        WHERE emp_id = %s AND is_active = TRUE
        """

        cursor.execute(query, (emp_id,))
        connection.commit()

        if cursor.rowcount == 0:
            return False

        return True

    except Exception as e:
        logger.error(f"Error deactivating employee: {e}")
        return False

    finally:
        cursor.close()
        connection.close()
