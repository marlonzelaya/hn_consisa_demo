# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HnUsersInherit(models.Model):
    _inherit = "res.users"

    extension = fields.Char("Extension", help="Forma para comunicarse con el personal en caso de llamada.",
                            tracking=True)