from celery import Celery, Task
from flask_socketio import SocketIO
from dotenv import load_dotenv
import random
import time
import os


load_dotenv()

celery_app = Celery(__name__)
celery_app.conf.broker_url = os.environ['BROKER_URL']
celery_app.conf.broker_connection_retry_on_startup = True
socket_data = SocketIO(message_queue=os.environ['BROKER_URL'])

@celery_app.task(bind=True)
def stream_data(self: Task, sid):
    i = 1
    while i <= 100:
        value = random.randrange(0, 10000, 1) / 100
        socket_data.emit("new_data", {"value" :  value})
        i += 1
        time.sleep(0.01)
