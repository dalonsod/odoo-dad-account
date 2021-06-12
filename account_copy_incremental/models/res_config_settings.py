# Copyright (C) 2021 David Alonso Domínguez
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    account_copy_increment = fields.Integer(
        related="company_id.account_copy_increment", required=True, readonly=False
    )

    @api.constrains("account_copy_increment")
    def _check_account_copy_increment(self):
        if self.account_copy_increment <= 0:
            raise ValidationError(
                _(
                    "Account Copy Increment value not valid (%s). It shoud be greater than zero!"
                )
                % self.account_copy_increment
            )
