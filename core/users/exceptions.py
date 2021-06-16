from core.exceptions import ServiceException

class WrongCredentialsException(ServiceException):
    status_code = 401
    error_message = 'wrong pair login/password'
