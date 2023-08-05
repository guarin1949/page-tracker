# src/page_tracker/app.py

import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)
# redis = Redis(port=9736)


@app.get("/")
def index():
    # page_views = redis().incr("page_views")
    # return f"This page has been seen {page_views} times."
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{pensive face}", 500
    else:
        return f"This page has been seen {page_views} times."


@cache
def redis():
    # return Redis(port=9736)
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:9736"))
