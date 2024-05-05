from flask import Flask
from flask_socketio import SocketIO
import os
import eventlet
eventlet.monkey_patch(all=False, socket=True)


socket_io = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123qweaA@'

    from .views.task import task
    from . import events

    app.register_blueprint(task, url_prefix='/task')
    socket_io.init_app(app, message_queue=os.environ['BROKER_URL'])

    return app
