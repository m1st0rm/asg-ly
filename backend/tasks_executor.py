from data_layer.db_executor import db_get_executor_tasks, db_insert_action_log, db_update_executor_task_status


GETTING_EXECUTOR_TASKS_DETAILS = "Пользователь просмотрел информацию о задачах, которые назначены ему."
UPDATING_EXECUTOR_STATUS_DETAILS = "Пользователь обновил статус задачи со стороны исполнителя."


def get_executor_tasks(user_id):
    db_insert_action_log(user_id, GETTING_EXECUTOR_TASKS_DETAILS)
    result = db_get_executor_tasks(user_id)
    executor_tasks = []

    for row in result:
        executor_tasks.append(
            {
                "Номер задачи": row[0],
                'Имя задачи': row[1],
                'Описание задачи': row[2],
                'Дедлайн задачи': row[3].strftime("%Y-%m-%d %H:%M:%S"),
                'Дата и время создания задачи': row[4].strftime("%Y-%m-%d %H:%M:%S"),
                'Дата и время последнего изменения задачи': row[5].strftime("%Y-%m-%d %H:%M:%S"),
                'ID координатора': row[6],
                'Имя координатора': row[7],
                'Фамилия координатора': row[8],
                'Приоритет задачи': row[9],
                'Тип задачи': row[10],
                'Статус со стороны исполнителя': row[11],
                'Статус со стороны координатора': row[12],
            }
        )

    return executor_tasks


def update_task_executor_status(user_id, task_id, executor_status_id):
    result = db_update_executor_task_status(task_id, executor_status_id)
    if result[0] != int(executor_status_id):
        return 1
    else:
        db_insert_action_log(user_id, UPDATING_EXECUTOR_STATUS_DETAILS)
        return 2
