from odoo import fields, models

class PropertyOffer(models.Model):
    _name= "estate.property.offer"
    _description = "Property Offer"

    property_id= fields.Many2one("estate.property")
    price      = fields.Float()
    partner_id=fields.Many2one('res.partner', index=True, tracking=True)
    status= fields.Selection( nocopy= True,
        string='Property Offer Status',
        selection=[
         ('accepted','Accepted'),
         ('refused' ,'Refused' )
         ])
