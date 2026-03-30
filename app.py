from flask import Flask

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    return {'users': []}

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    return {'user': id}

@app.route('/api/login', methods=['POST'])
def login():
    return {'token': 'abc123'}
