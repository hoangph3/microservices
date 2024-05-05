from web_app import create_app, socket_io
from dotenv import load_dotenv


app = create_app()


@app.before_request
def before_request():
    pass


@app.after_request
def after_request(response):
    return response


if __name__ == '__main__':
    load_dotenv()
    socket_io.run(app, host="0.0.0.0", port=8080, debug=True)
