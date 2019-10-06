# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Ottobre 06/10/2019 14:59
# Created with PyCharm
# Project: Gestionale Bibblioteca

from datetime import datetime
from datetime import timedelta


class Prestito:
    def __init__(self, prestitoid, libroid, utenteid, in_ritardo=None, preso_il=None, scadenza=None):
        self.prestitoid = prestitoid
        self.libroid = libroid
        self.utenteid = utenteid
        self.in_ritardo = in_ritardo if in_ritardo else False
        self.preso_il = preso_il if preso_il else datetime.today()
        self.scadenza = scadenza if scadenza else self.preso_il + timedelta(days=15)  # 15 Giorni di Delta cioè aggiungo 15 giorni
        self.preso_il = self.preso_il.__str__()
        self.scadenza = self.scadenza.__str__()

    def check_ritardo(self):
        if self.scadenza < datetime.today().__str__():
            self.in_ritardo = True
