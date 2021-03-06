import pymysql
from flask import Flask
from datetime import timedelta
from flask_jwt import JWT
from constants import DB_USER, DB_PASS, DB_HOST, DB_NAME, PREFIX, SECRET
from security import authenticate, identity
from db import db

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)
app.config['JWT_AUTH_HEADER_PREFIX'] = PREFIX
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET

jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=False, host="0.0.0.0", port=80)
