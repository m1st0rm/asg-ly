from data_layer.db_executor import (db_get_departments,
                                    db_insert_action_log,
                                    db_add_department,
                                    db_get_department_by_name,
                                    db_get_department_by_id,
                                    db_update_department_by_id)


GETTING_DEPARTMENTS_DETAILS = "Пользователь просмотрел информацию об отделах."
INSERTING_DEPARTMENT_DETAILS = "Пользователь добавил новый отдел."
UPDATING_DEPARTMENT_DETAILS = "Пользователь изменил название отдела."


def get_departments(user_id):
    db_insert_action_log(user_id, GETTING_DEPARTMENTS_DETAILS)
    result = db_get_departments()
    departments = []

    if len(result) == 0:
        departments.append(
            {
                "ID отдела": "Не существует отделов",
                "Имя отдела": "Не существует отделов",
                "Количество сотрудников в отделе": "Не существует отделов",
                "Дата и время создания отдела": "Не существует отделов",
                "Дата и время последнего изменения отдела": "Не существует отделов",
            }
        )
        return departments

    for row in result:
        departments.append(
            {
                "ID отдела": row[0],
                "Имя отдела": row[1],
                "Количество сотрудников в отделе": row[4],
                "Дата и время создания отдела": row[2].strftime("%Y-%m-%d %H:%M:%S"),
                "Дата и время последнего изменения отдела": row[3].strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    return departments


def add_department(user_id, department_name):
    check = db_get_department_by_name(department_name)
    if check is not None:
        return 1
    else:
        result = db_add_department(department_name)
        if result[0] != department_name:
            return 2
        else:
            db_insert_action_log(user_id, INSERTING_DEPARTMENT_DETAILS)
            return 3


def update_department(user_id, department_id, new_department_name):
    check1 = db_get_department_by_id(department_id)
    check2 = db_get_department_by_name(new_department_name)
    if check1 is None:
        return 1
    elif check2 is not None:
        return 2
    else:
        result = db_update_department_by_id(department_id, new_department_name)
        if result[0] != new_department_name:
            return 3
        else:
            db_insert_action_log(user_id, UPDATING_DEPARTMENT_DETAILS)
            return 4
