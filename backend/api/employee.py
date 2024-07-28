# from flask_restful import Resource
from flask import request, jsonify
from . import api_blueprint
from models import db, Employee

@api_blueprint.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    employee_name = data['employee_name']
    vp_name = data['vp_name']
    department = data['department']

    employee = Employee(employee_name, vp_name, department)
    db.session.add(employee)
    db.session.commit()

    return jsonify({"message": "Employee created successfully", "employee": employee.to_dict()})

@api_blueprint.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.to_dict() for employee in employees])
