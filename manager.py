from werkzeug.exceptions import HTTPException
from app import create_app
from app.libs.error_code import ServerError
from app.libs.errors import APIException

#创建app对象
app = create_app('develop')

#添加蓝图级别的异常处理
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # TODO log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e

if __name__ == '__main__':
    app.run(debug=True)
