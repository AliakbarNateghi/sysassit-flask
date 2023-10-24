import pandas as pd

from models.models import Component, User, db


def extract_initial_data():
    df = pd.read_excel("./data/GT-22-component.xlsx")

    for index, row in df.iterrows():
        product = Component(
            section=row["Section"],
            sub_section=row["sub-section"],
            level=row["Level"],
            t_code=row["TCode"],
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
