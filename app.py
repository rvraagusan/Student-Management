from flask import Flask , jsonify, request

from DB import db

database = db.Database()

app = Flask(__name__)

@app.route('/')
def dummy_api():
    return jsonify(data='welcome for Flask API')
@app.route('/insert', methods=['PUT','POST'])
def insert_student():
    _json = request.json
    if request.method == 'PUT':
        msg = database.insert_data('STUDENT', _json)
        return msg
    else:
        return jsonify(message='Insert data properly') 


if __name__ == '__main__':
    app.run(debug=True)