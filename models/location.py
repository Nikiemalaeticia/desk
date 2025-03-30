from odoo import models, fields

class Appartement(models.Model):
    _name = 'appartement'
    _description = 'Appartement'

    name = fields.Char(string='Nom')
    adresse = fields.Text(string='Adresse')

class Partenaire(models.Model):
    _name = 'partenaire'
    _description = 'Partenaire'

    name = fields.Char(string='Nom')
    l_immo = fields.Many2one("appartement", string="Appartement")
    l_location = fields.Many2one("partenaire", string="Location")
    l_bailleur = fields.Many2one("partenaire", string="Bailleur") 
    prix = fields.Float(string="Prix de location")
    date_debut_location = fields.date(string="date du debut de la location")
    date_fin_location = fields.date(string="date de fin de la location")
