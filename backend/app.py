# app.py
from flask import Flask, Blueprint, render_template, jsonify, request, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from apis.ted import ted_api
from flask_restplus import Api
import os
from maintenance import not_under_maintenance, UnderMaintenanceException

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
os.environ["db_uri"] = Config.SQLALCHEMY_DATABASE_URI 


@app.errorhandler(UnderMaintenanceException)
def handle_maintenance(e):
    return jsonify({"status": "error", "maintenance": True, "message": "Server is under maintenance!"}), 503


# API v1
apiV1BP = Blueprint('apiV1', __name__, url_prefix='/api/v1')
apiV1 = Api(apiV1BP, title='TED API', version='1.0')
apiV1.add_namespace(ted_api)
app.register_blueprint(apiV1BP)



# Web Pages
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")




# include this for local dev
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8008, debug=True)
    # app.run(host='0.0.0.0', ssl_context='adhoc')  # For https
