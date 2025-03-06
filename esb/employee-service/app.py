from flask import Flask
from routes import employee_routes

app = Flask(__name__)
app.config.from_object('config.Config')

# Register the routes
app.register_blueprint(employee_routes)

if __name__ == '__main__':
    app.run(debug=True)
