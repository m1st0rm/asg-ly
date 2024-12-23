from data_layer.db_executor import db_register, db_get_user_by_email
from backend.helpers import *


def register(first_name, last_name, email, password):
    check = db_get_user_by_email(email)

    if check is not None:
        return 0
    else:
        hashed_password = hash_data(password)
        result = db_register(first_name, last_name, email, hashed_password)

        if result != 1:
            return 1
        else:
            return 2
