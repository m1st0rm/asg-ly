from data_layer.db_executor import db_login
from backend.helpers import *
from backend.instances import User


def login(email, password):
    hashed_password = hash_data(password)
    user = db_login(email, hashed_password)
    print(user)

    if user is None:
        return 0
    elif user[6] is False:
        return 1
    else:
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
