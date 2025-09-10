from enum import Enum

class HttpCode(str, Enum):
    '''
        Http 基础业务状态码
        状态码列表如下：
            success // 成功
            fail // 失败
            not_found // 资源不存在
            unauthorized // 未授权
            forbidden // 无权限
            validation_error // 参数验证错误
    '''
    SUCCESS  = 'success' # 成功
    FAIL = 'fail' # 失败
    NOT_FOUND = 'not_found' # 资源不存在
    UNAUTHORIZED = 'unauthorized' # 未授权
    FORBIDDEN = 'forbidden' # 无权限
    VALIDATION_ERROR = 'validation_error' # 参数验证错误
