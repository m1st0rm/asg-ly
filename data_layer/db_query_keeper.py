REGISTER_USER = """
    INSERT INTO public.users (first_name, last_name, email, password_hash, role_id, department_id)
    VALUES (%s, %s, %s, %s, 3, NULL);
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

QUERIES = {
    'register': REGISTER_USER,
    'login': LOGIN_USER,
    'get_user_by_email': GET_USER_BY_EMAIL
}