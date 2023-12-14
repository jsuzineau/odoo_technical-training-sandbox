from odoo import api,fields, models
from datetime import timedelta

class PropertyOffer(models.Model):
    _name= "estate.property.offer"
    _description = "Property Offer"

    property_id= fields.Many2one("estate.property")
    price      = fields.Float()
    partner_id=fields.Many2one('res.partner', index=True)
    status= fields.Selection(
        string='Property Offer Status',
        selection=[
         ('accepted','Accepted'),
         ('refused' ,'Refused' )
         ])
    def action_Accept(self):
        for record in self:
          record.status= "accepted"
          record.property_id.selling_price= record.price
        return True
    def action_Refuse(self):
        for record in self:
          record.status= "refused"
        return True
    validity= fields.Integer( default=7, string="Validity (days)")

    #date_deadline
    date_deadline= fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline",string="Deadline")
    @api.depends('create_date','validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date+timedelta(days=record.validity)
    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date and record.date_deadline:
                record.validity = record.date_deadline-record.create_date
