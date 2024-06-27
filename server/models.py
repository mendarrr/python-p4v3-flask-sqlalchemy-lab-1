from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Integer, Float, String, MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = db.Column(Integer, primary_key=True)
    magnitude = db.Column(Float)
    location = db.Column(String)
    year = db.Column(Integer)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"

