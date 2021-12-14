from flask import Blueprint, jsonify, request, Response
from DB import db

teacher_api = Blueprint('teacher', __name__)
database = db.Database()

@teacher_api.route('/add_teacher', methods=['PUT','POST'])
def insert_teacher():
    _json = request.json
    if request.method == 'PUT':
        msg = database.insert_data('TEACHER', _json)
        return msg, 200
    else:
        return {'message':'Request method in invalid' }, 405


@teacher_api.route('/teachers', methods=['GET'])
def get_teachers():
    if request.method == 'GET':
        data = database.get_data('TEACHER')
        return data, 200
    else:
        return {'message':'Request method in invalid' }, 405


@teacher_api.route('/teacher/<id>', methods=['GET'])
def get_teacher(id):
    if request.method=='GET':
        data = database.get_data('TEACHER', id)
        return data, 200
    else : 
        return {'message':'Request method in invalid' }, 405


@teacher_api.route('/teacher/remove/<id>', methods=['DELETE'])
def delete_teacher(id):
    if request.method=='DELETE':
        resp = database.detele_data('TEACHER', id)
        return resp ,200
    else : 
        return {'message':'Request method in invalid' }, 405


@teacher_api.route('/teacher/update/<id>', methods=['POST'])
def update_teacher(id):
    _json = request.json
    if request.method == 'POST':
        msg = database.update_data('TEACHER',id , _json)
        return msg , 200
    else:
        return {'message':'Request method in invalid' }, 405