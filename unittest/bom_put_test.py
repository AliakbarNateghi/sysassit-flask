import os
import sys
import unittest
from unittest.mock import patch

from models.models import Component


class Testcomponent(unittest.TestCase):
    @patch("app.Component.query")
    @patch("app.request")
    @patch("openpyxl.load_workbook")
    @patch("openpyxl.Workbook")
    def test_put(self, mock_workbook, mock_load_workbook, mock_request, mock_query):
        mock_query.get.return_value = None
        mock_request.json = {
            "section": "test_section",
            "sub-section": "test_sub_section",
            "level": "test_level",
            "TCode": "test_TCode",
            "code": "test_code",
            "Parent": "test_Parent",
            "module": True,
            "repeated": False,
            "condition": "test_condition",
            "fig": "test_fig",
            "position": "test_position",
            "part": "test_part",
            "quantity": "test_quantity",
            "standard": "test_standard",
            "national_stock_number": "test_national_stock_number",
            "part_number": "test_part_number",
            "ATA_number": "test_ATA_number",
            "weight_on_pcs": "test_weight_on_pcs",
            "weight": "test_weight",
            "version": "test_version",
            "sap_code": "test_sap_code",
            "head_of_CVE": "test_head_of_CVE",
            "CP": True,
            "CCL": False,
            "drawing_lvl_2": True,
            "ITP_and_SPc_of_material": False,
            "ITP_and_SPC_of_production_technology": True,
            "type_of_analysis": False,
            "prototype_part": True,
            "test": False,
        }

        component = Component()
        component.put(component_id=1)

        mock_query.get.assert_called_once_with(1)
        mock_query.get.return_value = Component(id=1)
        component.put(component_id=1)

        self.assertEqual(mock_query.get.call_count, 2)
        self.assertEqual(mock_workbook.call_count, 1)
        self.assertEqual(mock_load_workbook.call_count, 1)
