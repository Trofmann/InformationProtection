import json

import uvicorn
from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

from lab1 import Coder as Lab1Coder
from lab2 import Coder as Lab2Coder
from lab3 import Coder as Lab3Coder
from lab4 import Coder as Lab4Coder
from lab5 import Coder as Lab5Coder
from lab6 import Coder as Lab6Coder

app = FastAPI()


@app.get("/")
def read_root():
    return FileResponse('interface.html')


@app.post('/encode')
def encode(data=Body()):
    kind = data['kind']  # type: str
    key = data['key']  # type: str
    open_text = data['open_text']  # type: str

    result = ''  # type: str
    # Пока только для ЛБ1
    if kind == 'lab1':
        key = json.loads(key)  # type: dict
        coder = Lab1Coder(key)
        result = coder.encode(msg=open_text)
    elif kind == 'lab2':
        key = list(map(int, key.split()))  # type: list
        coder = Lab2Coder(key)
        result = coder.encode(open_text)
    elif kind == 'lab3':
        coder = Lab3Coder()
        result = coder.encode(open_text)
    elif kind == 'lab4':
        coder = Lab4Coder(key)
        result = coder.encode(open_text)
    elif kind == 'lab5':
        coder = Lab5Coder(key)
        result = coder.encode(open_text)
    elif kind == 'lab6':
        coder = Lab6Coder(key)
        result = coder.encode(open_text)

    return {'result': result}


@app.post('/decode')
def decode(data=Body()):
    kind = data['kind']  # type: str
    key = data['key']  # type: str
    encoded_text = data['encoded_text']  # type: str

    result = ''  # type: str

    if kind == 'lab1':
        key = json.loads(key)  # type: dict
        coder = Lab1Coder(key)
        result = coder.decode(msg=encoded_text)
    elif kind == 'lab2':
        key = list(map(int, key.split()))  # type: list
        coder = Lab2Coder(key)
        result = coder.decode(encoded_text)
    elif kind == 'lab3':
        coder = Lab3Coder()
        result = coder.decode(encoded_text)
    elif kind == 'lab4':
        coder = Lab4Coder(key)
        result = coder.decode(encoded_text)
    elif kind == 'lab5':
        coder = Lab5Coder(key)
        result = coder.decode(encoded_text)
    elif kind == 'lab6':
        coder = Lab6Coder(key)
        result = coder.decode(encoded_text)

    return {'result': result}


uvicorn.run(app)
