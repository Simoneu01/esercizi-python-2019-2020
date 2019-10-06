####Biblioteca####
##By John Patrick Gabriel##
##Last update 6/10/2019 time:12.35Pm##

import datetime

##Classi##
class Libro:
    titolo = ''
    genere = ''
    autore = ''
    codice = ''
    prestato = ''

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

    def modificatuttolibro(self,titolo,autore,genere,codice,prestato):
        if titolo != '':
            self.titolo = titolo
        if autore != '':
            self.autore = autore
        if genere != '':
            self.genere = genere
        if codice != '':
            self.codice = codice
        if prestato != '':
            self.prestato = prestato

    def filelibri(self,f):
        f.write(self.titolo+','+self.autore+','+self.genere+','+self.codice+','+self.prestato+'\n')

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

    def modificatuttoutente(self,nome,cognome,codice,libroprenotato):
        if nome != '':
            self.nome = nome
        if cognome != '':
            self.cognome = cognome
        if codice != '':
            self.codice = codice
        if libroprenotato != '':
            self.libroprenotato = libroprenotato
    
    def fileutenti(self,f):
        f.write(self.nome+','+self.cognome+','+self.codice+','+self.libroprenotato+'\n')


        
##MAIN##
scelta = ''
lista_libri = []
lista_utenti = []
lista_prenotati = []

try:
    with open("Libri.txt") as f:
        read = f.readlines()
    for cont in range(len(read)):
        temp = read[cont]
        temp = temp.split(",")
        temp.remove("\n")
        libro = Libro(temp[0],temp[1],temp[2],temp[3],temp[4])
        lista_libri.append(libro)
except:
    pass

try:
  with open("Utenti.txt") as f:
    read = f.readlines()
    for cont in range(len(read)):
        temp = read[cont]
        temp = temp.split(",")
        temp.remove("\n")
        tesserato = Utente(temp[0],temp[1],temp[2],temp[3])
        lista_utenti.append(tesserato)
except:
    pass


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
        prestato = 'False'

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
                                if lista_libri[cont].prestato == 'False':
                                    prestato = 'True'
                                    lista_libri[cont].modificalibro(prestato)
                                    lista_utenti[cont].modificalibroprenotato(lista_libri[cont].codice)
                                    print(lista_libri[cont].visualizzalibro(),'\nLibro prenotato')
                                    giaprenotato = False
                                else:
                                    print('Libro gia prenotato.')

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
                                if lista_libri[cont].prestato == 'True':
                                    prestato = 'False'
                                    lista_libri[cont].modificalibro(prestato)
                                    libroprenotato = 'False'
                                    lista_utenti[cont].modificalibroprenotato(libroprenotato)
                                    print(lista_libri[cont].visualizzalibro(),'\nReso effettuato')
                                    giareso = True
                                else:
                                    print('Reso gia effettuato.')

            if giareso == False:
                print('\n\n\nL\'utente non ha un libro prenotato o ha inserito il codice utente sbagliato.')

        else:
            print('\n\n\nLibro non trovato.')
            

    ##Ricerca/Modifica/Cancellazione di un libro##
    elif scelta == '5':
        nonmodifica = False
        modifica = input('Inserire il codice del libro da ricercare: ')
        
        for cont in range (len(lista_utenti)):
            if lista_utenti[cont].libroprenotato == modifica:
                nonmodifica = True
                
        if nonmodifica == False:
            trovato = False
            for cont in range(len(lista_libri)):
                if modifica == lista_libri[cont].codice:
                    trovato = True
                    print(lista_libri[cont].visualizzalibro())
                    modcanc = input('Desidera modificare o cancellare il libro?\n1-Modifica\n2-Cancella\n>>>')

                    if modcanc == '1':
                        titolo = input('Inserire il nuovo titolo oppure lasciare vuoto con invio: ')
                        autore = input('Inserire il nuovo autore oppure lasciare vuoto con invio: ')
                        genere = input('Inserire il nuovo genere oppure lasciare vuoto con invio: ')
                        codice = input('Inserire il nuovo codice oppure lasciare vuoto con invio: ')
                        prestato = 'False'
                        
                        lista_libri[cont].modificatuttolibro(titolo,autore,genere,codice,prestato)
                    
                    elif modcanc == '2':
                        lista_libri.remove(lista_libri[cont])
                    else:
                        print('\n\n\nErrore....riprovare.')

            if trovato == False:
                print('\n\n\nLibro non trovato.')
        else:
            print('\n\n\nUn utente ha il libro prenotato...Impossibile modificare o cancellare il libro richiesto.')

    ##Ricerca/Modifica/Cancellazione di un tesserato
    elif scelta == '6':
        nonmodifica = False
        modifica = input('Inserire il codice utente da ricercare: ')
        
        for cont in range (len(lista_utenti)):
            if lista_utenti[cont].libroprenotato != False:
                nonmodifica = True

        if nonmodifica == False:     
            trovato = False
            for cont in range(len(lista_utenti)):
                if modifica == lista_utenti[cont].codice:
                    trovato = True
                    print(lista_utenti[cont].visualizzalibro())
                    modcanc = input('Desidera modificare o cancellare il libro?\n1-Modifica\n2-Cancella\n>>>')

                    if modcanc == '1':
                        nome = input('Inserire il nuovo nome oppure lasciare vuoto con invio: ')
                        cognome = input('Inserire il nuovo cognome oppure lasciare vuoto con invio: ')
                        codice = input('Inserire il nuovo codice oppure lasciare vuoto con invio:')
                        libroprenotato = 'False'

                        lista_utenti[cont].modificatuttoutente(nome,cognome,genere,codice,prestato)
                        
                    elif modcanc == '2':
                        lista_utenti.remove(lista_utenti[cont])
                    else:
                        print('\n\n\nErrore....riprovare.')
                        
            if trovato == False:
                print('\n\n\nTesserato non trovato.')
        else:
            print('\n\n\nUn utente ha il libro prenotato...Impossibile modificare o cancellare il tesserato richiesto.')

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

with open("Libri.txt","w") as f: 
    for cont in range(len(lista_libri)):
        lista_libri[cont].filelibri(f)
        
with open("Utenti.txt","w") as f:
    for cont in range(len(lista_utenti)):
        lista_utenti[cont].fileutenti(f)

    
