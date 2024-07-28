from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from config import DevelopementConfig, Config
from flask_migrate import Migrate
from flask_restful import Api
from api import api_blueprint  # Import the blueprint
import boto3
import time
# from s3utils import upload_to_s3, list_from_s3

from models import Employee, Attendance, db


from api.employee import create_employee


app = Flask(__name__)
app.config.from_object(DevelopementConfig)
app.config.from_object(Config)

#  Database initialization
db.init_app(app)

migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    inspector = inspect(db.engine)
    if not inspector.has_table('employees'):
        Employee.__table__.create(db.engine)
    if not inspector.has_table('attendances'):
        Attendance.__table__.create(db.engine)

#  Security
# security = Security(app,datastore)

#   API Initialization
api = Api(app)

# ------------------------

app.app_context().push()


app.register_blueprint(api_blueprint, url_prefix='/api')  # Register the blueprint
# CORS ENABLE
# CORS(app, supports_credentials=True)

@app.route("/new")
def checking():
    return render_template('attendence.html')

# @app.route('/submit_attendance', methods=['POST'])
# def submit_attendance():
#     data = request.json
#     employee_name = data['employee_name']
#     vp_name = data['vp_name']
#     department = data['department']
#     day = data['day']
#     timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

#     record = {
#         'employee_name': employee_name,
#         'vp_name': vp_name,
#         'department': department,
#         'day': day,
#         'timestamp': timestamp
#     }

#     s3_key = f"attendance/{employee_name}_{day}.json"
#     upload_to_s3(record, s3_key)

#     return jsonify({"message": "Attendance recorded successfully"})

# @app.route('/attendance_records', methods=['GET'])
# def get_attendance_records():
#     records = list_from_s3('attendance/')
#     return jsonify(records)


if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
