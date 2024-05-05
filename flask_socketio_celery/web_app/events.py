from task_app.task import stream_data
from flask import request

from . import socket_io


@socket_io.on("start_data_stream")
def start_data_stream():
    stream_data.delay(request.sid)
