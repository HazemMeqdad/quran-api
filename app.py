from flask import Flask
import views
from flask_cors import CORS


app = Flask(__name__, instance_relative_config=True)
CORS(app)

@app.route("/test")
def test():
    return "test"


app.config.from_pyfile("config.py")
app.secret_key = app.config["SECRET_KEY"]

app.register_blueprint(views.index)
app.register_blueprint(views.moshaf)
app.register_blueprint(views.readers)
app.register_blueprint(views.azkar)

if __name__ == "__main__":
    app.run(debug=True, port=3)
