import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip():
    import socket
    return socket.gethostbyname(socket.gethostname())

@app.route('/', methods=['POST'])
def stress_cpu():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return {"message": "CPU stress initiated"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

