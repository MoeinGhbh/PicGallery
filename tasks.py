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
    MyModel.update(sec.content)
    data = GetHistory()
    response = {
            'content': sec.content,
            'time': datetime.datetime.now(),
            'data':data
        }
    return response

@app.task
def GetAll():
    data = GetHistory()
    return data

def GetHistory():
    AllPic =  MyModel.GetPicturs()
    data=[]
    for pic in AllPic:
        data.append(pic[0])
    return data

