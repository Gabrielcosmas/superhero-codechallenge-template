from . import db

class Superhero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    power = db.Column(db.String(120), nullable=False)

    def serialize(self):
        return {'id': self.id, 'name': self.name, 'power': self.power}

