# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Settembre 20/09/2019 09:35
# Created with PyCharm
# Project: Gestionale Bibblioteca

class Libro():
    def __init__(self, libroid, titolo, genere, autore, isbn=None):
        self.libroid = libroid
        self.titolo = titolo
        self.genere = genere
        self.autore = autore
        if isbn:
            self.isbn = isbn

    def modifica(self, titolo, genere, autore, isbn):
        if self.titolo != titolo & titolo != '':
            self.titolo = titolo
        if self.genere != genere & genere != '':
            self.genere = genere
        if self.autore != autore & autore != '':
            self.autore = autore
        if self.isbn != isbn & isbn != '':
            self.isbn = isbn
