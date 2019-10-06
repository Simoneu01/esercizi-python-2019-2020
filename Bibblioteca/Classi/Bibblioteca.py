# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Settembre 20/09/2019 09:35
# Created with PyCharm
# Project: Gestionale Bibblioteca

import os
import json

from Classi.Libri import Libro
from Classi.Utenti import Utenti

nome_libri_json = ".\\Database\\libri.json"
nome_utenti_json = '.\\Database\\utenti.json'
nome_data_json = '.\\Database\\data.json'


def obj_dict(obj):
    return obj.__dict__


class Bibblioteca:
    def __init__(self):
        # Gestione Lista Libri
        if os.path.isfile(nome_libri_json):
            with open(nome_libri_json, "r") as read_file:
                self.lista_libri = json.load(read_file)
            new_list = []
            for libro in self.lista_libri:
                new_list.append(Libro(libro["titolo"], libro["genere"], libro["autore"],
                                      libro['isbn'] if 'isbn' in libro else None))
            self.lista_libri = new_list
        else:
            self.lista_libri = []
        # Gestione Lista Utente
        if os.path.isfile(nome_utenti_json):
            with open(nome_utenti_json, "r") as read_file:
                self.lista_utenti = json.load(read_file)
            new_list = []
            for utente in self.lista_utenti:
                new_list.append(Utenti(utente["nome"], utente["cognome"], utente["email"], utente["telefono"],
                                       utente["codice_fiscale"] if 'codice_fiscale' in utente else None,
                                       utente["cap"] if 'cap' in utente else None))
            self.lista_libri = new_list
        else:
            self.lista_utenti = []

        # AI Utenti e Libri
        if os.path.isfile(nome_data_json):
            with open(nome_data_json, "r") as read_file:
                data = json.load(read_file)
                self.utentiID = data['Identificativo_Utente_AI']
                self.libriID = data['Identificativo_Libro_AI']
        else:
            self.utentiID = 0
            self.libriID = 0

    def incrementa_utenti_id(self):
        self.utentiID += 1

    def incrementa_libri_id(self):
        self.libriID += 1

    def aggiungi_libro(self, libro):
        self.lista_libri.append(libro)
        self.incrementa_libri_id()

    def aggiungi_utente(self, utente):
        self.lista_utenti.append(utente)
        self.incrementa_utenti_id()

    def salva_file_libri(self):
        with open(nome_libri_json, 'w') as outfile:
            json.dump(self.lista_libri, outfile, indent=4, default=obj_dict)

    def salva_file_utente(self):
        with open(nome_utenti_json, 'w') as outfile:
            json.dump(self.lista_utenti, outfile, indent=4, default=obj_dict)

    def salva_file_data(self):
        with open(nome_data_json, 'w') as outfile:
            json.dump(dict(Identificativo_Utente_AI=self.utentiID, Identificativo_Libro_AI=self.libriID),
                      outfile, indent=4)

    def salva(self):
        self.salva_file_libri()
        self.salva_file_utente()
        self.salva_file_data()
