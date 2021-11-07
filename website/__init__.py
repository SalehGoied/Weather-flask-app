from flask import Flask
from flask_cors import CORS
from .views import views

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '**********'




app.register_blueprint(views, url_prefix=('/'))

    