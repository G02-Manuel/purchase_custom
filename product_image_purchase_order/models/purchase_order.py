from odoo import api, fields, models, _


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    image_small = fields.Binary(string="Imagen")

    @api.multi
    @api.onchange('product_id')
    def onchange_purchase_product_image(self):
        for product in self:
            product.image_small = product.product_id.image_small
