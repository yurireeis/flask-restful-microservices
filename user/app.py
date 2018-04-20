import pymysql
from flask import Flask
from flask_restful import Api
from constants import DB_USER, DB_PASS, DB_HOST, DB_NAME, PREFIX, SECRET
from resources.user import User
from db import db

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
api.add_resource(User, '/users', '/users/<int:_id>', endpoint='user')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=False, host="0.0.0.0", port=80)
