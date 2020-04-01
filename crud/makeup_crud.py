from flask import jsonify, redirect
from models import db, Makeup


def get_all_makeups():
    try:
        all_makeups = Makeup.query.all()
        result = [makeup.as_dict() for makeup in all_makeups]
        return jsonify(result)
    except Exception as error:
        return error('getting all makeups', error)


def create_makeup(name, kind, description):
    try:
        new_makeup = Makeup(name=name, kind=kind, description=description or None)
        db.session.add(new_makeup)
        db.session.commit()
        return jsonify(new_makeup.as_dict())
    except Exception as error:
        return error('creating new makeup', error)

def get_makeup(id):
    try:
        makeup = Makeup.query.get(id)
        if makeup:
            return jsonify(makeup.as_dict())
        else:
            raise Exception('Error getting makeup at id {}'.format(id))
    except Exception as error:
        print(f'Error in getting one makeup\n{error}')
        return jsonfiy(error='Server Error')


def update_makeup(id, name, kind, description):
    try:
        makeup = Makeup.query.get(id)
        makeup.kind = kind or makeup.kind
        makeup.name = name or makeup.name
        makeup.description = description or makeup.description
        db.session.commit()
        return jsonify(makeup.as_dict())
    except Exception as error:
        return error('updating one makeup', error)

def destroy_makeup(id):
    try:
        makeup = Makeup.query.get(id)
        db.session.delete(makeup)
        db.session.commit()
        return redirect('/makeups')
    except Exception as error:
        return error('deleting a makeup', error)