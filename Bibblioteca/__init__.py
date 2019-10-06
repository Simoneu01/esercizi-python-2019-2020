# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Settembre 20/09/2019 09:35
# Created with PyCharm
# Project: Gestionale Bibblioteca

import json

from Classi.Bibblioteca import Bibblioteca
from Classi.Libri import Libro
from Classi.Prestito import Prestito
from Classi.Utenti import Utenti


def elenco_libri():
    print('LISTA LIBRI\n')
    print(' ' * (5 - len('ID')), 'ID',
          ' ' * (25 - len('TITOLO')), 'TITOLO',
          ' ' * (25 - len('GENERE')), 'GENERE',
          ' ' * (25 - len('AUTORE')), 'AUTORE',
          ' ' * (25 - len('ISBN')), 'ISBN',
          ' ' * (25 - len('IN PRESTITO?')), "IN PRESTITO?")
    print(' ' * (5 - len('ID')), '-' * len('ID'),
          ' ' * (25 - len('TITOLO')), '-' * len('TITOLO'),
          ' ' * (25 - len('GENERE')), '-' * len('GENERE'),
          ' ' * (25 - len('AUTORE')), '-' * len('AUTORE'),
          ' ' * (25 - len('ISBN')), '-' * len('ISBN'),
          ' ' * (25 - len('IN PRESTITO?')), '-' * len('IN PRESTITO?'))
    for libro in Bibblioteca.lista_libri:
        print(' ' * (5 - len(str(libro.libroid))), libro.libroid,
              ' ' * (25 - len(libro.titolo)), libro.titolo,
              ' ' * (25 - len(libro.genere)), libro.genere,
              ' ' * (25 - len(libro.autore)), libro.autore,
              ' ' * (25 - len(libro.isbn if hasattr(libro, 'isbn') else "N/A")),
              libro.isbn if hasattr(libro, 'isbn') else "N/A",
              ' ' * (25 - len(str(in_prestito(libro.libroid)))), in_prestito(libro.libroid),
              )


def in_prestito(id_libro):
    for i in Bibblioteca.lista_prestiti:
        if str(id_libro) == i.libroid:
            return True


def elenco_tesserati():
    print('ELENCO TESSERATI\n')
    print(' ' * (5 - len('ID')), 'ID',
          ' ' * (25 - len('NOME')), 'NOME',
          ' ' * (25 - len('COGNOME')), 'COGNOME',
          ' ' * (25 - len('EMAIL')), 'EMAIL',
          ' ' * (25 - len('TELEFONO')), 'TELEFONO',
          ' ' * (25 - len('CAP')), 'CAP',
          ' ' * (25 - len('CODICE FISCALE')), 'CODICE FISCALE'
          )
    print(' ' * (5 - len('ID')), '-' * len('ID'),
          ' ' * (25 - len('NOME')), '-' * len('NOME'),
          ' ' * (25 - len('COGNOME')), '-' * len('COGNOME'),
          ' ' * (25 - len('EMAIL')), '-' * len('EMAIL'),
          ' ' * (25 - len('TELEFONO')), '-' * len('TELEFONO'),
          ' ' * (25 - len('CAP')), '-' * len('CAP'),
          ' ' * (25 - len('CODICE FISCALE')), '-' * len('CODICE FISCALE')
          )
    for tesserato in Bibblioteca.lista_utenti:
        print(' ' * (5 - len(str(tesserato.userid))), tesserato.userid,
              ' ' * (25 - len(tesserato.nome)), tesserato.nome,
              ' ' * (25 - len(tesserato.cognome)), tesserato.cognome,
              ' ' * (25 - len(tesserato.email)), tesserato.email,
              ' ' * (25 - len(tesserato.telefono)), tesserato.telefono,
              ' ' * (25 - len(tesserato.cap if hasattr(tesserato, 'cap') else "N/A")),
              tesserato.cap if hasattr(tesserato, 'cap') else "N/A",
              ' ' * (25 - len(tesserato.codice_fiscale if hasattr(tesserato, 'codice_fiscale') else "N/A")),
              tesserato.codice_fiscale if hasattr(tesserato, 'codice_fiscale') else "N/A"
              )


def elenco_prestiti(ritardo=False):
    if ritardo:
        print('LISTA PRESTITI IN RITARDO\n')
        print('LISTA PRESTITI\n')
        print(' ' * (5 - len('ID')), 'ID',
              ' ' * (25 - len('ID LIBRO')), 'ID LIBRO',
              ' ' * (25 - len('ID TESSERATO')), 'ID TESSERATO',
              ' ' * (25 - len('IN RITARDO?')), 'IN RITARDO?',
              ' ' * (25 - len('PRESO IL')), 'PRESO IL',
              ' ' * (25 - len('SCADENZA')), 'SCADENZA',
              )

        print(' ' * (5 - len('ID')), '-' * len('ID'),
              ' ' * (25 - len('ID LIBRO')), '-' * len('ID LIBRO'),
              ' ' * (25 - len('ID TESSERATO')), '-' * len('ID TESSERATO'),
              ' ' * (25 - len('IN RITARDO?')), '-' * len('IN RITARDO?'),
              ' ' * (25 - len('PRESO IL')), '-' * len('PRESO IL'),
              ' ' * (25 - len('SCADENZA')), '-' * len('SCADENZA')
              )
        for prestito in Bibblioteca.lista_prestiti:
            prestito.check_ritardo()
            if prestito.in_ritardo:
                print(' ' * (5 - len(str(prestito.prestitoid))), prestito.prestitoid,
                      ' ' * (25 - len(prestito.libroid)), prestito.libroid,
                      ' ' * (25 - len(prestito.utenteid)), prestito.utenteid,
                      ' ' * (25 - len(str(prestito.in_ritardo))), prestito.in_ritardo,
                      ' ' * (25 - len(prestito.preso_il)), prestito.preso_il,
                      ' ' * (25 - len(prestito.scadenza)), prestito.scadenza,
                      )
    else:
        print('LISTA PRESTITI\n')
        print(' ' * (5 - len('ID')), 'ID',
              ' ' * (25 - len('ID LIBRO')), 'ID LIBRO',
              ' ' * (25 - len('ID TESSERATO')), 'ID TESSERATO',
              ' ' * (25 - len('IN RITARDO?')), 'IN RITARDO?',
              ' ' * (25 - len('PRESO IL')), 'PRESO IL',
              ' ' * (25 - len('SCADENZA')), 'SCADENZA',
              )

        print(' ' * (5 - len('ID')), '-' * len('ID'),
              ' ' * (25 - len('ID LIBRO')), '-' * len('ID LIBRO'),
              ' ' * (25 - len('ID TESSERATO')), '-' * len('ID TESSERATO'),
              ' ' * (25 - len('IN RITARDO?')), '-' * len('IN RITARDO?'),
              ' ' * (25 - len('PRESO IL')), '-' * len('PRESO IL'),
              ' ' * (25 - len('SCADENZA')), '-' * len('SCADENZA')
              )

        for prestito in Bibblioteca.lista_prestiti:
            prestito.check_ritardo()
            print(' ' * (5 - len(str(prestito.prestitoid))), prestito.prestitoid,
                  ' ' * (25 - len(prestito.libroid)), prestito.libroid,
                  ' ' * (25 - len(prestito.utenteid)), prestito.utenteid,
                  ' ' * (25 - len(str(prestito.in_ritardo))), prestito.in_ritardo,
                  ' ' * (25 - len(prestito.preso_il)), prestito.preso_il,
                  ' ' * (25 - len(prestito.scadenza)), prestito.scadenza,
                  )


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
    # Gestione Prestiti
    elif scelta == '3':
        print('\n******GESTIONE PRESTITI******')
        if input("\nVuoi visualizzare l'elenco libri? [SI/NO]\n>>>").upper() == 'SI':
            elenco_libri()
        if input("\nVuoi visualizzare l'elenco tesserati? [SI/NO]\n>>>").upper() == 'SI':
            elenco_tesserati()
        libro = input("Inserisci l'ID del libro: ")
        utenteID = input("Inserisci l'ID dell'utente: ")
        if in_prestito(libro):
            print('Libro attualmente in prestito')
        else:
            prestito = Prestito(Bibblioteca.prestitiID, libro, utenteID)
            for tesserato in Bibblioteca.lista_utenti:
                if str(tesserato.userid) == utenteID:
                    tesserato.aggiungi_libro(prestito)
            Bibblioteca.aggiungi_prestito(prestito)
    # Gestione Reso
    elif scelta == '4':
        print('\n******GESTIONE RESI ******')
        if input("\nVuoi visualizzare l'elenco prestiti? [SI/NO]\n>>>").upper() == 'SI':
            elenco_prestiti()
        reso = input("Inserisci l'ID del prestito: ")
        for prestito in Bibblioteca.lista_prestiti:
            if str(prestito.prestitoid) == reso:
                Bibblioteca.lista_prestiti.remove(prestito)
    # Modifica e Cancellazione Libro
    elif scelta == '5':
        if input("\nVuoi visualizzare l'elenco libri? [SI/NO]\n>>>").upper() == 'SI':
            elenco_libri()
        libroID = input("Inserisci l'ID del libro: ")

        while True:
            a = input("\nVuoi modificare o eliminare il libro?\n1.Modificare\n2.Eliminare"
                      "(VERRANNO RIMOSSI ANCHE I PRESTITI COLEGATI AL LIBRO)\n>>>")
            if a == '1':
                for libro in Bibblioteca.lista_libri:
                    if libroID == str(libro.libroid):
                        titolo = input('Inserisci titolo: ')
                        genere = input('Inserisci genere: ')
                        autore = input('Inserisci autore: ')
                        isbn = input('(Opzionale) Inserisci isbn: ')
                        libro.modifica(titolo, genere, autore, isbn if isbn != '' else None)
                break
            elif a == '2':
                print('ATTENZIONE VERRANNO RIMOSSI ANCHE I PRESTITI COLEGATI AL LIBRO')
                # Rimuovo il libro
                for libro in Bibblioteca.lista_libri:
                    if str(libro.libroid) == libroID:
                        Bibblioteca.lista_libri.remove(libro)
                # Rimuovo i Prestiti legati al libro
                for prestito in Bibblioteca.lista_prestiti:
                    if str(prestito.libroid) == libroID:
                        Bibblioteca.lista_prestiti.remove(prestito)
    # Modifica e Cancellazione Tesserato
    elif scelta == '6':
        if input("\nVuoi visualizzare l'elenco tesserati? [SI/NO]\n>>>").upper() == 'SI':
            elenco_tesserati()
        utenteID = input("Inserisci l'ID del tesserato: ")
        while True:
            a = input("\nVuoi modificare o eliminare il tesserato?\n1.Modificare\n2.Eliminare"
                      "(VERRANNO RIMOSSI ANCHE I PRESTITI COLEGATI AL TESSERATO)\n>>>")
            if a == '1':
                for tesserato in Bibblioteca.lista_utenti:
                    if utenteID == str(tesserato.utenteid):
                        nome = input('Inserisci nome: ')
                        cognome = input('Inserisci cognome: ')
                        email = input('Inserisci email: ')
                        telefono = input('Inserisci telefono: ')
                        codice_fiscale = input('(Opzionale) Inserisci codice fiscale: ')
                        cap = input('(Opzionale) Inserisci cap: ')
                        tesserato.modifica(nome, cognome, email, telefono,
                                           codice_fiscale if codice_fiscale != '' else None,
                                           cap if cap != '' else None)
                break
            elif a == '2':
                print('ATTENZIONE VERRANNO RIMOSSI ANCHE I PRESTITI COLLEGATI AL TESSERATO')
                # Rimuovo il tesserato
                for tesserato in Bibblioteca.lista_utenti:
                    if str(tesserato.utenteid) == utenteID:
                        Bibblioteca.lista_libri.remove(libro)
                # Rimuovo i Prestiti legati al libro
                for prestito in Bibblioteca.lista_prestiti:
                    if str(prestito.utenteid) == utenteID:
                        Bibblioteca.lista_prestiti.remove(prestito)
    # Visualizzazione Libri
    elif scelta == '7':
        elenco_libri()
    # Visualizzazione Tesserati
    elif scelta == '8':
        elenco_tesserati()
    # Visualizzazione Libri in Prestito
    elif scelta == '9':
        elenco_prestiti()
    # Visualizzazione Libri in Ritardo
    elif scelta == '10':
        elenco_prestiti(ritardo=True)
        if input("\nVuoi contattare il tesserato? [SI/NO]\n>>>").upper() == 'SI':
            tesseratoID = input("Inserisci l'ID dell'tesserato: ")
            for utente in Bibblioteca.lista_utenti:
                if str(tesseratoID) == str(utente.userid):
                    print('EMAIL - TELEFONO')
                    print(utente.email, '-', utente.telefono)
    # Uscita e Salvataggio su File
    elif scelta == '11':
        print('Grazie per aver usato il programma!')
        Bibblioteca.salva()
        break
