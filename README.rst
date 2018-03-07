=================================
iphoneからMacのマウスを操作する
=================================


対象環境
=========
* python 2.7.3+
* virtualenv
* ifconfig


準備
====
::

    git clone https://github.com/planset/controlmouse
    cd controlmouse
    virtualenv env
    source env/bin/activate
    pip install tornado


実行
====

1. terminalを起動します。::

    cd controlmouse
    source env/bin/activate
    cd app
    python server.py

2. iphoneのsafariで http://MacのIP:5000/ を開く。
