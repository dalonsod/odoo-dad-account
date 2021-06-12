# Copyright (C) 2021 David Alonso Domínguez
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    account_copy_increment = fields.Integer(required=True, default=10)
