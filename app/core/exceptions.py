class BaseAppException(Exception):
    pass

class NotFoundException(BaseAppException):
    pass

class AlreadyExistsException(BaseAppException):
    pass

class PermissionDeniedException(BaseAppException):
    pass