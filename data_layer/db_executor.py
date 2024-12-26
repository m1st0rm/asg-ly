from data_layer.db_connector import get_db_connection
from data_layer.db_query_keeper import QUERIES


def db_login(email, hashed_password):
    db_connection = get_db_connection()
    query = QUERIES['login']

    with db_connection.cursor() as cursor:
        cursor.execute(query, (email, hashed_password))
        result = cursor.fetchone()
    db_connection.close()
    return result


def db_get_user_by_email(email):
    db_connection = get_db_connection()
    query = QUERIES['get_user_by_email']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (email,))
        result = cursor.fetchone()
    db_connection.close()
    return result


def db_register(first_name, last_name, email, hashed_password):
    db_connection = get_db_connection()
    query = QUERIES['register']

    with db_connection.cursor() as cursor:
        cursor.execute(query, (first_name, last_name, email, hashed_password))
        user_id = cursor.fetchone()[0]
    db_connection.commit()
    db_connection.close()
    return user_id


def db_insert_action_log(user_id, action_details):
    db_connection = get_db_connection()
    query = QUERIES['insert_action_log']

    with db_connection.cursor() as cursor:
        cursor.execute(query, (user_id, action_details))
    db_connection.commit()
    db_connection.close()


def db_get_user_by_id(user_id):
    db_connection = get_db_connection()
    query = QUERIES['get_user_by_id']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
    db_connection.close()
    return result


def db_get_role_by_id(role_id):
    db_connection = get_db_connection()
    query = QUERIES['get_role_by_id']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (role_id,))
        result = cursor.fetchone()
    db_connection.close()
    return result


def db_get_department_by_id(department_id):
    db_connection = get_db_connection()
    query = QUERIES['get_department_by_id']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (department_id,))
        result = cursor.fetchone()
    db_connection.close()
    return result


def db_update_user_personal_info(updations):
    db_connection = get_db_connection()
    query = QUERIES['update_user_personal_info']
    with db_connection.cursor() as cursor:
        cursor.execute(query, updations)
        result = cursor.fetchone()
    db_connection.commit()
    db_connection.close()
    return result


def db_get_action_history():
    db_connection = get_db_connection()
    query = QUERIES['get_action_history']
    with db_connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    db_connection.close()
    return result


def db_get_departments():
    db_connection = get_db_connection()
    query = QUERIES['get_departments']
    with db_connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    db_connection.close()
    return result


def db_add_department(department_name):
    db_connection = get_db_connection()
    query = QUERIES['add_department']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (department_name,))
        result = cursor.fetchone()
    db_connection.commit()
    db_connection.close()
    return result


def db_get_department_by_name(department_name):
    db_connection = get_db_connection()
    query = QUERIES['get_department_by_name']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (department_name,))
        result = cursor.fetchone()
    db_connection.close()
    return result


def db_update_department_by_id(department_id, department_name):
    db_connection = get_db_connection()
    query = QUERIES['update_department']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (department_name, department_id))
        result = cursor.fetchone()
    db_connection.commit()
    db_connection.close()
    return result


def db_get_users_ex_admin():
    db_connection = get_db_connection()
    query = QUERIES['get_users_ex_admin']
    with db_connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    db_connection.close()
    return result


def db_get_roles_names():
    db_connection = get_db_connection()
    query = QUERIES['get_roles_names']
    with db_connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    db_connection.close()
    return result


def db_get_departments_names():
    db_connection = get_db_connection()
    query = QUERIES['get_departments_names']
    with db_connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    db_connection.close()
    return result


def db_update_user_active_status(user_id, active_status):
    db_connection = get_db_connection()
    query = QUERIES['update_user_active_status']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (active_status, user_id))
        result = cursor.fetchone()
    db_connection.commit()
    db_connection.close()
    return result


def db_update_user_role(user_id, role_id):
    db_connection = get_db_connection()
    query = QUERIES['update_user_role']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (role_id, user_id))
        result = cursor.fetchone()
    db_connection.commit()
    db_connection.close()
    return result


def db_update_user_department(user_id, department_id):
    db_connection = get_db_connection()
    query = QUERIES['update_user_department']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (department_id, user_id))
        result = cursor.fetchone()
    db_connection.commit()
    db_connection.close()
    return result


def db_get_role_id_by_name(role_name):
    db_connection = get_db_connection()
    query = QUERIES['get_role_id_by_name']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (role_name,))
        result = cursor.fetchone()
    db_connection.close()
    return result


def db_get_department_id_by_name(department_name):
    db_connection = get_db_connection()
    query = QUERIES['get_department_id_by_name']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (department_name,))
        result = cursor.fetchone()
    db_connection.close()
    return result


def db_is_user_available_to_change_role(user_id):
    db_connection = get_db_connection()
    query = QUERIES['is_user_available_to_change_role']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (user_id, ))
        result = cursor.fetchone()
    db_connection.close()
    return result


def db_get_users_to_add_task():
    db_connection = get_db_connection()
    query = QUERIES['get_users_to_add_task']
    with db_connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    db_connection.close()
    return result


def db_insert_new_task(task_name, description, assigned_to_user_id, due_date, created_by_user_id, priority_id, task_type_id):
    db_connection = get_db_connection()
    query = QUERIES['insert_new_task']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (task_name, description, assigned_to_user_id, due_date, created_by_user_id, priority_id, task_type_id))
        result = cursor.fetchone()
    db_connection.commit()
    db_connection.close()
    return result


def db_get_manager_tasks(coordinator_id):
    db_connection = get_db_connection()
    query = QUERIES['get_manager_tasks']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (coordinator_id,))
        result = cursor.fetchall()
    db_connection.close()
    return result


def db_update_manager_task_status(task_id, assignor_status_id):
    db_connection = get_db_connection()
    query = QUERIES['update_manager_task_status']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (assignor_status_id, task_id))
        result = cursor.fetchone()
    db_connection.commit()
    db_connection.close()
    return result


def db_get_commentaries_for_task(task_id):
    db_connection = get_db_connection()
    query = QUERIES['get_commentaries_for_task']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (task_id,))
        result = cursor.fetchall()
    db_connection.close()
    return result


def db_insert_commentary_for_task(task_id, user_id, content):
    db_connection = get_db_connection()
    query = QUERIES['insert_commentary_for_task']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (task_id, user_id, content))
        result = cursor.fetchone()
    db_connection.commit()
    db_connection.close()
    return result


def db_get_executor_tasks(executor_id):
    db_connection = get_db_connection()
    query = QUERIES['get_executor_tasks']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (executor_id,))
        result = cursor.fetchall()
    db_connection.close()
    return result


def db_update_executor_task_status(task_id, executor_status_id):
    db_connection = get_db_connection()
    query = QUERIES['update_executor_task_status']
    with db_connection.cursor() as cursor:
        cursor.execute(query, (executor_status_id, task_id))
        result = cursor.fetchone()
    db_connection.commit()
    db_connection.close()
    return result
