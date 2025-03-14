# Copyright (C) 2009  Renato Lima - Akretion, Gabriel C. Stabel
# Copyright (C) 2012  Raphaël Valyi - Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = [_name, "l10n_br_fiscal.document.mixin"]

    @api.model
    def _default_fiscal_operation(self):
        return self.env.company.purchase_fiscal_operation_id

    @api.model
    def _fiscal_operation_domain(self):
        domain = [
            ("state", "=", "approved"),
            ("fiscal_type", "in", ("purchase", "other", "purchase_refund")),
        ]
        return domain

    active_company_country_id = fields.Many2one(
        comodel_name="res.country",
        string="Active Company Country",
        default=lambda self: self.env.company.country_id,
    )

    fiscal_operation_id = fields.Many2one(
        comodel_name="l10n_br_fiscal.operation",
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=_default_fiscal_operation,
        domain=lambda self: self._fiscal_operation_domain(),
    )

    cnpj_cpf = fields.Char(
        string="CNPJ/CPF",
        related="partner_id.cnpj_cpf",
    )

    legal_name = fields.Char(
        string="Legal Name",
        related="partner_id.legal_name",
    )

    ie = fields.Char(
        string="State Tax Number/RG",
        related="partner_id.inscr_est",
    )

    comment_ids = fields.Many2many(
        comodel_name="l10n_br_fiscal.comment",
        relation="purchase_order_comment_rel",
        column1="purchase_id",
        column2="comment_id",
        string="Comments",
    )

    operation_name = fields.Char(
        copy=False,
    )

    @api.model
    def _get_view(self, view_id=None, view_type="form", **options):
        arch, view = super()._get_view(view_id, view_type, **options)
        arch = self.env["purchase.order.line"].inject_fiscal_fields(arch)
        return arch, view

    @api.onchange("fiscal_operation_id")
    def _onchange_fiscal_operation_id(self):
        result = super()._onchange_fiscal_operation_id()
        self.fiscal_position_id = self.fiscal_operation_id.fiscal_position_id
        return result

    def _get_amount_lines(self):
        """Get object lines instaces used to compute fields"""
        return self.mapped("order_line")

    @api.depends("order_line")
    def _compute_fiscal_amount(self):
        return super()._compute_fiscal_amount()

    @api.depends("order_line.price_total")
    def _amount_all(self):
        self._compute_fiscal_amount()

    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super()._prepare_invoice()
        if self.fiscal_operation_id:
            # O caso Brasil se caracteriza por ter a Operação Fiscal
            document_type_id = (
                self.order_line[0].fiscal_operation_line_id.document_type_id.id
                if self.order_line
                and self.order_line[0].fiscal_operation_line_id.document_type_id
                else (
                    self.fiscal_operation_id.document_type_ids[0].document_type_id.id
                    if self.fiscal_operation_id
                    and self.fiscal_operation_id.document_type_ids
                    else self.company_id.document_type_id.id
                )
            )
            invoice_vals.update(
                {
                    "ind_final": self.ind_final,
                    "fiscal_operation_id": self.fiscal_operation_id.id,
                    "document_type_id": document_type_id,
                }
            )
        return invoice_vals

    def _get_fiscal_partner(self):
        self.ensure_one()
        partner = super()._get_fiscal_partner()
        if partner.id != partner.address_get(["invoice"]).get("invoice"):
            partner = self.env["res.partner"].browse(
                partner.address_get(["invoice"]).get("invoice")
            )
        return partner
