####Biblioteca####
##By John Patrick Gabriel##
##Last update 4/10/2019 time:12.35Pm##

import datetime

##Classi##
class Libro:
    def __init__(self,titolo,autore,genere,codice,prestato):
        self.titolo = titolo
        self.autore = autore
        self.genere = genere
        self.codice = codice
        self.prestato = prestato

    def visualizzalibro(self):
        print(self.titolo,self.autore,self.genere,self.codice,self.prestato)

    def modificalibro(self,prestato):
        self.prestato = prestato

class Utente:
    nome = ''
    cognome = ''
    codice = ''
    libroprenotato = ''

    def __init__(self,nome,cognome,codice, libroprenotato):
        self.nome = nome
        self.cognome = cognome
        self.codice = codice
        self.libroprenotato = libroprenotato

    def visualizzautente(self):
        print(self.nome,self.cognome,self.codice,self.libroprenotato)

    def modificalibroprenotato(self,libroprenotato):
        self.libroprenotato = libroprenotato

##MAIN##
scelta = ''
lista_libri = []
lista_utenti = []
lista_prenotati = []

while(scelta != '11'):
    print('''
1-Inserimento Libro
2-Anagrafica tesserati
3-Prestito
4-Reso
5-Ricerca/modifica/cancellazione libro
6-Ricerca/modifica/cancellazione tesserato
7-Elenco Libro
8-Elenco tesserati
9-Elenco libri in prestito
10-Elenco libri in ritardo
11-Esci
''')
    scelta = input('>>>') #Scelta menu

    ##Inserimento Libro##
    if scelta == '1':
        titolo = input('Inserire il titolo del libro: ')
        autore = input('Inserire l\'autore del libro: ')
        genere = input('Inserire il genere del libro: ')
        codice = input('Inserire il codice del libro: ')
        prestato = False

        libro = Libro(titolo,autore,genere,codice,prestato)

        lista_libri.append(libro)

    ##Inserimento dati utente##
    elif scelta == '2':
        nome = input('Inserire il nome dell\'utente: ')
        cognome = input('Inserire il cognome dell\'utente: ')
        codice = input('Inserire il codice dell\'utente: ')
        libroprenotato = 'False'

        utente = Utente(nome,cognome,codice,libroprenotato)

        lista_utenti.append(utente)

    ##Prenotazione del libro##
    elif scelta == '3':
        cercalib = input('Inserire il codice del libro da ricercare: ')
        trovato = False
        for cont in range(len(lista_libri)):
            if cercalib == lista_libri[cont].codice:
                lista_libri[cont].visualizzalibro()
                trovato = True

        if trovato == True:
            giaprenotato = True
            ricercacodiceutente= input('Inserire il codice dell\'utente: ')
            for cont in range(len(lista_utenti)):
                    if ricercacodiceutente == lista_utenti[cont].codice and lista_utenti[cont].libroprenotato == 'False':     
                        for cont in range(len(lista_libri)):
                            if cercalib == lista_libri[cont].codice:
                                if lista_libri[cont].prestato == False:
                                    prestato = True
                                    lista_libri[cont].modificalibro(prestato)
                                    lista_utenti[cont].modificalibroprenotato(lista_libri[cont].codice)
                                    print(lista_libri[cont].visualizzalibro(),'\nLibro prenotato')
                                    giaprenotato = False
                                else:
                                    print('Libro gia prenotato.')

                    elif lista_utenti[cont].libroprenotato != 'False':
                        giaprenotato = True

            if giaprenotato == True:
                print('\n\n\nL\'utente ha gia un libro prenotato o ha inserito il codice utente sbagliato.')

        else:
            print('\n\n\nLibro non trovato.')

    ##Richiesta reso##
    elif scelta == '4':
        cercalib = input('Inserire il codice del libro da ricercare: ')
        trovato = False
        for cont in range(len(lista_libri)):
            if cercalib == lista_libri[cont].codice:
                lista_libri[cont].visualizzalibro()
                trovato = True


        if trovato == True:
            nontrovato = True
            ricercacodiceutente= input('Inserire il codice dell\'utente: ')
            for cont in range(len(lista_utenti)):
                    if ricercacodiceutente == lista_utenti[cont].codice and lista_utenti[cont].libroprenotato != 'False':     
                        for cont in range(len(lista_libri)):
                            if cercalib == lista_libri[cont].codice:
                                if lista_libri[cont].prestato == True:
                                    prestato = False
                                    lista_libri[cont].modificalibro(prestato)
                                    libroprenotato = 'False'
                                    lista_utenti[cont].modificalibroprenotato(libroprenotato)
                                    print(lista_libri[cont].visualizzalibro(),'\nReso effettuato')
                                    giareso = True
                                else:
                                    print('Reso gia effettuato.')

                    elif lista_utenti[cont].libroprenotato == 'False':
                        giareso = False

            if giareso == False:
                print('\n\n\nL\'utente non ha un libro prenotato o ha inserito il codice utente sbagliato.')

        else:
            print('\n\n\nLibro non trovato.')
            

    ##Ricerca/Modifica/Cancellazione di un libro##
    elif scelta == '5':
        modifica = input('Inserire il codice del libro da ricercare: ')

        trovato= False
        for cont in range(len(lista_libri)):
            if modifica == lista_libri[cont].codice:
                trovato = True
                print(lista_libri[cont].visualizzalibro())
                modcanc = input('Desidera modificare o cancellare il libro?\n1-Modifica\n2-Cancella\n>>>')

                if modcanc == '1':
                    titolo = input('')
                    autore = input('')
                    genere = input('')
                    codice = input('')
                    prestato = False
                    
                elif modcanc == '2':
                    pass
                else:
                    print('\n\n\nErrore....riprovare.')

        if trovato == False:
            print('\n\n\nLibro non trovato.')

    ##Ricerca/Modifica/Cancellazione di un tesserato
    elif scelta == '6':
        modifica = input('Inserire il codice del libro da ricercare: ')

        trovato= False
        for cont in range(len(lista_utenti)):
            if modifica == lista_utenti[cont].codice:
                trovato = True
                print(lista_utenti[cont].visualizzalibro())

        if trovato == True:
            modcanc = input('Desidera modificare o cancellare il libro?\n1-Modifica\n2-Cancella\n>>>')


            if modcanc == '1':
                pass
            elif modcanc == '2':
                pass
            else:
                print('\n\n\nErrore....riprovare.')
        else:
            print('\n\n\nTesserato non trovato.')

    ##Visualizzazione di tutti i libri##
    elif scelta == '7':
        for cont in range(len(lista_libri)):
            print(lista_libri[cont].visualizzalibro())

        menu = input('\n\n\nSchiacciare qualsiasi tasto per ritornare nel menu principale: ')

    ##Visualizzazione dei tesserati##
    elif scelta == '8':
        for cont in range(len(lista_utenti)):
            print(lista_utenti[cont].visualizzautente())

        menu = input('\n\n\nSchiacciare qualsiasi tasto per ritornare nel menu principale: ')

    ##Visualizzazione dei libri prenotati##
    elif scelta == '9':
        niente = False
        for cont in range(len(lista_libri)):
            if lista_libri[cont].prestato == True:
                print(lista_libri[cont].visualizzalibro())
                niente = True

        if niente == False:
            print('\n\n\nNessun libro prenotato trovato.')

    ##Visualizzazione dei libri in ritardo##
    elif scelta == '10':
        pass

        if niente == False:
            print('\n\n\nNessun libro prenotato trovato.')

    ##Uscita dal programma##
    elif scelta == '11':
        print('\n\nUscito con successo!!!')

    ##Messaggio di errore##
    else:
        print('\n\nErrore......')




##l'ora attuale##
##time.ctime()
