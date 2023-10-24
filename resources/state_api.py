from http.client import BAD_REQUEST

from flask import Blueprint, abort, jsonify, redirect, request, session, url_for
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, Resource

from ..models.models import State, componentUser, db
from ..schemas.schemas import CreateStateSchema

state_bp = Blueprint("state_api", __name__)
state_api = Api(state_bp)


class state(Resource):
    @jwt_required()
    def post(self):
        user = get_jwt_identity()
        if "username" in session and session["username"] == user:
            user = componentUser.query.filter_by(username=user).first()

        errors = CreateStateSchema().validate(request.json)

        if errors:
            abort(BAD_REQUEST, str(errors))

        state = State(
            component_id=request.json.get("component_id"),
            user_name=user.username,
            user_email=user.email,
            owner=request.json.get("owner"),
            note=request.json.get("note"),
            state=request.json.get("state"),
        )

        # old_state_data = state.serialize()

        db.session.add(state)
        db.session.commit()

        return state.serialize(), 200

    @jwt_required()
    def get(self, component_id=None):
        
        if component_id:
            states = State.query.filter_by(component_id=component_id)
        else:
            states = State.query.all()
        result = []
        for state in states:
            state_dict = {}
            state_dict["user_name"] = state.user_name
            state_dict["user_email"] = state.user_email
            state_dict["created_at"] = state.created_at
            state_dict["state"] = state.state
            state_dict["owner"] = state.owner
            state_dict["note"] = state.note
            state_dict["component_id"] = state.component_id
            result.append(state_dict)
        return jsonify(result)


state_api.add_resource(state, "/api/state", "/api/state/", "/api/state/<int:component_id>")
