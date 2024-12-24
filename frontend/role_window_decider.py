from frontend.admin_window import open_admin_window


ROLES_WINDOWS = {
    1: open_admin_window,
}


def role_window_decider(root, user_id, role_id):
    ROLES_WINDOWS.get(role_id)(root, user_id)
