from frontend.admin_window import open_admin_window
from frontend.manager_window import open_manager_window
from frontend.executor_window import open_executor_window


ROLES_WINDOWS = {
    1: open_admin_window,
    2: open_manager_window,
    3: open_executor_window,
}


def role_window_decider(root, user_id, role_id):
    ROLES_WINDOWS.get(role_id)(root, user_id)
