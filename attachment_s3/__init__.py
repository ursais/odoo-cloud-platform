import os
from . import models
from . import controllers

from odoo import api, SUPERUSER_ID


def _auto_create_bucket(cr, registry):
    # create the S3 bucket after module installed
    env = api.Environment(cr, SUPERUSER_ID, {})
    if os.environ.get('AWS_BUCKETNAME', False):
        env["ir.attachment"]._get_s3_bucket()
        env["ir.config_parameter"].create({"key": "ir_attachment.location", "value": "s3"})
        env["ir.attachment"].force_storage()
