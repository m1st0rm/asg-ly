from data_layer.db_executor import db_get_users_to_add_task, db_insert_action_log, db_insert_new_task
from datetime import datetime, timedelta


GET_USERS_TO_ADD_TASK_DETAILS = "Пользователь просмотрел информацию о исполнителях задач."
INSERT_TASK_DETAILS = "Пользователь добавил новую задачу."


def get_users_to_add_task(user_id):
    db_insert_action_log(user_id, GET_USERS_TO_ADD_TASK_DETAILS)
    result = db_get_users_to_add_task()
    users_to_add_task = []

    for row in result:
        users_to_add_task.append(
            {
                'ID исполнителя': row[0],
                'Имя исполнителя': row[1],
                'Фамилия исполнителя': row[2],
                'Отдел исполнителя': row[3],
            }
        )

    return users_to_add_task


def insert_new_task(task_name, description, assigned_to_user_id, task_days, created_by_user_id, priority_id, task_type_id):
    due_date = datetime.now() + timedelta(days=task_days)
    result = db_insert_new_task(task_name, description, assigned_to_user_id, due_date, created_by_user_id, priority_id, task_type_id)

    if result[0] != task_name:
        return 1
    else:
        db_insert_action_log(created_by_user_id, INSERT_TASK_DETAILS)
        return 2
