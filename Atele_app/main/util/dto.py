from flask_restplus import Namespace, fields


class ClientDto:
    api = Namespace('client', description='client related operations')
    client = api.model('client', {
        'nom': fields.String(required=True, description='client nom '),
        'prenoms': fields.String(required=True, description='client prenoms'),
        'date_naissance': fields.String(required=True, description='client date_naissance'),
        'situation_matrimoniale': fields.String(description='client situation_matrimoniale'),
        'entreprise': fields.String(required=True, description='client entreprise'),
        'longitude': fields.String(description='client longitude'),
        'latitude': fields.String(description='client latitude'),
        'forme_juridique': fields.String(required=True, description='client forme_juridique'),
        'adresse': fields.String(required=True, description='client adresse'),
        'fonction': fields.String(required=True, description='client fonction'),
        'dom_activite': fields.String(required=True, description='client dom_activite'),

    })

