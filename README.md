# Student-Management
Simple Student Management system using Flask and Pymongo

# Building
It is best to use python `pipenv shell` tool to build locally:

```bash
 > git clone https://github.com/rvraagusan/Student-Management.git
 > cd STUDENT-MANAGEMENT
 > pipenv install
 > pipenv shell
```

After install virtualenv just run `python app.py` to start at `localhost:5000/` 

# DB Collection 
dump and restore command that used  
```bash
 mongodump --collection=mycollection --db=student_db
```
to restore need to install mongo restore tool after that
```bash
mongorestore --port <port> --db <destination database> --collection <collection-name> <data-dump-path/dbname/collection.bson>
```
# API Endpoints
some of Endpoint listed here
add new student - `/insert_student`
update student - `/student/update/<id>`
delete student - `/student/remove/<id>`
search student - `/student/<id>`
add course - `/add_course`
add teacher - `/add_teacher`
find course teacher - `/find_teacher`
