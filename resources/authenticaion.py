from flask import (
    Blueprint,
    Flask,
    json,
    jsonify,
    make_response,
    redirect,
    render_template,
    request,
    session,
)
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from flask_restful import Api, Resource
from werkzeug.security import check_password_hash, generate_password_hash

from ..models.models import componentUser

authentication_bp = Blueprint("authentication_api", __name__)
authentication_api = Api(authentication_bp)


class Login(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        user = componentUser.query.filter_by(username=username).first()
        if user and check_password_hash(
            user.password, password
        ):  # password == user.password:
            access_token = create_access_token(identity=username)
            session["username"] = username
            return {
                "access": access_token,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            }, 200

        return {"message": "Invalid username or password"}, 401


authentication_api.add_resource(Login, "/api/login")
