from tasks import grabPic,GetAll
from flask import Flask, url_for, render_template, request, jsonify, make_response
import io, os, json, time
import requests, io, os, json
import base64
from flask_sqlalchemy import SQLAlchemy
from models import MyModel
from base64 import decodestring
from config import app
from PIL import Image
from io import BytesIO

def getHistory():
    return ''

@app.route("/")
def index():
    data=  GetAll()
    return render_template('index.html',current_place=data)


@app.route("/grabScreenshot" , methods=["GET","POST"])
def getPic():
    webAddress = request.form['webAddress']
    result = grabPic.delay(webAddress)
    result.ready()
    # print(result.backend)
    imgBackend= result.get(timeout=5)
    data = {}
    data['img'] = base64.encodebytes(imgBackend['content']).decode("utf-8")
    # print(json.dumps(data))
    return render_template('index.html', encode_image = data['img'] , name=imgBackend['time'],current_place=imgBackend['data'] )


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


with app.test_request_context():
    print(url_for('index'))
    print(url_for('getPic'))
   

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)


