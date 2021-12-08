from flask import Flask , jsonify, request, Response

from DB import db

database = db.Database()

app = Flask(__name__)

@app.route('/')
def dummy_api():
    return jsonify(data='welcome for Flask API')

@app.route('/insert_student', methods=['PUT','POST'])
def insert_student():
    _json = request.json
    if request.method == 'PUT':
        msg = database.insert_data('STUDENT', _json)
        return msg, 200
    else:
        return {'message':'Request method in invalid' }, 405

@app.route('/students', methods=['GET'])
def get_students():
    if request.method == 'GET':
        data = database.get_data('STUDENT')
        return data, 200
    else:
        return {'message':'Request method in invalid' }, 405

@app.route('/student/<id>', methods=['GET'])
def get_student(id):
    if request.method=='GET':
        data = database.get_data('STUDENT', id)
        return data, 200
    else : 
        return {'message':'Request method in invalid' }, 405

@app.route('/student/remove/<id>', methods=['DELETE'])
def delete_student(id):
    if request.method=='DELETE':
        resp = database.detele_data('STUDENT', id)
        return resp ,200
    else : 
        return {'message':'Request method in invalid' }, 405

@app.route('/student/update/<id>', methods=['POST'])
def update_student(id):
    _json = request.json
    if request.method == 'POST':
        msg = database.update_data('STUDENT',id , _json)
        return msg , 200
    else:
        return {'message':'Request method in invalid' }, 405

@app.route('/add_teacher', methods=['PUT','POST'])
def insert_teacher():
    _json = request.json
    if request.method == 'PUT':
        msg = database.insert_data('TEACHER', _json)
        return msg, 200
    else:
        return {'message':'Request method in invalid' }, 405

@app.route('/teachers', methods=['GET'])
def get_teachers():
    if request.method == 'GET':
        data = database.get_data('TEACHER')
        return data, 200
    else:
        return {'message':'Request method in invalid' }, 405

@app.route('/teacher/<id>', methods=['GET'])
def get_teacher(id):
    if request.method=='GET':
        data = database.get_data('TEACHER', id)
        return data, 200
    else : 
        return {'message':'Request method in invalid' }, 405

@app.route('/teacher/remove/<id>', methods=['DELETE'])
def delete_teacher(id):
    if request.method=='DELETE':
        resp = database.detele_data('TEACHER', id)
        return resp ,200
    else : 
        return {'message':'Request method in invalid' }, 405

@app.route('/teacher/update/<id>', methods=['POST'])
def update_teacher(id):
    _json = request.json
    if request.method == 'POST':
        msg = database.update_data('TEACHER',id , _json)
        return msg , 200
    else:
        return {'message':'Request method in invalid' }, 405

@app.route('/add_course', methods=['PUT','POST'])
def insert_course():
    _json = request.json
    if request.method == 'PUT':
        msg = database.insert_data('COURSE', _json)
        return msg, 200
    else:
        return {'message':'Request method in invalid' }, 405
@app.route('/find_teacher', methods=['PUT', 'POST'])
def course_view():
    _json = request.json
    code = _json['Course_code']
    if request.method=='POST':
        data = database.course_lookup_db(code)
        return {'Request':_json, 'Results': data }
    else:
        return {'message':'Request method in invalid' }, 405


if __name__ == '__main__':
    app.run(debug=True)