"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User,Characters,Locations,Favourites
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/people',methods=['GET'])
def handle_peopele():
    peoples=Characters.query.all()
    people_dictoneries=[]
    for people in peoples:
        people_dictoneries.append(people.serialize())
    return jsonify(people_dictoneries),200

@api.route('/people/<id>',methods=['GET'])
def handle_individual_peopele(id):
    all_peoples=Characters.query.get(id)
    return jsonify(all_peoples.serialize()),200

@api.route('/planet',methods=['GET'])
def handle_planet():
    planets=Locations.query.all()
    planets_dictoneries=[]
    for planet in planets:
        planets_dictoneries.append(planet.serialize())
    return jsonify(planets_dictoneries),200

@api.route('/planet/<id>',methods=['GET'])
def handle_individual_planet(id):
    all_planets=Locations.query.get(id)
    return jsonify(all_planets.serialize()),200

@api.route('/users',methods=['GET'])
def handle_user():
    users=User.query.all()
    user_dictoneries=[]
    for user in users:
        user_dictoneries.append(user.serialize())
    return jsonify(user_dictoneries),200

@api.route('/users/favorites',methods=['GET'])
def all_favorites():
    favorites=Favourites.query.all()
    favorite_dictoneries=[]
    for favorite in favorites:
        favorite_dictoneries.append(favorite.serialize())
    return jsonify(favorite_dictoneries),200

@api.route('/favorite/planet/<planet_id>',methods=['POST'])
def favorite_planet(planet_id):
    body=request.json
    single_planet=Favourites(
        user_id=body["user_id"],
        planet_id=planet_id
    )
    db.session.add(single_planet)
    db.session.commit()
    return single_planet.serialize_planet()

@api.route('/favorite/people/<people_id>',methods=['POST'])
def favorite_person(people_id):
    body=request.json
    single_people=Favourites(
        user_id=body["user_id"],
        people_id=people_id
    )
    db.session.add(single_people)
    db.session.commit()
    return single_people.serialize_people()

@api.route('/favorite/planet/<planet_id>',methods=['DELETE'])
def delete_planet(planet_id):
    delete_single_planet=Favourites.query.get(planet_id)
    db.session.delete(delete_single_planet)
    db.session.commit()
    return None

@api.route('/favorite/people/<people_id>',methods=['DELETE'])
def delete_person(people_id):
    delete_single_people=Favourites.query.get(people_id)
    db.session.delete(delete_single_people)
    db.session.commit()
    return None
