from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str
    email: str
    role_id: int
    department_id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

