import logging

from odoo.addons.web.controllers.main import Database
from odoo import http
from odoo import exceptions
from odoo.http import request

_logger = logging.getLogger(__name__)


class Database(Database):
    @http.route()
    def drop(self, master_pwd, name):
        response = super(Database, self).drop(master_pwd, name)
        try:
            bucket = request.env["ir.attachment"]._get_s3_bucket()
            bucket.objects.all().delete()
            return response
        except exceptions.UserError:
            _logger.exception(
                "error reading attachment '%s' from object storage", fname
            )
            return response
