from flask import Blueprint, jsonify, request, Response
from DB import db

courses_api = Blueprint('courses', __name__)
database = db.Database()

@courses_api.route('/add_course', methods=['PUT','POST'])
def insert_course():
    _json = request.json
    if request.method == 'PUT':
        msg = database.insert_data('COURSE', _json)
        return msg, 200
    else:
        return {'message':'Request method in invalid' }, 405
@courses_api.route('/find_teacher', methods=['PUT', 'POST'])
def course_view():
    _json = request.json
    code = _json['Course_code']
    if request.method=='POST':
        data = database.course_lookup_db(code)
        return {'Request':_json, 'Results': data }
    else:
        return {'message':'Request method in invalid' }, 405