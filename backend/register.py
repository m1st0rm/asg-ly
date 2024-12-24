from data_layer.db_executor import db_register, db_get_user_by_email, db_insert_action_log
from backend.helpers import *


REGISTER_ACTION_DETAILS = "Пользователь зарегестрировался в системе."


def register(first_name, last_name, email, password):
    check = db_get_user_by_email(email)

    if check is not None:
        return 0
    else:
        hashed_password = hash_data(password)
        user_id = db_register(first_name, last_name, email, hashed_password)

        if user_id is None:
            return 1
        else:
            db_insert_action_log(user_id, REGISTER_ACTION_DETAILS)
            return 2
