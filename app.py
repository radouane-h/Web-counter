import time
from datetime import datetime

import redis
from flask import Flask, render_template, jsonify

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379, decode_responses=True)

START_TIME = datetime.utcnow()


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


def redis_info():
    try:
        info = cache.info()
        return {
            "status": "connected",
            "version": info.get("redis_version", "—"),
            "used_memory": info.get("used_memory_human", "—"),
            "uptime_days": info.get("uptime_in_days", 0),
            "connected_clients": info.get("connected_clients", 0),
        }
    except redis.exceptions.ConnectionError:
        return {"status": "disconnected"}


@app.route('/')
def index():
    count = get_hit_count()
    info = redis_info()
    uptime = str(datetime.utcnow() - START_TIME).split('.')[0]
    return render_template('index.html', count=count, info=info, uptime=uptime)


@app.route('/api/stats')
def stats():
    """JSON endpoint for live stats polling."""
    try:
        count = int(cache.get('hits') or 0)
    except redis.exceptions.ConnectionError:
        count = -1
    info = redis_info()
    return jsonify(hits=count, redis=info, uptime=str(datetime.utcnow() - START_TIME).split('.')[0])


@app.route('/reset', methods=['POST'])
def reset():
    try:
        cache.set('hits', 0)
        return jsonify(ok=True)
    except redis.exceptions.ConnectionError:
        return jsonify(ok=False, error='Redis unavailable'), 503


@app.errorhandler(500)
def server_error(e):
    return render_template('error.html', error=str(e)), 500
