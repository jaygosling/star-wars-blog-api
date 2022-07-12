"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Vehicles, Planets, Fav_characters, Fav_planets, Fav_vehicles
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/favorite/characters', methods=['GET'])
def get_all_favorite_char():
    fav_chars = Fav_characters.query.filter_by(user_id=1)
    fav_chars = list(map(lambda elemento: elemento.serialize(), fav_chars))
    return jsonify({"mensaje":fav_chars})

@app.route('/favorite/planets', methods=['GET'])
def get_all_favorite_planets():
    fav_plan = Fav_planets.query.filter_by(user_id=1)
    fav_plan = list(map(lambda elemento: elemento.serialize(), fav_plan))
    return jsonify({"mensaje":fav_plan})    

@app.route('/favorite/vehicles', methods=['GET'])
def get_all_favorite_vehicles():
    fav_veh = Fav_vehicles.query.filter_by(user_id=1)
    fav_veh = list(map(lambda elemento: elemento.serialize(), fav_veh))
    return jsonify({"mensaje":fav_veh})

@app.route('/users', methods=['GET'])
def get_all_users():
    allUsers = User.query.all()
    allUsers = list(map(lambda elemento: elemento.serialize(), allUsers))
    return jsonify({"mensaje":allUsers})

@app.route('/characters', methods=['GET'])
def get_characters():
    allcharacters = Characters.query.all()
    allcharacters = list(map(lambda elemento: elemento.serialize(), allcharacters))
    return jsonify({"mensaje":allcharacters})

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    allvehicles = Vehicles.query.all()
    allvehicles = list(map(lambda elemento: elemento.serialize(), allvehicles))
    return jsonify({"mensaje": allvehicles})

@app.route('/planets', methods=['GET'])
def get_planets():
    allplanets = Planets.query.all()
    allplanets = list(map(lambda elemento: elemento.serialize(), allplanets))
    return jsonify({"mensaje": allplanets})

@app.route('/characters/<int:id>', methods=['GET'])
def get_onecharacter(id):
    onecharacter = Characters.query.get(id)
    if onecharacter:
        onecharacter = onecharacter.serialize()
        return jsonify({"resultado":onecharacter})
    else:
        return jsonify({"resultado":"El personaje no existe"})

@app.route('/vehicles/<int:id>', methods=['GET'])
def get_onevehicle(id):
    onevehicle = Vehicles.query.get(id)
    if onevehicle:
        onevehicle = onevehicle.serialize()
        return jsonify({"resultado":onevehicle})
    else:
        return jsonify({"resultado":"El vehículo no existe"})

@app.route('/planets/<int:id>', methods=['GET'])
def get_oneplanet(id):
    oneplanet = Planets.query.get(id)
    if oneplanet:
        oneplanet = oneplanet.serialize()
        return jsonify({"resultado":oneplanet})
    else:
        return jsonify({"resultado":"El personaje no existe"})

    print(oneplanet)

#Los POSTS ---->

@app.route('/favorite/characters/<int:character_id>', methods=['POST'])
def add_character_fav(character_id):
    one_character = Characters.query.get(character_id)
    if one_character:
        new = Fav_characters()
        new.user_id = 1
        new.character_id = character_id
        db.session.add(new)
        db.session.commit()
        return jsonify({"mensaje":"Todo salio bien"})
    else:
        return jsonify({"mensaje": "Personaje no existe"})

@app.route('/favorite/planets/<int:planet_id>', methods=['POST'])
def add_planet_fav(planet_id):
    one_planet = Planets.query.get(planet_id)
    if one_planet:
        new = Fav_planets()
        new.user_id = 1
        new.planet_id = planet_id
        db.session.add(new)
        db.session.commit()
        return jsonify({"mensaje":"Todo salio bien"})
    else:
        return jsonify({"mensaje": "Personaje no existe"})

@app.route('/favorite/vehicles/<int:vehicle_id>', methods=['POST'])
def add_vehicle_fav(vehicle_id):
    one_vehicle = Planets.query.get(vehicle_id)
    if one_vehicle:
        new = Fav_vehicles()
        new.user_id = 1
        new.vehicle_id = vehicle_id
        db.session.add(new)
        db.session.commit()
        return jsonify({"mensaje":"Todo salio bien"})
    else:
        return jsonify({"mensaje": "Personaje no existe"})

#Los deletes -->
@app.route('/favorite/characters/<int:char_id>', methods=['DELETE'])
def del_character_fav(char_id):
    char_fav = Fav_characters.query.filter_by(character_id=char_id, user_id=1).first()
    if char_fav:
        db.session.delete(char_fav)
        db.session.commit()
        return jsonify({"mensaje":"Personaje favorito eliminado"})
    else:
        return jsonify({"mensaje": "Favorito no encontrado"})

@app.route('/favorite/planets/<int:planet>', methods=['DELETE'])
def del_planet_fav(planet):
    planet_fav = Fav_planets.query.filter_by(planet_id=planet, user_id=1).first()
    if planet_fav:
        db.session.delete(planet_fav)
        db.session.commit()
        return jsonify({"mensaje":"Planeta favorito eliminado"})
    else:
        return jsonify({"mensaje": "Favorito no encontrado"})

@app.route('/favorite/vehicles/<int:vehicle>', methods=['DELETE'])
def del_vehicle_fav(vehicle):
    vehicle_fav = Fav_vehicles.query.filter_by(vehicle_id=vehicle, user_id=1).first()
    if vehicle_fav:
        db.session.delete(vehicle_fav)
        db.session.commit()
        return jsonify({"mensaje":"Vehículo favorito eliminado"})
    else:
        return jsonify({"mensaje": "Favorito no encontrado"})



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
