from models import app, User, Makeup, Brand
from flask import jsonify, request
from crud.makeup_crud import get_all_makeups, create_makeup, get_makeup, update_makeup

@app.route('/makeups', methods=['GET', 'POST'])
def makeup_index_create():
    if request.method == 'GET':
        try:
            return get_all_makeups()
        except Exception as error:
            return error('GET /makeups route', error)
    if request.method == 'POST':
        try:
            return create_makeup(name=request.form['name'], kind=request.form['kind'], description=request.form['description'])
        except Exception as error:
            return error('POST /makeup route', error)  

@app.route('/makeups/<int:id>', methods=['GET', 'PUT', 'DELETE']) 
def makeup_show_update_delete(id):
    if request.method == 'GET':
        try:
            return get_makeup(id)
        except Exception as error:
            return error('GET /makeups/:id route', error)
    if request.method == 'PUT':
        try:
            return update_makeup(
                id=id,
                name=request.form['name'],
                kind=request.form['kind'],
                description=request.form['description']
            )
        except Exception as error:
            return error('PUT /makeups/:id route', error)
    if request.method == 'DELETE':
        try:
            return destroy_makeup(id)
        except Exception as error:
            return error('DELETE /makeups/:id route', error)