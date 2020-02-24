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
    # print(data)
    #   image
    # binary_values = a_binary_string.split(" ")
    # image.show()
    # my_string = base64.b64encode(image[0])
    # buffered = BytesIO()
    # image.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue())
    # print(img_str)
    # AllPic =  Model.GetPicturs()
    # result =  grabPic.apply_async(countdown=10)
    # result =  GetAll.delay()
    # result.ready()
    # imgBackend= result.get()
    # print(imgBackend)
    # data['img'] = base64.encodebytes(imgBackend['content']).decode("utf-8")
    # for pic in AllPic:
    #     current_place = {
    #         'imgFile' : base64.encodebytes(pic[0]).decode("utf-8"),
    #         'name' : pic[1]
    #     }
    # arry = []
    # for pic in AllPic:
    #     res = AsyncResult(pic[0],app=app)
    #     res.state
    #     print(res.get())
        # pic[0].tos
        # arry.append(base64.encodebytes(pic[0]).decode("utf-8"))
        # image = Image.open(io.BytesIO(pic[0]))
        # print(pic[0])
        # arry.append(Image.open(io.BytesIO(pic[0])))
        # arry.append(pic[0])
        # for f in pic:
            # print(f[0])
    return render_template('index.html',current_place=data)
    # return render_template('index.html')


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
    return render_template('index.html', encode_image = data['img'] , name=imgBackend['time'] )


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


with app.test_request_context():
    print(url_for('index'))
    print(url_for('getPic'))
   

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)


