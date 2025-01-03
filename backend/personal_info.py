from data_layer.db_executor import (db_get_user_by_id,
                                    db_get_role_by_id,
                                    db_get_department_by_id,
                                    db_insert_action_log,
                                    db_update_user_personal_info,
                                    db_get_user_by_email)

GETTING_PERSONAL_INFO_BY_ID_DETAILS = "Пользователь просмотрел информацию о своей учётной записи."
UPDATING_PERSONAL_INFO_BY_ID_DETAILS = "Пользователь изменил свои персональные данные."


def get_personal_info_by_user_id(user_id):
    user = db_get_user_by_id(user_id)
    role = db_get_role_by_id(user[5])
    department = db_get_department_by_id(user[6])

    if role is None:
        role_name = 'Неопределена'
    else:
        role_name = role[1]

    if department is None:
        department_name = 'Неопределён'
    else:
        department_name = department[1]

    db_insert_action_log(user[0], GETTING_PERSONAL_INFO_BY_ID_DETAILS)
    return {
            "user_id": user[0],
            "first_name": user[1],
            "last_name": user[2],
            "email": user[3],
            "hashed_password": user[4],
            "role": role_name,
            "department": department_name,
            "is_active": user[7],
            "created_at": user[8],
            "updated_at": user[9],
        }


def update_personal_info_by_user_id(user_id, new_first_name, new_last_name, new_email, new_hashed_password):
    if db_get_user_by_email(new_email) is not None:
        return 0

    user = db_update_user_personal_info((new_first_name, new_last_name, new_email, new_hashed_password, user_id))

    if user[0] != user_id:
        return 1
    else:
        db_insert_action_log(user[0], UPDATING_PERSONAL_INFO_BY_ID_DETAILS)
        return 2

