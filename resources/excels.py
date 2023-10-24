import json

from flask import Blueprint, redirect, send_file, session, url_for
from flask_jwt_extended import jwt_required
from flask_restful import Api, Resource

excel_bp = Blueprint("excel_api", __name__)
excel_api = Api(excel_bp)


class download_components_excel(Resource):
    @jwt_required()
    def get(self):
        component_excel = "data/GT-22-BOM.xlsx"
        return send_file(component_excel, as_attachment=True)


class download_logs_excel(Resource):
    @jwt_required()
    def get(self):
        logs_excel = "data/logs.xlsx"
        return send_file(logs_excel, as_attachment=True)


excel_api.add_resource(download_components_excel, "/excel/components")
excel_api.add_resource(download_logs_excel, "/excel/logs")
