from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)


@app.route('/')
def hello():
   redis.incr('hits')
   return 'Hello from Sani Basak, submitting project for Containerization with Docker!'

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)
