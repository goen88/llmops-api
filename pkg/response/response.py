from dataclasses import dataclass, field
from typing import Any

from flask import jsonify

from .http_code import HttpCode


@dataclass
class Response:
    '''
        基础http响应格式
    '''

    code: HttpCode = HttpCode.SUCCESS
    message: str = ''
    data: Any = field(default_factory=dict)


def json(data: Response):
    '''基础响应接口'''
    return jsonify(data), 200


def success_json(data: Any):
    '''成功响应接口'''
    return json(Response(code=HttpCode.SUCCESS, message='', data=data))


def fail_json(data: Any):
    '''失败响应接口'''
    return json(Response(code=HttpCode.FAIL, message='', data=data))


def validation_error_json(errors: dict = None):
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ''

    '''验证失败响应接口'''
    return json(Response(code=HttpCode.VALIDATION_ERROR, message=msg, data=errors))


def message(code: HttpCode, msg: str):
    '''基础消息响应,固定消息提示，数据为固定为空字典'''
    return json(Response(code=code, message=msg, data={}))

def success_message(msg: str):
    '''成功消息响应,固定消息提示，数据为固定为空字典'''
    return message(HttpCode.SUCCESS, msg)


def fail_message(msg: str):
    '''失败消息响应,固定消息提示，数据为固定为空字典'''
    return message(HttpCode.FAIL, msg)


def unauthorized_message(msg: str):
    '''未授权消息响应,固定消息提示，数据为固定为空字典'''
    return message(HttpCode.UNAUTHORIZED, msg)


def forbidden_message(msg: str):
    '''禁止访问消息响应,固定消息提示，数据为固定为空字典'''
    return message(HttpCode.FORBIDDEN, msg)


def not_found_message(msg: str):
    '''未找到消息响应,固定消息提示，数据为固定为空字典'''
    return message(HttpCode.NOT_FOUND, msg)
