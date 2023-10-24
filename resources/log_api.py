import json

from flask import Blueprint, jsonify, redirect, request, session, url_for
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, Resource

from ..models.models import componentLog, componentUser, db

log_bp = Blueprint("log_api", __name__)
log_api = Api(log_bp)


class logs_api(Resource):
    @jwt_required()
    def get(self, component_id=None):
        if component_id:
            logs = componentLog.query.filter_by(component_id=component_id)
        else:
            logs = componentLog.query.all()
        result = []
        for log in logs:
            log_dict = {}
            log_dict["user_name"] = log.user_name
            log_dict["user_email"] = log.user_email
            log_dict["created_at"] = log.created_at
            log_dict["updated_at"] = log.updated_at
            log_dict["updated_fields"] = log.updated_fields
            log_dict["old_value"] = log.old_value
            log_dict["new_value"] = log.new_value
            result.append(log_dict)
        return jsonify(result)


log_api.add_resource(logs_api, "/api/logs", "/api/logs/<int:component_id>")
