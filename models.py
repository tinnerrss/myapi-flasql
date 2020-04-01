from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/myapi_flasql'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    makeups = db.relationship('Makeup', backref='user', lazy=True)

    def __repr__(self):
        return f"💁‍♀️User(id={self.id}, name='{self.name}', email='{self.email}')💁‍♀️"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

makeup_brands = db.Table('makeup_brands',
    db.Column('makeup_id', db.Integer, db.ForeignKey('makeups.id'), primary_key=True),
    db.Column('brand_id', db.Integer, db.ForeignKey('brands.id'), primary_key=True))


class Makeup(db.Model):
    __tablename__ = 'makeups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    kind = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))

    brands = db.relationship('Brand', secondary=makeup_brands, lazy='subquery', backref=db.backref('makeups', lazy=True))

    def __repr__(self):
        return f"💄Makeup(id={self.id}, name='{self.name}', kind='{self.kind}', description='{self.description}', user_id={self.user_id})💄"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'kind': self.kind,
            'description': self.description,
            'brands': [brand.as_dict()[brand] for brand in self.brands]
        }

class Brand(db.Model):
    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"🔖Brand(id={self.id}, name='{self.name})🔖"


