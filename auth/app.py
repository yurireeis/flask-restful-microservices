from flask import Flask
from flask_jwt import JWT
from os import getenv
from security import authenticate, identity

app = Flask(__name__)
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)
app.config['JWT_AUTH_HEADER_PREFIX'] = getenv('PREFIX', 'Bearer ')
app.config['SECRET_KEY'] = getenv('SECRET', 'tdc')
api = Api(app)
jwt = JWT(app, authenticate, identity)

@jwt.jwt_payload_handler
def customized_jwt_payload_handler(identity):
    identity = getattr(identity, 'username') or identity['username']
    return {'identity': identity}

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    payload = identity.json()
    payload['access_token'] = access_token.decode('utf-8')
    return jsonify(payload)


if __name__ == '__main__':
    app.run(debug=True)
