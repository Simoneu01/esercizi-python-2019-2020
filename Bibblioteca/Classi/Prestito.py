# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Ottobre 06/10/2019 14:59
# Created with PyCharm
# Project: Gestionale Bibblioteca

from datetime import datetime
from datetime import timedelta


class Prestito:
    def __init__(self, libroid, utenteid):
        self.libroid = libroid
        self.utenteid = utenteid
        self.in_presito = True  # Da vedere se serve
        self.preso_il = datetime.now()
        self.scadenza = self.preso_il + timedelta(days=15)  # 15 Giorni di Delta cioè aggiungo 15 giorni
