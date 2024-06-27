# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Update to use Session.get() instead of Query.get()
@app.route('/earthquakes/<int:id>')
def get_earthquake_id(id):
    earthquake = db.session.get(Earthquake, id)
    if earthquake is None:
        return jsonify({"message": f"Earthquake {id} not found."}), 404
    else:
        return jsonify({
            "id": earthquake.id,
            "location": earthquake.location,
            "magnitude": earthquake.magnitude,
            "year": earthquake.year
        }), 200

@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    response = {
        "count": len(earthquakes),
        "quakes": [{"id": eq.id, "location": eq.location, "magnitude": eq.magnitude, "year": eq.year} for eq in earthquakes]
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
