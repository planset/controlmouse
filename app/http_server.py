#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template

def get_ipaddr():
    '''かなり適当にIP取得・・・'''
    import subprocess
    ipaddr = '127.0.0.1'
    lines = subprocess.check_output(['ifconfig | grep -E "inet\s" | cut -d" " -f2'], shell=True)
    for line in reversed(lines.split('\n')):
        if line == '127.0.0.1':
            break
        ipaddr = line
    return ipaddr

wshost = get_ipaddr()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', wshost=wshost)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


