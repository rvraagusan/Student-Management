from flask import Flask , jsonify, request, Response

from DB import db
from API.controllers.student import student_api
from API.controllers.teacher import teacher_api
from API.controllers.course import courses_api

database = db.Database()

app = Flask(__name__)

@app.route('/')
def dummy_api():
    return jsonify(data='welcome for Flask API')

app.register_blueprint(student_api)
app.register_blueprint(teacher_api)
app.register_blueprint(courses_api)


if __name__ == '__main__':
    app.run(debug=True)