from flask import Response

from models.user_model import *


def populate_db():
    db.drop_all()
    db.create_all()
    User.init_db_users()
    response_text = '{ "message": "Database populated." }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


def basic():
    response_text = '{ "message": "Vulnerable REST API with OWASP top 10 vulnerabilities for APIs.!", "Help": "R3connaissance is K3y to $ucc3$$." } '
    response = Response(response_text, 200, mimetype='application/json')
    return response
