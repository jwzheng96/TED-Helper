from functools import wraps
import os


class UnderMaintenanceException(Exception):
    pass


def not_under_maintenance(api_function):
    @wraps(api_function)
    def decorated_function(*args, **kwargs):
        if os.getenv("MAINTENANCE"):
            return {"status": "error", "maintenance": True, "message": "Server is under maintenance!"}
        return api_function(*args, **kwargs)
    return decorated_function


def check_maintenance():
    if os.getenv("MAINTENANCE"):
        raise UnderMaintenanceException("Server is under maintenance!")
