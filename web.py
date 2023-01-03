from flask import Flask
from app.DependencyContainer import DependencyContainer

app = DependencyContainer()

app_name = app.config().get('APP', 'name')


app = Flask(__name__)


@app.route('/')
def landing():

    return '<p>Welcome to <b>' + app_name + '</b></p>'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080
    )