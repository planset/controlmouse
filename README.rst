=================================
iphoneからMacのマウスを操作する
=================================


対象環境
=========
* mac os x 10.8.2
* python 2.7.3
* virtualenv
* mkvirtualenv


準備
==========
flask, tornadoをインストールします。
::

    mkvirtualenv controlmouse
    pip install flask
    pip install tornado


実行
====

1. terminalを２つ起動しておきます。
2. terminalの１つ目::

    cd controlmouse/app
    workon controlmouse
    python http_server.py

3. terminalの２つ目::

    cd controlmouse/app
    workon controlmouse
    python ws_server.py

4. iphoneのsafariで http://MacのIP:5000/ を開く。




