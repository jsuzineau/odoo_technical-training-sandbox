{
'name':"estate",
'license':"LGPL-3",
'version': '1.0',
'description':"Real estate",
'depends':['base'],
'application':True,
'data':[
       'security/ir.model.access.csv',
       'views/property_type.xml',
       'views/property_tag.xml',
       'views/property_offer.xml',
       'views/property.xml',
       'views/menu.xml',
       'report/estate_property_templates.xml',
       'report/estate_property_reports.xml',
       ]
}