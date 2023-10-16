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
from lab7 import Coder as Lab7Coder
from lab8 import Coder as Lab8Coder
from lab9_1 import Coder as Lab91Coder
from lab9_2 import Coder as Lab92Coder

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
    elif kind == 'lab2':
        key = list(map(int, key.split()))  # type: list
        coder = Lab2Coder(key)
    elif kind == 'lab3':
        coder = Lab3Coder()
    elif kind == 'lab4':
        coder = Lab4Coder(key)
    elif kind == 'lab5':
        coder = Lab5Coder(key)
    elif kind == 'lab6':
        coder = Lab6Coder(key)
    elif kind == 'lab7':
        coder = Lab7Coder(key)
    elif kind == 'lab8':
        coder = Lab8Coder(key)
    elif kind == 'lab9_1':
        coder = Lab91Coder(key)
    elif kind == 'lab9_2':
        coder = Lab92Coder(key)
    else:
        raise Exception('Неизвестная ЛБ')
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
    elif kind == 'lab2':
        key = list(map(int, key.split()))  # type: list
        coder = Lab2Coder(key)
    elif kind == 'lab3':
        coder = Lab3Coder()
    elif kind == 'lab4':
        coder = Lab4Coder(key)
    elif kind == 'lab5':
        coder = Lab5Coder(key)
    elif kind == 'lab6':
        coder = Lab6Coder(key)
    elif kind == 'lab7':
        coder = Lab7Coder(key)
    elif kind == 'lab8':
        coder = Lab8Coder()
    elif kind == 'lab9_1':
        coder = Lab91Coder()
    elif kind == 'lab9_2':
        coder = Lab92Coder()
    else:
        raise Exception('Неизвестная ЛБ')
    result = coder.decode(encoded_text)

    return {'result': result}


uvicorn.run(app)
