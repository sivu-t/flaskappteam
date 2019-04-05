# Referencing the modules
from flask_sqlalchemy import SQLAlchemy
from src.flaskbasic.models import Student
from src.flaskbasic.form import StudentForm
from src.flaskbasic.wsgi import db
# from src.flaskbasic.wsgi import Student
import os


class Functions():
# 
#       def signup(username, email, newpassword, confirm):
#         form = SignUp()
#         new_user = Auth(username=form.username.data, email=form.email.data, newpassword=form.password.data, confirm=form.confirmpassword.data)
#         db.session.create(new_user)
#         db.session.commit()
#
#       def login(email,password):
#         form = Login()
#         if request.form['password'] == 'password' and request.form['email'] == 'email':
#          session['logged_in'] = True
# #     else:
# #         flash('wrong password!')
#     # return redirect(url_for('login.html'))
#       #   email = request.form['email']
#         password = functions.generate_password_hash(request.form['password'])
#         user_id = functions.check_user_exists(email, password)

      # create the data in the database
      def putData():
            form = StudentForm()
            student = Student(name=form.name.data, physics=form.physics.data, maths=form.maths.data,chemistry=form.chemistry.data,)
            db.session.add(student)
            db.session.commit()

      # read all the data in the database

      def readData():
            results = Student.query.all()
            return results

      # get the learner in  the database by Id
      def readName(learner,student_id):
            studentname = Student.query.filter_by(name=learner, id=student_id).all()
            for student_name in studentname:
                  return student_name.name

      #  read data by all the attributes
      def readResults(student_id,learner,physcalS, mathematics, chem ):
            studentname = Student.query.filter_by(id=student_id, name=learner, physics=physcalS, maths= mathematics, chemistry=chem     ).all()
            for student_name in studentname:
                  return student_name.id,student_name.name,student_name.physics,student_name.maths,student_name.chemistry

      # delete the data in the database by id
      def delete(student_id):
            student_results = Student.query.get_or_404(student_id)
            db.session.delete(student_results)
            db.session.commit()

      # delete all the data in the database
      def resetResults():
          db.drop_all()
