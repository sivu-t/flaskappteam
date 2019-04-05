from flask import Flask,render_template, redirect, url_for,request, jsonify, abort,request,flash
from flask_sqlalchemy import SQLAlchemy
from src.flaskbasic import *
from src.flaskbasic.form import StudentForm, RegisterForm, LoginForm
from src.flaskbasic.models import Student, Users
from flask_login import login_user, current_user, login_required, logout_user

import sys
import logging


# logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
_logger_adding = logging.getLogger('Adding results')
_logger_getting = logging.getLogger('Get results')
_logger_update = logging.getLogger('Update results')
_logger_delete = logging.getLogger('Delete results')


# route that renders when the page loads, register a user/ admin
@login.user_loader
def load_user(user_id):
    return Users.query.filter(Users.id == int(user_id)).first()

# add student marks
@application.route('/add_results', methods=['GET','POST'])
# @login_required
def add_results():
    form = StudentForm()
    _logger_adding.warning("Inside Add Results function")
    _logger_adding.warning("Student form waiting for Input")
    if form.validate_on_submit():
      _logger_adding.warning("When form is submitted with data")
      student = Student(name=form.name.data, physics=form.physics.data, maths=form.maths.data,chemistry=form.chemistry.data,)
      _logger_adding.warning("Student: {} , physics: {} , maths: {}, chemistry: {}".format(form.name.data,form.physics.data,form.maths.data,form.chemistry.data))
      db.session.add(student)
      _logger_adding.warning('student results was added to database')
      db.session.commit()
      _logger_adding.warning("database commit")
      return redirect(url_for("add_results"))
    else:
      return render_template('home.html', form=form)

# get all the data from the database

@application.route('/results', methods=['GET','POST'])
def get_results():
  _logger_getting.warning('retrieving all student results')
  data = Student.query.all()
  _logger_getting.warning('the students results have been collected for {}'.format(data))
  return render_template('results.html', data = data)

# route that edit the existing data in the database

@application.route('/edit_results/<int:student_id>', methods=['GET','POST'])
@login_required
def edit_student(student_id):
  form = StudentForm()
  data = Student.query.get_or_404(student_id)
  return render_template('edit_results.html',data=data)

# update the existing data in the database

@application.route('/edit_results/<int:student_id>/update_results',methods=['GET','PUT','POST'])
@login_required
def update_results(student_id):
  student_data = Student.query.get_or_404(student_id)
  form = StudentForm()
  if form.validate_on_submit():
    student_data.name = form.name.data
    student_data.physics = form.physics.data
    student_data.maths = form.maths.data
    student_data.chemistry = form.chemistry.data
    db.session.commit()
    flash('Your results were successfully Updated')
    return redirect(url_for('get_results', student_id=student_data.id))
  elif request.method == 'GET':
    form.name.data = student_data.name
    form.physics.data = student_data.physics
    form.maths.data = student_data.maths
    form.chemistry.data = student_data.chemistry
  # return render_template('edit_results.html', student_data=student_data)
  return render_template('update_page.html',form=form)

# delete data from the database by id

@application.route("/edit_results/<int:student_id>/delete", methods=['GET'])
def delete_post(student_id):
    if request.method == 'GET':
      student_results = Student.query.get_or_404(student_id)
      db.session.delete(student_results)
      db.session.commit()
    return redirect(url_for('get_results'))

@application.route('/', methods=['GET', 'POST'])
def register():
      # If the User is already logged in, don't allow them to try to register
      if current_user.is_authenticated:
          flash('Already registered!  Redirecting to your User Profile page...')
          return redirect(url_for('user.login'))

      form = RegisterForm()
      if request.method == 'POST' and form.validate_on_submit():
          new_user = Users(form.email.data, form.password.data)
          new_user.authenticated = True
          db.session.add(new_user)
          db.session.commit()
          login_user(new_user)
          flash('Thanks for registering, {}!'.format(new_user.email))
          return redirect(url_for('add_results'))
      return render_template('register.html', form=form)

@application.route('/login', methods=['GET', 'POST'])
def login():
    # If the User is already logged in, don't allow them to try to log in again
    if current_user.is_authenticated:
        flash('Already logged in!  Redirecting to your User Profile page...')
        return redirect(url_for('add_results'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user and user.is_correct_password(form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=form.remember_me.data)
                flash('Thanks for logging in, {}!'.format(current_user.email))
                return redirect(url_for('add_results'))

        flash('ERROR! Incorrect login credentials.')
    return render_template('login.html', form=form)


@application.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('login'))

#
