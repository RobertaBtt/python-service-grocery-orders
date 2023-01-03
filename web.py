from flask import Flask
from app.DependencyContainer import DependencyContainer

app = DependencyContainer()

app_name = app.config().get('APP', 'name')


flask_app = Flask(__name__)


@flask_app.route('/')
def landing():
    result = app.service_grocery().get_all_orders()
    return app.serializer().convert(result)


flask_app.run(
        host='0.0.0.0',
        port=8080
)