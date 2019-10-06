# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Settembre 20/09/2019 09:35
# Created with PyCharm
# Project: Gestionale Bibblioteca

# TODO:

from Classi import *
import json
from appJar import gui

# create a GUI variable called app
app = gui("Gestionale Bibblioteca", "1920x1080")
app.setFont(18)


def menuPress(button):
    if button == 'Aggiungi Tesserato':
        pass

def editPress(button):
    pass

def reportPress(button):
    if button == 'Elenco Tesserati':
        app.removeAllWidgets()
        app.addLabel("l1", "Label 1")
        app.addLabel("l2", "Label 2")
        app.addLabel("l3", "Label 3")
    else:
        print('BOH')

def press(button):
    app.getAllEntries()
    print(app.getAllEntries())


# handle button events
def menuPress(button):
    if button == "Inserisci Tesserato":
        app.removeAllWidgets()
        app.addLabel('Inserisci', 'Inserisci',0,1)
        app.addLabel('3', ' ',0,0)
        app.addLabel('2', ' ',0,2)
        app.setLabelBg("Inserisci", "blue")
        app.setLabelBg("3", "blue")
        app.setLabelBg("2", "blue")
        app.setLabelFg("Inserisci", "orange")
        app.addLabel('Nome', 'Nome' ,1,0)
        app.addEntry('nome', 1,1)
        app.setEntryDefault('nome','Simone')
        app.addLabel('Cognome', 'Cognome' ,2,0)
        app.addEntry('cognome',2,1)
        app.setEntryDefault('cognome','Ungaro')
        app.addLabel('Email', 'Email' ,3,0)
        app.addEntry('email',3,1)
        app.setEntryDefault('emal','scuola@libero.it')
        app.addLabel('Telefono', 'Telefono' ,4,0)
        app.addEntry('telefono',4,1)
        app.setEntryDefault('telefono','02 282446201')
        app.addLabel('cap', 'CAP / ZIP CODE' ,5,0)
        app.addEntry('cap',5,1)
        app.setEntryDefault('cap','20100')
        app.addLabel('codice_fiscale', 'Codice Fiscale' ,6,0)
        app.addEntry('codice_fiscale',6,1)
        app.setEntryDefault('codice_fiscale','NGRSMW09IB2774W')
        app.addButton('Salva',press,7,2)
    elif button == "Modifica":
        app.removeAllWidgets()
        app.addLabel('Modifica', 'Modifica', 0, 1)
        app.addLabel('3', ' ',0,0)
        app.addLabel('2', ' ',0,2)
        app.setLabelBg("Modifica", "blue")
        app.setLabelFg("Modifica", "orange")
        app.setLabelBg("3", "blue")
        app.setLabelBg("2", "blue")
        app.addLabel('Nome', 'Nome' ,1,0)
        app.addEntry('Nome', 1,1)
        app.addLabel('Cognome', 'Cognome' ,2,0)
        app.addEntry('Cognome',2,1)
        app.addLabel('Email', 'Email' ,3,0)
        app.addEntry('Email',3,1)
        app.addLabel('Telefono', 'Telefono' ,4,0)
        app.addEntry('Telefono',4,1)
        app.addLabel('Categoria', 'Categoria' ,5,0)
        app.addOptionBox("Categoria", ["Amici di Scuola", "Amici di Studio", "Amici del Cuore"],5,1)
        app.addButton('Salva',press,6,2)
    elif button == "Cerca":
        app.removeAllWidgets()
    elif button == "Visualizza":
        app.removeAllWidgets()
        app.addTable("g1",
        [["Nome", "Cognome", "Email", "Telefono", "Categoria"]])
    elif button == "Esci":
        app.stop()
    else:
        print("Errore")


# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to Gestionale Bibblioteca")

app.setLabelBg("title", "blue")
fileMenus = ["Inserisci Libro", "Inserisci Tesserato", "-", "Prestito", "-", "Esci"]
editMenus = ["Ricerca/Modifca/Cancella Libro", "Ricerca/Modifca/Cancella Tesserato", "-", "Esci"]
app.addMenuList("Inserimenti / Prestiti", fileMenus, menuPress) # create the File menu, with the list of items
app.addMenuList("Modifica", editMenus, editPress) # create the File menu, with the list of items
reportMenus = ["Elenco Libri", "Elenco Tesserati", "Elenco libri in Prestito", "Elenco libri in Ritarto", "-", "Esci"]
app.addMenuList("Report", reportMenus, reportPress) # create the File menu, with the list of items

app.setLabelFg("title", "orange")
# start the GUI
app.go()
