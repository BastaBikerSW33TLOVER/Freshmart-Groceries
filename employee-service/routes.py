from flask import Blueprint, request, jsonify
from controller import EmployeeController

employee_routes = Blueprint('employee_routes', __name__)

@employee_routes.route('/employees', methods=['GET'])
def get_all_employees():
    try:
        employees = EmployeeController.get_all_employees()
        return jsonify({"data": employees}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@employee_routes.route('/employees', methods=['POST'])
def create_employee():
    try:
        data = request.json
        employee = EmployeeController.create_employee(data)
        return jsonify({"message": "Employee created successfully", "data": employee}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400