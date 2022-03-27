from flask import Blueprint, Response


readers = Blueprint('reders', __name__, url_prefix="/readers")


@readers.route('/')
def index():
    def stream():
        with open("readers/Mishary_Alafasy/001.mp3", "rb") as fwav:
            data = fwav.read(1024)
            while True:
                data = fwav.read(1024)
                yield data
    return Response(stream(), mimetype="audio/mpeg")

