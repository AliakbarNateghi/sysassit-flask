from marshmallow import Schema, fields


class CreateComponentSchema(Schema):
    section = fields.Str(required=True)
    sub_section = fields.Str(required=False)
    level = fields.Int(required=True)
    TCode = fields.Str(required=True)
    code = fields.Str(required=True)
    Parent = fields.Str(required=False)
    module = fields.Bool(required=True)
    repeated = fields.Bool(required=True)
    condition = fields.Str(required=False)
    fig = fields.Int(required=False)
    position = fields.Str(required=False)
    part = fields.Str(required=True)
    quantity = fields.Int(required=False)
    standard = fields.Str(required=False)
    national_stock_number = fields.Str(required=False)
    part_number = fields.Str(required=True)
    ATA_number = fields.Str(required=False)
    weight_on_pcs = fields.Float(required=False)
    weight = fields.Float(required=False)
    version = fields.Str(required=False)
    sap_code = fields.Str(required=False)
    head_of_CVE = fields.Str(required=False)
    CP = fields.Bool(required=True)
    CCL = fields.Bool(required=True)
    drawing_lvl_2 = fields.Bool(required=True)
    ITP_and_SPc_of_material = fields.Bool(required=True)
    ITP_and_SPC_of_production_technology = fields.Bool(required=True)
    type_of_analysis = fields.Bool(required=True)
    prototype_part = fields.Bool(required=True)
    test = fields.Bool(required=True)


class CreateStateSchema(Schema):
    component_id = fields.Int(required=True)
    owner = fields.Str(required=False)
    note = fields.Str(required=False)
    state = fields.Str(required=True)
