
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime 

db = SQLAlchemy()


class Employee(db.Model):
    __tablename__ = 'employees'
    emp_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(100), nullable=False)
    vp_name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    attendance_records = db.relationship('Attendance', backref='employee', lazy=True)

    def __init__(self, employee_name, vp_name, department):
        self.employee_name = employee_name
        self.vp_name = vp_name
        self.department = department

    def to_dict(self):
        return {
            'emp_id': self.emp_id,
            'name': self.employee_name,
            'vp_name': self.vp_name,
            'department': self.department
        }

class Attendance(db.Model):
    __tablename__ = 'attendances'
    attendance_id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    employee_id = db.Column(db.Integer, db.ForeignKey('employees.emp_id'), nullable=False)

    def __init__(self, employee_id, day, timestamp):
        self.employee_id = employee_id
        self.day = day
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'attendance_id': self.attendance_id,
            'employee_id': self.employee_id,
            'day': self.day,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
