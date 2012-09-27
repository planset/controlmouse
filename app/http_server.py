#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import (Flask, request, session, g, redirect,
        url_for, render_template, flash,
        send_from_directory, abort,
        render_template, flash, send_from_directory,
        render_template_string)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


