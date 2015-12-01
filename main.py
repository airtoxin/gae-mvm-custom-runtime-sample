#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__, static_folder='static')

@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route("/_ah/start")
def _ah_start():
    return "ok"

@app.route("/_ah/health")
def _ah_health():
    return "ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
