from data_layer.db_executor import db_login, db_insert_action_log
from backend.helpers import *
from backend.instances import User


LOGIN_ACTION_DETAILS = "Пользователь вошёл в систему."


def login(email, password):
    hashed_password = hash_data(password)
    user = db_login(email, hashed_password)

    if user is None:
        return 0
    elif user[6] is False:
        return 1
    else:
        db_insert_action_log(user[0], LOGIN_ACTION_DETAILS)
        return User(
            user_id=user[0],
            first_name=user[1],
            last_name=user[2],
            email=user[3],
            role_id=user[4],
            department_id=user[5],
            is_active=user[6],
            created_at=user[7],
            updated_at=user[8],
        )
