from flask import Flask
import views
from flask_cors import CORS


app = Flask(__name__, instance_relative_config=True)
CORS(app)


app.config.from_pyfile("config.py")
app.secret_key = app.config["SECRET_KEY"]

app.register_blueprint(views.index)
app.register_blueprint(views.moshaf)
app.register_blueprint(views.reciters)
app.register_blueprint(views.azkar)
app.register_blueprint(views.pray)

app.register_error_handler(404, views.errors.page_not_found)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
