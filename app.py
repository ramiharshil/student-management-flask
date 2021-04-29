import flask
from flask import flask, request, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)



# Student Class/Model
class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=False)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.Integer)
  discord = db.Column(db.String(100), unique=True)
  role = db.Column(db.String(10))
  

  def __init__(self, name, email, password, discord, role):
    self.name = name
    self.email = email
    self.password = password
    self.discord = discord
    self.role = role

# Student Schema
class StudentSchema(ma.Schema):
  class Meta:
    fields = ('id','name','email','password','discord','role')

# Init schema
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


# Create a student
@app.route('/student', methods=['POST'])
def create_student():
  name = request.json['name']
  email = request.json['email']
  password = request.json['password']
  discord = request.json['discord']
  role = request.json['role']

  new_student = Student(name, email, password, discord, role)

  db.session.add(new_student)
  db.session.commit()

  return student_schema.jsonify(new_student)

# Get All Students
@app.route('/student', methods=['GET'])
def get_students():
  all_students = Student.query.all()
  result = students_schema.dump(all_students)
  #return jsonify(result.data)
  return jsonify(result)


# Get Single Products
@app.route('/student/<id>', methods=['GET'])
def get_student(id):
  student = Student.query.get(id)
  return student_schema.jsonify(student)

# Update a Student
@app.route('/student/<id>', methods=['PUT'])
def update_student(id):
  student = Student.query.get(id)

  name = request.json['name']
  email = request.json['email']
  password = request.json['password']
  discord = request.json['discord']
  role = request.json['role']

  student.name = name
  student.email = email
  student.password = password
  student.discord = discord
  student.role = role

  db.session.commit()

  return student_schema.jsonify(student)


# Delete Student
@app.route('/student/<id>', methods=['DELETE'])
def delete_student(id):
  student = Student.query.get(id)
  db.session.delete(student)
  db.session.commit()

  return student_schema.jsonify(student)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5001)

