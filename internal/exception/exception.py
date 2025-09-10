from dataclasses import field
from typing import Any

from pkg.response import HttpCode


class CustomException(Exception):
    """
    自定义异常
    """
    code:HttpCode = HttpCode.FAIL
    message:str = ''
    data:Any = field(default_factory= dict)

    def __init__(self, message:str = "",data: Any = None):
        super().__init__(message)
        self.message = message
        self.data = data


class FailException(CustomException):
    """
    失败异常
    """
    pass

class ForbiddenException(CustomException):
    """
    权限不足异常
    """
    code:HttpCode = HttpCode.FORBIDDEN
    pass

class NotFoundException(CustomException):
    """
    资源不存在异常
    """
    code:HttpCode = HttpCode.NOT_FOUND
    pass

class UnauthorizedException(CustomException):
    """
    未授权异常
    """
    code:HttpCode = HttpCode.UNAUTHORIZED
    pass

class ValidationErrorException(CustomException):
    """
    参数验证异常
    """
    code:HttpCode = HttpCode.VALIDATION_ERROR
    pass

