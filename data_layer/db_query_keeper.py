REGISTER_USER = """
    INSERT INTO public.users (first_name, last_name, email, password_hash, role_id, department_id)
    VALUES (%s, %s, %s, %s, 3, NULL)
    RETURNING user_id;
    """

LOGIN_USER = """
    SELECT user_id, first_name, last_name, email, role_id, department_id, is_active, created_at, updated_at
    FROM public.users
    WHERE email = %s AND password_hash = %s;
    """

GET_USER_BY_EMAIL = """
    SELECT user_id, first_name, last_name, email, role_id, department_id, is_active, created_at, updated_at
    FROM public.users
    WHERE email = %s;
    """

INSERT_ACTION_LOG = """
    INSERT INTO public.actionhistory
    (user_id, action_details)
    VALUES(%s, %s);
"""

GET_USER_BY_ID = """
    SELECT * FROM public.users
    WHERE user_id = %s;
"""

GET_ROLE_BY_ID = """
    SELECT * FROM public.role
    WHERE role_id = %s;
"""

GET_DEPARTMENT_BY_ID = """
    SELECT * FROM public.department
    WHERE department_id = %s;
"""

UPDATE_USER_PERSONAL_INFO = """
    UPDATE public.users
    SET 
        first_name = %s,
        last_name = %s,
        email = %s,
        password_hash = %s,
        updated_at = CURRENT_TIMESTAMP
    WHERE user_id = %s
    RETURNING user_id;
"""

GET_ACTION_HISTORY = """
    SELECT 
        *
    FROM 
        public.actionhistory AS a
    LEFT JOIN 
        public.users AS u
        ON a.user_id = u.user_id
    LEFT JOIN 
        public.role AS r
        ON u.role_id = r.role_id
    LEFT JOIN 
        public.department AS d
        ON u.department_id = d.department_id
    ORDER BY a.created_at DESC;
"""

GET_DEPARTMENTS = """
SELECT 
    d.department_id, 
    d.department_name, 
    d.created_at, 
    d.updated_at, 
    COUNT(u.user_id) 
FROM 
    public.department d 
LEFT JOIN 
    public.users u 
    ON d.department_id = u.department_id 
GROUP BY d.department_id
ORDER BY d.department_id ASC;
"""

ADD_DEPARTMENT = """
INSERT INTO public.department (department_name)
VALUES (%s)
RETURNING department_name;
"""

GET_DEPARTMENT_BY_NAME = """
SELECT * FROM public.department
WHERE department_name = %s;
"""

UPDATE_DEPARTMENT = """
UPDATE public.department
SET
    department_name = %s,
    updated_at = CURRENT_TIMESTAMP
WHERE department_id = %s
RETURNING department_name;
"""

GET_USERS_EX_ADMIN = """
SELECT 
    u.user_id, 
    u.first_name, 
    u.last_name, 
    u.email, 
    u.is_active, 
    u.created_at, 
    u.updated_at, 
    d.department_name, 
    r.role_name
FROM 
    public.users u
LEFT JOIN 
    public.department d ON u.department_id = d.department_id
LEFT JOIN 
    public.role r ON u.role_id = r.role_id
WHERE 
    u.role_id <> 1
ORDER BY u.user_id ASC;
"""

GET_ROLES_NAMES = """
SELECT role_name FROM public.role
WHERE role_id <> 1;
"""

GET_DEPARTMENTS_NAMES = """
SELECT department_name FROM public.department
"""

UPDATE_USER_ACTIVE_STATUS = """
UPDATE public.users
SET 
    is_active = %s,
    updated_at = CURRENT_TIMESTAMP
WHERE user_id = %s
RETURNING is_active;
"""

UPDATE_USER_ROLE = """
UPDATE public.users
SET 
    role_id = %s,
    updated_at = CURRENT_TIMESTAMP
WHERE user_id = %s
RETURNING role_id;
"""

UPDATE_USER_DEPARTMENT = """
UPDATE public.users
SET 
    department_id = %s,
    updated_at = CURRENT_TIMESTAMP
WHERE user_id = %s
RETURNING department_id;
"""

GET_ROLE_ID_BY_NAME = """
SELECT role_id
FROM public.role
WHERE role_name = %s
"""

GET_DEPARTMENT_ID_BY_NAME = """
SELECT department_id
FROM public.department
WHERE department_name = %s
"""

IS_USER_AVAILABLE_TO_CHANGE_ROLE = """
SELECT *
FROM public.task
WHERE 
    assigned_to_user_id = %s
    AND execution_status_id <> 4
    AND assignor_status_id <> 3;
"""

GET_USERS_TO_ADD_TASK = """
SELECT 
    u.user_id, 
    u.first_name, 
    u.last_name, 
    d.department_name
FROM
    public.users u
INNER JOIN 
    public.department d ON u.department_id = d.department_id
WHERE 
    u.role_id <> 1 AND u.role_id <> 2 AND u.is_active = TRUE 
ORDER BY u.user_id ASC;
"""

INSERT_NEW_TASK = """
INSERT INTO public.task
(task_name, description, assigned_to_user_id, due_date, execution_status_id, created_by_user_id, priority_id, task_type_id, assignor_status_id)
VALUES(%s, %s, %s, %s, 1, %s, %s, %s, 1)
RETURNING task_name;
"""

GET_MANAGER_TASKS = """
SELECT 
    t.task_id, 
    t.task_name, 
    t.description, 
    t.due_date, 
    t.created_at, 
    t.updated_at, 
    u.user_id, 
    u.first_name, 
    u.last_name, 
    t2.priority_name, 
    t3.task_type_name, 
    es.execution_status_name, 
    as2.assignor_status_name 
FROM 
    public.task t
INNER JOIN 
    public.users u ON t.assigned_to_user_id = u.user_id
INNER JOIN 
    public.taskpriority t2 ON t.priority_id = t2.priority_id
INNER JOIN 
    public.tasktype t3 ON t.task_type_id = t3.task_type_id
INNER JOIN 
    public.execution_status es ON t.execution_status_id = es.execution_status_id
INNER JOIN 
    public.assignor_status as2 ON t.assignor_status_id = as2.assignor_status_id
WHERE 
    t.created_by_user_id = %s
ORDER BY t.task_id DESC;
"""

UPDATE_MANAGER_TASK_STATUS = """
UPDATE public.task
SET 
    assignor_status_id = %s,
    updated_at = CURRENT_TIMESTAMP
WHERE 
    task_id = %s
RETURNING assignor_status_id;
"""

GET_COMMENTARIES_FOR_TASK = """
    SELECT 
    t.comment_id, 
    t.content, 
    t.created_at, 
    u.user_id, 
    u.first_name, 
    u.last_name, 
    r.role_name, 
    d.department_name
FROM 
    public.taskcomment t
INNER JOIN 
    public.users u ON t.user_id = u.user_id
INNER JOIN 
    public.role r ON u.role_id = r.role_id
INNER JOIN 
    public.department d ON u.department_id = d.department_id
WHERE 
    t.task_id = %s;
"""

INSERT_COMMENTARY_FOR_TASK = """
    INSERT INTO public.taskcomment (task_id, user_id, content)
    VALUES (%s, %s, %s)
    RETURNING content;
"""

QUERIES = {
    'register': REGISTER_USER,
    'login': LOGIN_USER,
    'get_user_by_email': GET_USER_BY_EMAIL,
    'insert_action_log': INSERT_ACTION_LOG,
    'get_user_by_id': GET_USER_BY_ID,
    'get_role_by_id': GET_ROLE_BY_ID,
    'get_department_by_id': GET_DEPARTMENT_BY_ID,
    'update_user_personal_info': UPDATE_USER_PERSONAL_INFO,
    'get_action_history': GET_ACTION_HISTORY,
    'get_departments': GET_DEPARTMENTS,
    'add_department': ADD_DEPARTMENT,
    'get_department_by_name': GET_DEPARTMENT_BY_NAME,
    'update_department': UPDATE_DEPARTMENT,
    'get_users_ex_admin': GET_USERS_EX_ADMIN,
    'get_roles_names': GET_ROLES_NAMES,
    'get_departments_names': GET_DEPARTMENTS_NAMES,
    'update_user_active_status': UPDATE_USER_ACTIVE_STATUS,
    'update_user_role': UPDATE_USER_ROLE,
    'update_user_department': UPDATE_USER_DEPARTMENT,
    'get_role_id_by_name': GET_ROLE_ID_BY_NAME,
    'get_department_id_by_name': GET_DEPARTMENT_ID_BY_NAME,
    "is_user_available_to_change_role": IS_USER_AVAILABLE_TO_CHANGE_ROLE,
    'get_users_to_add_task': GET_USERS_TO_ADD_TASK,
    'insert_new_task': INSERT_NEW_TASK,
    'get_manager_tasks': GET_MANAGER_TASKS,
    'update_manager_task_status': UPDATE_MANAGER_TASK_STATUS,
    'get_commentaries_for_task': GET_COMMENTARIES_FOR_TASK,
    'insert_commentary_for_task': INSERT_COMMENTARY_FOR_TASK,
}
