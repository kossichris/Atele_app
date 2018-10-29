from .. import db, flask_bcrypt

class Client(db.Model):
    """ Client Model for storing user related details """
    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(255), unique=False, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    prenoms = db.Column(db.String(50), unique=False)
    date_naissance = db.Column(db.String(50), unique=False)
    situation_matrimoniale = db.Column(db.String(50))
    entreprise = db.Column(db.String(50), unique=False)
    longitude =db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))
    latitude = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))
    forme_juridique = db.Column(db.String(50), unique=False)
    adresse = db.Column(db.String(50), unique=False)
    fonction = db.Column(db.String(50), unique=False)
    dom_activite = db.Column(db.String(50), unique=False)

    # admin = db.Column(db.Boolean, nullable=False, default=False)
    # public_id = db.Column(db.String(100), unique=True)
    #password_hash = db.Column(db.String(100))