from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def alertmanager_webhook():
    subprocess.call(['ansible-playbook', '/ansible/restart_nginx.yml'])
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
