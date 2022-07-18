from flask import Flask
from redis import Redis, RedisError
import os
import socket
from imp import reload

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)
@app.route("/")
def hello():
    print('test123')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)