from flask import Flask, render_template
from flask_sock import Sock
from math_func import *

app = Flask(__name__)
sock = Sock(app)


@app.route('/')
def index():
    return render_template('index.html')



@sock.route('/data')
def ws(sock):
    while True:
        data = sock.receive()
        global v;global p
        v,p = update_vecteur(data,v,p)






app.run(host='192.168.0.115', port=8081, debug=True)
