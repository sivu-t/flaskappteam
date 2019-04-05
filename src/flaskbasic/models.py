# Referencing the modules
from src.flaskbasic import db, application,  bcrypt
from datetime import datetime

# how the data is structured in the database
class Student(db.Model):

    __tablename__ = 'Student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable= False)
    physics = db.Column(db.Integer)
    maths = db.Column(db.Integer)
    chemistry = db.Column(db.Integer)

    def __init__(self,name,physics,maths,chemistry):
        self.name = name
        self.physics = physics
        self.maths = maths
        self.chemistry = chemistry

    def get_id(self):
        return str(self.id)

    def get_name(self):
        return str(self.name)

    def get_physics(self):
       return int(self.physics)

    def get_maths(self):
        return int(self.maths)

    def get_chemistry(self):
        return int(self.chemistry)

    def __repr__(self):
        return "Student('{self.id}', '{self.name}',{self.physics}',{self.maths}',{self.chemistry}')"



class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.Binary(60), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column(db.DateTime, nullable=True)
    role = db.Column(db.String, default='user')

    def __init__(self, email, plaintext_password, role='user'):
        self.email = email
        self.hashed_password = bcrypt.generate_password_hash(plaintext_password)
        self.authenticated = False
        self.registered_on = datetime.now()
        self.role = role

    def set_password(self, plaintext_password):
        self.hashed_password = bcrypt.generate_password_hash(plaintext_password)

    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.hashed_password, plaintext_password)

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the id of a user to satisfy Flask-Login's requirements."""
        return str(self.id)

    def __repr__(self):
        return '<Users {}>'.format(self.email)
