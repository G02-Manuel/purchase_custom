from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    seq_company_logo = fields.Binary(string="Logo Segunda Empresa")
    seq_company_address = fields.Text(string="Direccion")