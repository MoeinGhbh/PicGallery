from celery import Celery
import datetime , requests, psycopg2, io
from flask_sqlalchemy import SQLAlchemy
import base64
from celery.result import AsyncResult
from models import MyModel 
from config import app
from PIL import Image

app = Celery('tasks', broker='redis://localhost//', backend='db+postgresql://postgres:123@localhost/mydatabase')

@app.task
def grabPic(webaddress):
    sec = requests.get("http://image.thum.io/get/?url=http%3A%2F%2F{}%2F".format(webaddress), stream=True)
    # sec = requests.get("https://image.thum.io/get/auth/7730-moein/https://{}/".format(webaddress), stream=True)
    # print(sec)
    # image = base64.encodebytes(sec.content).decode("utf-8")
    # image = Image.open(io.BytesIO(sec.content))
    # image = image.convert("RGB")
    # dd = io.BytesIO(sec.content)
    MyModel.update(sec.content)
    response = {
            'content': sec.content,
            'time': datetime.datetime.now()
        }
    return response

@app.task
def GetAll():
    AllPic =  MyModel.GetPicturs()
    # for pic in AllPic:
        # res = AsyncResult(pic[0],app=app)
        # print(res.state)
        # print(res)
        #  res.get()
    data=[]
    for pic in AllPic:
        # p1 = pic[0]
        # p2 = eval(p1)
        # print(p2)
        # data.append(pic)
        data.append(pic[0])
        # data['pic'] = pic[0]
        # data['date_time'] = pic[1]
    return data

