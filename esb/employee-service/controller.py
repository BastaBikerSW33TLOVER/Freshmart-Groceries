from models import PersonalInfo
from bson import ObjectId

class EmployeeController:
    @staticmethod
    def create_employee(data):
        try:
            # Validate required fields
            required_fields = ["name", "date_of_birth", "contact_number", "emergency_contact_number"]
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Missing required field: {field}")

            # Create and save the employee
            employee = PersonalInfo(
                name=data["name"],
                date_of_birth=data["date_of_birth"],
                contact_number=data["contact_number"],
                emergency_contact_number=data["emergency_contact_number"]
            )
            employee.save()

            # Return the created employee data
            return {
                "name": employee.name,
                "date_of_birth": employee.date_of_birth,
                "contact_number": employee.contact_number,
                "emergency_contact_number": employee.emergency_contact_number
            }
        except Exception as e:
            raise Exception(f"Error creating employee: {str(e)}")

    @staticmethod
    def get_employee_by_id(employee_id):
        try:
            # Convert string ID to ObjectId
            obj_id = ObjectId(employee_id)
            employee = PersonalInfo.get_by_id(obj_id)
            
            if employee:
                return {
                    "name": employee.name,
                    "date_of_birth": employee.date_of_birth,
                    "contact_number": employee.contact_number,
                    "emergency_contact_number": employee.emergency_contact_number
                }
            return None
        except Exception as e:
            raise Exception(f"Error fetching employee: {str(e)}")

    @staticmethod
    def get_all_employees():
        try:
            employees = PersonalInfo.get_all()
            return [{
                "name": emp["name"],
                "date_of_birth": emp["date_of_birth"],
                "contact_number": emp["contact_number"],
                "emergency_contact_number": emp["emergency_contact_number"]
            } for emp in employees]
        except Exception as e:
            raise Exception(f"Error fetching employees: {str(e)}")
