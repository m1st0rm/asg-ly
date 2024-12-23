import psycopg2
from data_layer.db_credentials import DB_CREDENTIALS as credentials


def get_db_connection():
    return psycopg2.connect(
        dbname=credentials.get('dbname'),
        user=credentials.get('user'),
        password=credentials.get('password'),
        host=credentials.get('host'),
        port=credentials.get('port')
    )
