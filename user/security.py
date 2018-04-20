from re import sub
from flask_restful import reqparse, abort, inputs
from functools import wraps
from jwt import decode
from constants import PREFIX, SECRET, DECODE_OPTIONS

def jwt_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            parser = reqparse.RequestParser()
            parser.add_argument('Authorization', type=str, location='headers')
            data = parser.parse_args()

            token = data.get('Authorization')

            if not token or not isinstance(token, str):
                abort(400, message="This request must have an authorization token")

            _validate_token(token)

            return fn(*args, **kwargs)
        return decorator
    return wrapper

def _validate_token(token):
    prefix = PREFIX + ' '

    if not token.startswith(prefix):
        abort(400, message="invalid prefix")

    token_without_prefix = sub(prefix, '', token)

    try:
        decode(token_without_prefix, SECRET, verify=True, options=DECODE_OPTIONS)
    except Exception as err:
        abort(401, message='Unauthorized')
