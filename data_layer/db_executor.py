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

