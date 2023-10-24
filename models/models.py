from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class componentUser(db.Model):
    __tablename__ = "component_user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=True, unique=True)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
        }


class componentLog(db.Model):
    __tablename__ = "component_log"

    id = db.Column(db.Integer, primary_key=True)
    component_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String, nullable=True)
    user_email = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    old_value = db.Column(db.JSON)  # Initial json of component data
    new_value = db.Column(db.JSON)  # New json of component data

    def serialize(self):
        return {
            "id": self.id,
            "component_id": self.component_id,
            "user_name": self.user_name,
            "user_email": self.user_email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "old_value": self.old_value,
            "new_value": self.new_value,
        }


class State(db.Model):
    __tablename__ = "state"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=True)
    user_email = db.Column(db.String, nullable=False)
    component_id = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    note = db.Column(db.Text, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "component_id": self.component_id,
            "user_name": self.user_name,
            "user_email": self.user_email,
            "owner": self.owner,
            "state": self.state,
            # "created_at": self.created_at,
            "note": self.note,
        }


class Component(db.Model):
    __tablename__ = "component"

    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(50), nullable=False)
    sub_section = db.Column(db.String(50), nullable=True)
    level = db.Column(db.Integer, nullable=False)
    TCode = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    Parent = db.Column(db.String(50), nullable=True)
    module = db.Column(db.Boolean, nullable=False)
    repeated = db.Column(db.Boolean, nullable=False)
    condition = db.Column(db.String(50), nullable=True)
    fig = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(5), nullable=True)
    part = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    standard = db.Column(db.String(50), nullable=True)
    national_stock_number = db.Column(db.String(100), nullable=True)
    part_number = db.Column(db.String(100), nullable=False)
    ATA_number = db.Column(db.String(100), nullable=True)
    weight_on_pcs = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    version = db.Column(db.String(100), nullable=True)
    sap_code = db.Column(db.String(100), nullable=True)
    head_of_CVE = db.Column(db.String(100), nullable=True)
    CP = db.Column(db.Boolean, nullable=False)
    CCL = db.Column(db.Boolean, nullable=False)
    drawing_lvl_2 = db.Column(db.Boolean, nullable=False)
    ITP_and_SPc_of_material = db.Column(db.Boolean, nullable=False)
    ITP_and_SPC_of_production_technology = db.Column(db.Boolean, nullable=False)
    type_of_analysis = db.Column(db.Boolean, nullable=False)
    prototype_part = db.Column(db.Boolean, nullable=False)
    test = db.Column(db.Boolean, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "section": self.section,
            "sub_section": self.sub_section,
            "level": self.level,
            "TCode": self.TCode,
            "code": self.code,
            "Parent": self.Parent,
            "module": self.module,
            "Repeated": self.repeated,
            "condition": self.condition,
            "fig": self.fig,
            "position": self.position,
            "part": self.part,
            "quantity": self.quantity,
            "standard": self.standard,
            "national_stock_number": self.national_stock_number,
            "part_number": self.part_number,
            "ATA_number": self.ATA_number,
            "weight_on_pcs": self.weight_on_pcs,
            "weight": self.weight,
            "version": self.version,
            "sap_code": self.sap_code,
            "head_of_CVE": self.head_of_CVE,
            "CP": self.CP,
            "CCL": self.CCL,
            "drawing_lvl_2": self.drawing_lvl_2,
            "ITP_and_SPc_of_material": self.ITP_and_SPc_of_material,
            "ITP_and_SPC_of_production_technology": self.ITP_and_SPC_of_production_technology,
            "type_of_analysis": self.type_of_analysis,
            "prototype_part": self.prototype_part,
            "test": self.test,
        }
