# Copyright 2019 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import json

from lxml import etree

from odoo import _, api, models
from odoo.exceptions import UserError


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet.sheet"

    @api.model
    def get_view(self, view_id=None, view_type="form", **options):
        res = super().get_view(view_id, view_type, **options)
        review_policy = self.env.user.company_id.timesheet_sheet_review_policy
        if review_policy == "department_manager" and view_type == "tree":
            view = etree.XML(res["arch"])
            field = view.find(".//field[@name='department_id']")
            if field is not None:
                field.set("invisible", "0")
                modifiers = json.loads(field.get("modifiers"))
                modifiers.update(
                    {
                        "column_invisible": False,
                    }
                )
                field.set("modifiers", json.dumps(modifiers))
            res["arch"] = etree.tostring(
                view,
                encoding="unicode",
            ).replace("\t", "")
        return res

    @api.depends("department_id.manager_id.user_id")
    def _compute_department_manager_as_reviewer(self):
        self._compute_possible_reviewer_ids()

    def _get_complete_name_components(self):
        self.ensure_one()
        result = super()._get_complete_name_components()
        if self.review_policy == "department_manager":
            result += [self.department_id.name_get()[0][1]]
        return result

    def _get_possible_reviewers(self):
        self.ensure_one()
        res = super()._get_possible_reviewers()
        if self.review_policy == "department_manager":
            res |= self.department_id.manager_id.user_id
        return res

    def _check_can_review(self):
        res = super()._check_can_review()
        if self.filtered(
            lambda sheet: not sheet.can_review
            and sheet.review_policy == "department_manager"
        ):
            raise UserError(_("Only a Department's Manager can review the sheet."))
        return res
