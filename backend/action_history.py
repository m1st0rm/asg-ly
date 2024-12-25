from data_layer.db_executor import db_get_action_history, db_insert_action_log


GETTING_ACTION_HISTORY_DETAILS = "Пользователь просмотрел логи действий."


def get_action_history(user_id):
    db_insert_action_log(user_id, GETTING_ACTION_HISTORY_DETAILS)
    result = db_get_action_history()
    action_history = []

    if len(result) == 0:
        action_history.append(
            {
                "ID лога": 'Нет логов',
                "ID пользователя": 'Нет логов',
                "Имя пользователя": 'Нет логов',
                "Фамилия пользователя": 'Нет логов',
                "Email пользователя": 'Нет логов',
                "Роль пользователя": 'Нет логов',
                "Отдел пользователя": 'Нет логов',
                "Описание дейтсвия": 'Нет логов',
                "Дата и время совершения действия": 'Нет логов',
            }
        )
        return action_history

    for row in result:

        if not row[15]:
            user_role = "Неопределена"
        else:
            user_role = row[15]

        if not row[18]:
            user_department = "Неопределён"
        else:
            user_department = row[18]

        action_history.append(
            {
                "ID лога": row[0],
                "ID пользователя": row[1],
                "Имя пользователя": row[5],
                "Фамилия пользователя": row[6],
                "Email пользователя": row[7],
                "Роль пользователя": user_role,
                "Отдел пользователя": user_department,
                "Описание дейтсвия": row[2],
                "Время совершения действия": row[3].strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    return action_history
