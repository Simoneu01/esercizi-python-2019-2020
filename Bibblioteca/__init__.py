# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Settembre 20/09/2019 09:35
# Created with PyCharm
# Project: Gestionale Bibblioteca

import json

from Classi.Bibblioteca import Bibblioteca
from Classi.Libri import Libro
from Classi.Utenti import Utenti

Bibblioteca = Bibblioteca()
while True:
    print('\n******MENU PRINCIPALE******')
    scelta = input('\n'
                   '1-Inserimento Libro\n'
                   '2-Anagrafica tesserati\n'
                   '3-Prestito\n'
                   '4-Reso\n'
                   '5-Ricerca/modifica/cancellazione libro\n'
                   '6-Ricerca/modifica/cancellazione tesserato\n'
                   '7-Elenco Libro\n'
                   '8-Elenco tesserati\n'
                   '9-Elenco libri in prestito\n'
                   '10-Elenco libri in ritardo\n'
                   '11-Esci\n\n>>> ')
    # Inserimento Libro
    if scelta == '1':
        titolo = input('Inserisci titolo: ')
        genere = input('Inserisci genere: ')
        autore = input('Inserisci autore: ')
        isbn = input('(Opzionale) Inserisci isbn: ')

        Bibblioteca.aggiungi_libro(Libro(Bibblioteca.libriID, titolo, genere, autore, isbn if isbn != '' else None))
    # Inserimento Tesserato
    elif scelta == '2':
        nome = input('Inserisci nome: ')
        cognome = input('Inserisci cognome: ')
        email = input('Inserisci email: ')
        telefono = input('Inserisci telefono: ')
        codice_fiscale = input('(Opzionale) Inserisci codice fiscale: ')
        cap = input('(Opzionale) Inserisci cap: ')

        Bibblioteca.aggiungi_utente(Utenti(Bibblioteca.utentiID, nome, cognome, email, telefono,
                                           codice_fiscale if codice_fiscale != '' else None,
                                           cap if cap != '' else None))
    # Visualizzazione Libri
    elif scelta == '7':
        print('LISTA LIBRI\nTitolo\tGenere\tAutore\tISBN (Ove disponibile)')
        for libro in Bibblioteca.lista_libri:
            print(libro.titolo, '\t', libro.genere, '\t', libro.autore, '\t',
                  libro.isbn if hasattr(libro, 'isbn') else "N/A")
    # Uscita e Salvataggio su File
    elif scelta == '11':
        print('Grazie per aver usato il programma!')
        Bibblioteca.salva()
        break
