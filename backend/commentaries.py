from data_layer.db_executor import db_get_commentaries_for_task, db_insert_action_log, db_insert_commentary_for_task


GET_COMMENTARIES_FOR_TASK_DETAILS = "Пользователь просмотрел комментарии к задаче."
INSERT_COMMENTARY_FOR_TASK_DETAILS = "Пользователь оставил комментарии к задаче"


def get_commentaries_for_task(user_id, task_id):
    db_insert_action_log(user_id, GET_COMMENTARIES_FOR_TASK_DETAILS)
    result = db_get_commentaries_for_task(task_id)
    commentaries = []

    for row in result:
        commentaries.append(
            {
                'ID комментария': row[0],
                'ID автора': row[3],
                'Имя автора': row[4],
                'Фамилия автора': row[5],
                'Роль автора': row[6],
                'Отдел автора': row[7],
                'Текст комментария': row[1],
                'Дата и время оставления комментария': row[2],
            }
        )

    return commentaries


def insert_commentary_for_task(user_id, task_id, content):
    result = db_insert_commentary_for_task(task_id, user_id, content)

    if result[0] != content:
        return 1
    else:
        db_insert_action_log(user_id, INSERT_COMMENTARY_FOR_TASK_DETAILS)
        return 2
