from odoo import fields, models

class Property(models.Model):
    _name= "estate.property"
    _description = "Property"

    name              = fields.Char(required=True, string="Title")
    description       = fields.Text()
    postcode          = fields.Char()
    date_availability = fields.Date(string="Available From")
    expected_price    = fields.Float(required=True,string="Expected Price")
    selling_price     = fields.Float(string="Selling Price")
    bedrooms          = fields.Integer()
    living_area       = fields.Integer(string="Living area(sqm)")
    facades           = fields.Integer()
    garage            = fields.Boolean()
    garden            = fields.Boolean()
    garden_area       = fields.Integer(string="Garden area(sqm)")
    garden_orientation= fields.Selection(
        string='Garden Orientation',
        selection=[
         ('north','North'),
         ('south','South'),
         ('east' ,'East' ),
         ('west' ,'West' )
         ],
        help="Type is used to define orientation")
    property_type_id= fields.Many2one("estate.property.type", string="Property type")






