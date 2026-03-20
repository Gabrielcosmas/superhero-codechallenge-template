from flask import jsonify, request
from . import app, db
from .models import Superhero

@app.route('/')
def home():
    return 'Hello, Superhero!'

@app.route('/superheroes', methods=['GET'])
def get_superheroes():
    heroes = Superhero.query.all()
    return jsonify([h.serialize() for h in heroes])

@app.route('/superheroes', methods=['POST'])
def add_superhero():
    data = request.get_json()
    hero = Superhero(name=data['name'], power=data['power'])
    db.session.add(hero)
    db.session.commit()
    return jsonify(hero.serialize()), 201

@app.route('/superheroes/<int:id>', methods=['PUT'])
def update_superhero(id):
    hero = Superhero.query.get_or_404(id)
    data = request.get_json()
    hero.name = data.get('name', hero.name)
    hero.power = data.get('power', hero.power)
    db.session.commit()
    return jsonify(hero.serialize())

@app.route('/superheroes/<int:id>', methods=['DELETE'])
def delete_superhero(id):
    hero = Superhero.query.get_or_404(id)
    db.session.delete(hero)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'})

