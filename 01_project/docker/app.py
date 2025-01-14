import socket
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    return 'Some test! Here is {}\n'.format(hostname)