import os
import socket

import pandas as pd
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.security import generate_password_hash

from .models.models import Component, db, componentUser
from .resources.authenticaion import authentication_bp
from .resources.component_api import component_bp
from .resources.excels import excel_bp
from .resources.log_api import log_bp
from .resources.state_api import state_bp
from .resources.user import user_bp

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "database.db"
database_uri = "sqlite:///{}".format(os.path.join(project_dir, database_file))


app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config["SECRET_KEY"] = "your-secret-key"
app.config["JWT_SECRET_KEY"] = "jwt-secret-key"

jwt = JWTManager(app)

SWAGGER_URL = "/api/docs"  # URL for exposing Swagger UI (without trailing '/')
API_URL = (
    "/static/swagger/swagger.json"  # Our API url (can of course be a local resource)
)

db.init_app(app)
migrate = Migrate(app, db)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={"app_name": "Test application"},  # Swagger UI config overrides
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(log_bp)
app.register_blueprint(component_bp)
app.register_blueprint(excel_bp)
app.register_blueprint(state_bp)
app.register_blueprint(authentication_bp)
app.register_blueprint(user_bp)

api = Api(app)

# This line fixes the neccessary headers that needed !!!
CORS(app, resources={r"/*": {"origins": "*"}})
app.config["CORS_HEADERS"] = "Content-Type"


script_dir = os.path.dirname(os.path.abspath(__file__))
"""
    A function for extracting initia data of exel 
    and put the data in the database
"""


def extract_initial_data():
    USERdf = pd.read_excel(os.path.join(script_dir, ".", "data", "users.xlsx"))
    for index, row in USERdf.iterrows():
        user = componentUser(
            username = row["username"],
            password = generate_password_hash(row["password"]),
            email = row["email"],
        )

        db.session.add(user)

    BOMdf = pd.read_excel(os.path.join(script_dir, ".", "data", "GT-22-BOM.xlsx"))
    for index, row in BOMdf.iterrows():
        product = Component(
            section=row["Section"],
            sub_section=row["sub-section"],
            level=row["Level"],
            TCode=row["TCode"],
            code=row["Code"],
            Parent=row["Parent"],
            module=True if row["module"] == "yes" else False,
            repeated=True if row["Repeated"] == "yes" else False,
            condition=row["condition"],
            fig=row["Fig"],
            position=row["Position"],
            part=row["part"],
            quantity=row["Quantity"],
            standard=row["Standard"],
            national_stock_number=row["National Stock Number"],
            part_number=row["Part Number"],
            ATA_number=row["ATA number"],
            weight_on_pcs=row["weight/pcs"],
            weight=row["weight"],
            version=row["Version"],
            sap_code=row["Sap code"],
            head_of_CVE=row["head of CVE"],
            CP=True if row["CP"] == "yes" else False,
            CCL=True if row["CCL"] == "yes" else False,
            drawing_lvl_2=True if row["drawing  level 2"] == "yes" else False,
            ITP_and_SPc_of_material=True
            if row["ITP & Spc of material "] == "yes"
            else False,
            ITP_and_SPC_of_production_technology=True
            if row["ITP & Spc of Production Technology"] == "yes"
            else False,
            type_of_analysis=True if row["Type of  analysis"] == "yes" else False,
            prototype_part=True if row["prototype part"] == "yes" else False,
            test=True if row["Test"] == "yes" else False,
        )

        db.session.add(product)

    db.session.commit()


if __name__ == "__main__":
    # Find the local IP addr
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Running on: http://{local_ip}:5000")

    # Run the flask app
    app.run(debug=True, host=local_ip, port=5000)
