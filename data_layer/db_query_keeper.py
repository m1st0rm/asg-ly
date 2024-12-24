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

QUERIES = {
    'register': REGISTER_USER,
    'login': LOGIN_USER,
    'get_user_by_email': GET_USER_BY_EMAIL,
    'insert_action_log': INSERT_ACTION_LOG
}