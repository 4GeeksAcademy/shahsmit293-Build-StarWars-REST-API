from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__='characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            'gender':self.gender
            # do not serialize the password, its a security breach
        }

class Locations(db.Model):
    __tablename__='locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(120), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            'gender':self.type
            # do not serialize the password, its a security breach
        }

class Favourites(db.Model):
    __tablename__='favourites'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    def __init__(self,user_id,people_id=None,planet_id=None):
        self.user_id=user_id
        self.people_id=people_id
        self.planet_id=planet_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id":self.people_id,
            "planet_id":self.planet_id
        }
    
    def serialize_planet(self):
        return {
            "id":self.id,
            "user_id": self.user_id,
            "planet_id":self.planet_id
        }
    
    def serialize_people(self):
        return {
            "id":self.id,
            "user_id": self.user_id,
            "planet_id":self.people_id
        }