# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Settembre 20/09/2019 09:35
# Created with PyCharm
# Project: Gestionale Bibblioteca

import os
import json

nome_libri_json= "../Database/libri.json"
nome_utenti_json= '../Database/utenti.json'

class Bibblioteca():
    def __init__(self):
        if os.path.isfile(nome_libri_json):
            if os.path.isfile(nome_utenti_json):
                self.lista_libri = json.load(nome_libri_json)
                self.lista_utenti = json.load(nome_utenti_json)
            else:
                self.lista_libri=[]
                self.lista_utenti=[]
        else:
            self.lista_libri=[]
            self.lista_utenti=[]

    def aggiungi_libri(self, Libro):
        self.lista.append(Libro)

    def aggiungi_utente(self, Utente):
        self.lista.append(Utente)

    def salva_file_libri(self):
        with open(nome_libri_json, 'w') as outfile:
            for libro in self.lista_libri:
                json.dump(libro.__dict__, outfile, indent=4)

    def salva_file_utente(self):
        with open(nome_utenti_json, 'w') as outfile:
            for utente in self.lista_utenti:
                json.dump(libro.__dict__, outfile, indent=4)
