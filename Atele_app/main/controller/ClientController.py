
from flask import request
from flask_restplus import Resource

from ..util.dto import ClientDto
from ..service.ClientService import save_new_client, get_all_client, get_a_client, delete_client

api = ClientDto.api
_client = ClientDto.client


@api.route('/')
class ClientList(Resource):
    @api.doc('list_of_registered_clients')
    @api.marshal_list_with(_client, envelope='data')
    def get(self):
        """List all registered clients"""
        return get_all_client()

    @api.response(201, 'Client successfully created.')
    @api.doc('create a new client')
    @api.expect(_client, validate=True)
    def post(self):
        """Creates a new Client """
        data = request.json
        return save_new_client(data=data)


@api.route('/<id>')
@api.param('id', 'The client identifier')
@api.response(404, 'Client not found.')
class Client(Resource):
    @api.doc('get a client')
    @api.marshal_with(_client)
    def get(self, id):
        """get a client given its identifier"""
        client = get_a_client(id)
        if not client:
            api.abort(404)
        else:
            return client

    def delete(self, id):
        """delete a given client by its identifier"""
        client = delete_client(id)
        if not client:
            api.abort(404)
        else:
            return {'message ': 'successfully deleted'}



