# Copyright (C) 2021-Today - Akretion (<http://www.akretion.com>).
# @author Magno Costa <magno.costa@akretion.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "P7 Stock Valuation Report",
    "version": "16.0.1.0.0",
    "author": "Akretion, Odoo Community Association (OCA)",
    "category": "Reports/QWeb",
    "license": "AGPL-3",
    "depends": [
        "l10n_br_stock_account",
        "report_wkhtmltopdf_param",
    ],
    "website": "https://github.com/OCA/l10n-brazil",
    "development_status": "Beta",
    "maintainers": [
        "mbcosta",
    ],
    "data": [
        # Security
        "security/ir.model.access.csv",
        # Wizard
        "wizards/l10n_br_p7_model_inventory_report_wizard_view.xml",
        # Report
        "report/l10n_br_p7_model_inventory_report.xml",
        "report/l10n_br_p7_model_inventory_report_view.xml",
    ],
    "installable": True,
}
