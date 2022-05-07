import pathlib
from flask import Blueprint, Response
import random
import os

streams = Blueprint('streams', __name__)


@streams.route('/streams')
def index():
    return 'streams'

def make_stream(path):
    files = os.listdir(path)
    file = path + "/" + random.choice(files)
    if not pathlib.Path(file).exists():
        return 
    with open(file, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                make_stream(path)
            yield data

def get_surah_number_as_format(number: int):
    if number < 10:
        return f'00{number}'
    elif number < 100:
        return f'0{number}'
    else:
        return f'{number}'

@streams.route('/streams/abdulbasit-abdussamad')
def stream():
    return Response(make_stream("cdn/reciters/abdulbasit-abdussamad"), mimetype="audio/mpeg")
