# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Settembre 20/09/2019 09:35
# Created with PyCharm
# Project: Gestionale Bibblioteca

class Utenti():
    def __init__(self, userid, nome, cognome, email, telefono, codice_fiscale=None, cap=None):
        self.userid = userid
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.telefono = telefono
        self.cap = cap
        self.codice_fiscale = codice_fiscale
        self.lista_libri = []

    def modifica(self, nome, cognome, email, telefono, cap, codice_fiscale):
        if self.nome != nome & nome != '':
            self.nome = nome
        if self.cognome != cognome & cognome != '':
            self.cognome = cognome
        if self.email != email & email != '':
            self.email = email
        if self.telefono != telefono & telefono != '':
            self.telefono = telefono
        if self.codice_fiscale != codice_fiscale & codice_fiscale != '':
            self.codice_fiscale = codice_fiscale
        if self.cap != cap & cap != '':
            self.cap = cap

    def aggiungi_libro(self, id_libro):
        self.lista_libri.append(id_libro)