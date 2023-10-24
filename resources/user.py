from http.client import BAD_REQUEST
import json
from flask import Blueprint, abort, jsonify, redirect, request, session, url_for
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, Resource

from ..models.models import componentUser

user_bp = Blueprint("user_api", __name__)
user_api = Api(user_bp)

from flask import Flask, request, jsonify
import jwt


class User(Resource):
    @jwt_required()
    def get(self):
        user = get_jwt_identity()
        try: 
            if "username" in session and session["username"] == user:
                user = componentUser.query.filter_by(username=user).first()
                user = user.serialize()
                json_data = json.dumps(user)
                return jsonify(json_data)
        except jwt.ExpiredSignatureError:
            return {'error': 'Token has expired'}, 401
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}, 401
        

user_api.add_resource(User, "/api/user", "/api/user/")

