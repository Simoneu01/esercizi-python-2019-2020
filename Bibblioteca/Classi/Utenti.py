# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Settembre 20/09/2019 09:35
# Created with PyCharm
# Project: Gestionale Bibblioteca

class Utenti():
    def __init__(self, data):
        self.nome = data[nome]
        self.cognome = data[cognome]
        self.email = data[email]
        self.telefono = data[telefono]
        self.cap = data[cap]
        self.codice_fiscale = data[codice_fiscale]
        self.lista_libri = data[lista_libri]

    def modifica(self, nome, cognome, email, telefono, cap, codice_fiscale):
        if self.nome != nome:
            self.nome = nome
        if self.cognome != cognome:
            self.cognome = cognome
        if self.email != email:
            self.email = email
        if self.telefono != telefono:
            self.telefono = telefono
        if self.codice_fiscale != codice_fiscale:
            self.codice_fiscale = codice_fiscale
        if self.cap != cap:
            self.cap = cap
