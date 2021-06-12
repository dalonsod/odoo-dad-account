# Copyright (C) 2021 David Alonso Domínguez
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
from odoo import _, api, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    @api.returns("self", lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        if not default.get("code", False):
            AccountObj = self.env["account.account"]
            company = self.env["res.company"].browse(
                default.get("company_id", False) or self.company_id.id
            )
            company_domain = ("company_id", "=", company.id)
            default["code"] = self.code
            default.setdefault("name", _("%s (copy)") % (self.name or ""))
            while True:
                default["code"] = (
                    str(int(default["code"]) + company.account_copy_increment) or ""
                ).zfill(len(default["code"]))
                if not AccountObj.search(
                    [("code", "=", default["code"]), company_domain], limit=1
                ):
                    break
        return super().copy(default=default)
