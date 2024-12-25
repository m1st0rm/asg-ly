from data_layer.db_executor import db_get_departments, db_insert_action_log


GETTING_DEPARTMENTS_DETAILS = "Пользователь просмотрел информацию об отделах."


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
