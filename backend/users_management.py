from data_layer.db_executor import (db_get_users_ex_admin,
                                    db_insert_action_log,
                                    db_get_roles_names,
                                    db_get_departments_names,
                                    db_update_user_active_status,
                                    db_get_role_id_by_name,
                                    db_update_user_role,
                                    db_is_user_available_to_change_role,
                                    db_get_department_id_by_name,
                                    db_update_user_department,
                                    db_get_user_by_id)


GETTING_USERS_EX_ADMIN_DETAILS = "Пользователь просмотрел информацию о всех пользователях."
UPDATING_USER_ACTIVE_STATUS = "Пользователь изменил статус активности другого пользователя."
UPDATING_USER_ROLE = "Пользователь изменил роль другого пользователя."
UPDATING_USER_DEPARTMENT = "Пользователь изменил отдел другого пользователя."


def get_users_ex_admin(role_id):
    db_insert_action_log(role_id, GETTING_USERS_EX_ADMIN_DETAILS)
    result = db_get_users_ex_admin()
    users = []
    for row in result:
        department = row[7]
        role = row[8]
        active_status = row[4]

        if department is None:
            department_name = "Неопределён"
        else:
            department_name = department

        if role is None:
            role_name = "Неопределена"
        else:
            role_name = role

        if active_status is False:
            active_status_name = "Неактивна"
        else:
            active_status_name = "Активна"

        users.append(
            {
                "ID пользователя": row[0],
                "Имя пользователя": row[1],
                "Фамилия пользователя": row[2],
                "Email пользователя": row[3],
                "Статус учётной записи": active_status_name,
                "Дата и время создания учётной записи": row[5].strftime("%Y-%m-%d %H:%M:%S"),
                "Дата и время последнего изменения учётной записи": row[6].strftime("%Y-%m-%d %H:%M:%S"),
                "Отдел пользователя": department_name,
                "Роль пользователя": role_name,
            }
        )

    return users


def get_roles_names():
    result = db_get_roles_names()
    roles = []
    for row in result:
        roles.append(row[0])
    return roles


def get_departments_names():
    result = db_get_departments_names()
    departments = []
    for row in result:
        departments.append(row[0])
    return departments


def update_user_active_status(user_id, edited_user_id, active_status):
    if active_status == 'Активна':
        boolean_active_status = True
    else:
        boolean_active_status = False

    user = db_get_user_by_id(edited_user_id)

    if user is None:
        return 1

    result = db_update_user_active_status(edited_user_id, boolean_active_status)

    if result[0] != boolean_active_status:
        return 2
    else:
        db_insert_action_log(user_id, UPDATING_USER_ACTIVE_STATUS)
        return 3


def update_user_role(user_id, edited_user_id, role_name):
    user = db_get_user_by_id(edited_user_id)

    if user is None:
        return 1

    is_user_available_to_change_role = db_is_user_available_to_change_role(user_id)
    if is_user_available_to_change_role is not None:
        return 2

    role_id = db_get_role_id_by_name(role_name)[0]

    result = db_update_user_role(edited_user_id, role_id)

    if result[0] != role_id:
        return 3
    else:
        db_insert_action_log(user_id, UPDATING_USER_ROLE)
        return 4


def update_user_department(user_id, edited_user_id, department_name):
    user = db_get_user_by_id(edited_user_id)

    if user is None:
        return 1

    department_id = db_get_department_id_by_name(department_name)[0]
    result = db_update_user_department(edited_user_id, department_id)

    if result[0] != department_id:
        return 2
    else:
        db_insert_action_log(user_id, UPDATING_USER_DEPARTMENT)
        return 3
