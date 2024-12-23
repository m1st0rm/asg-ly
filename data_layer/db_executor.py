from data_layer.db_connector import get_db_connection
from data_layer.db_query_keeper import QUERIES


def db_login(email, hashed_password):
    db_connection = get_db_connection()
    query = QUERIES['login']

    with db_connection.cursor() as cursor:
        cursor.execute(query, (email, hashed_password))
        return cursor.fetchone()
