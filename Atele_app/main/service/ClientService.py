import uuid
import datetime

from Atele_app.main import db
from Atele_app.main.model.Client import Client
from flask import jsonify



def save_new_client(data):
    client = Client.query.filter_by(nom=data['nom']).first()
    if not client:
        new_client = Client(
            #public_id=str(uuid.uuid4()),
            nom=data['nom'],
            prenoms=data['prenoms'],
            date_naissance=data['date_naissance'],
            situation_matrimoniale=data['situation_matrimoniale'],
            entreprise=data['entreprise'],
            longitude=data['longitude'],
            latitude=data['latitude'],
            forme_juridique=data['forme_juridique'],
            adresse=data['adresse'],
            fonction=data['fonction'],
            dom_activite = data['dom_activite'],

            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_client)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def update_client(data):
    client = Client.query.filter_by(id=data['id']).first()
    if not client:
        the_client = Client(
            #public_id=str(uuid.uuid4()),
            nom=data['nom'],
            prenoms=data['prenoms'],
            date_naissance=data['date_naissance'],
            situation_matrimoniale=data['situation_matrimoniale'],
            entreprise=data['entreprise'],
            longitude=data['longitude'],
            latitude=data['latitude'],
            forme_juridique=data['forme_juridique'],
            adresse=data['adresse'],
            fonction=data['fonction'],
            dom_activite = data['dom_activite'],

            registered_on=datetime.datetime.utcnow()
        )
        save_up_changes(the_client)
        response_object = {
            'status': 'success',
            'message': 'Successfully updated.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Client already exists. Please Log in.',
        }
        return response_object, 409


def get_all_client():
    return Client.query.all()


def get_a_client(id):
    return Client.query.filter_by(id=id).first()

def delete_client(id):
    client = Client.query.filter_by(id=id).first()
    print(client)
    db.session.delete(client)
    db.session.commit()
    return jsonify({'result': True})

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def save_up_changes(data):
    db.session.commit()