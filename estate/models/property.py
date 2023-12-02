from odoo import api,fields, models

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
    salesman_id = fields.Many2one('res.users', index=True, tracking=True, default=lambda self: self.env.user)
    buyer_id=fields.Many2one('res.partner', index=True, tracking=True)
    tag_ids=fields.Many2many("estate.property.tag", string="Tags")
    offer_ids=fields.One2many("estate.property.offer", "property_id", string="Offers")

    #total_area
    @api.depends("living_area")
    @api.depends("garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area+record.garden_area
    total_area = fields.Float(compute="_compute_total_area", string="Total Area(sqm)")

    #best_price
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = min(record.offer_ids.mapped('price'))
            else:
                record.best_price = ""

    best_price = fields.Float(compute="_compute_best_price", string="Best Offer")


