from odoo import fields, models


class IRAttachmentPayrollCustom(models.Model):
    _name = "ir.attachment.payroll.custom"
    _description = "Payroll attachment"

    attachment_id = fields.Many2one(
        comodel_name="ir.attachment",
        string="Attachment File",
        prefetch=False,
        invisible=True,
        ondelete="cascade",
    )
    employee = fields.Char()
    identification_id = fields.Char("Identification ID")
    create_date = fields.Date(default=fields.Date.context_today)
    subject = fields.Char()
