# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Settembre 20/09/2019 09:35
# Created with PyCharm
# Project: Gestionale Bibblioteca

class Libro():
    def __init__(self, titolo, genere, autore, isbn):
        self.titolo = titolo
        self.genere = genere
        self.autore = autore
        self.isbn = isbn

    def modifica(self, titolo, genere, autore):
        if self.titolo != titolo:
            self.titolo = titolo
        if self.genere != genere:
            self.genere = genere
        if self.autore != autore:
            self.autore = autore
        if self.isbn != isbn:
            self.isbn = isbn
