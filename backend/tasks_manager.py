from data_layer.db_executor import db_get_manager_tasks, db_insert_action_log, db_update_manager_task_status


GETTING_MANAGER_TASKS_DETAILS = "Пользователь просмотрел информацию о задачах, которые созданы им."
UPDATING_MANAGER_STATUS_DETAILS = "Пользователь обновил статус задачи со стороны координатора."


def get_manager_tasks(user_id):
    db_insert_action_log(user_id, GETTING_MANAGER_TASKS_DETAILS)
    result = db_get_manager_tasks(user_id)
    manager_tasks = []

    for row in result:
        manager_tasks.append(
            {
                "Номер задачи": row[0],
                'Имя задачи': row[1],
                'Описание задачи': row[2],
                'Дедлайн задачи': row[3].strftime("%Y-%m-%d %H:%M:%S"),
                'Дата и время создания задачи': row[4].strftime("%Y-%m-%d %H:%M:%S"),
                'Дата и время последнего изменения задачи': row[5].strftime("%Y-%m-%d %H:%M:%S"),
                'ID исполнителя': row[6],
                'Имя исполнителя': row[7],
                'Фамилия исполнителя': row[8],
                'Приоритет задачи': row[9],
                'Тип задачи': row[10],
                'Статус со стороны исполнителя': row[11],
                'Статус со стороны координатора': row[12],
            }
        )

    return manager_tasks


def update_task_manager_status(user_id, task_id, assignor_status_id):
    result = db_update_manager_task_status(task_id, assignor_status_id)
    if result[0] != int(assignor_status_id):
        return 1
    else:
        db_insert_action_log(user_id, UPDATING_MANAGER_STATUS_DETAILS)
        return 2
