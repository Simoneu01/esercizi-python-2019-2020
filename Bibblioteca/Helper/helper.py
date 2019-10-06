# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Settembre 20/09/2019 09:35
# Created with PyCharm
# Project: Gestionale Bibblioteca

import os

# # Salva lista su File
# def salva_file(lista):
#    with open(nfile_rubrica_amici, 'a+') as f:
#         f.writelines('{0},{1},{2},{3},{4},\n'.format(lista))
#             if input('\nScrivi fine per terminare.....\n>>> ') == 'fine':
#                 break

# Rende una lista di liste una unica lista
def flat(lista):
    return [j for i in lista for j in i]


# Elimina un file
def elimina_file(nome_file):
    if os.path.isfile(nome_file):
        os.remove(nome_file)
        print('File {} cancellato'.format(nome_file))
    else:
        print('File {} non esiste'.format(nome_file))


def dict_categorie(nome_file):
    d = {}
    with open(nome_file) as f:
        next(f)
        for line in f:
            key, val, n = line.split(',')
            d[key] = val
    return d


# Genera una lista o lista di liste da un file di testo (non codificato)
def gen_list_from_txt(nome_file, sep=';', header=0, delete_chars='\n', cols=None):
    with open(nome_file) as f:
        if cols is None:
            return [record.replace(delete_chars, '').split(sep) for record in f.readlines()[header:]]
        return [record.replace(delete_chars, '').split(sep)[cols[0]:cols[1]:cols[2]] for record in f.readlines()[header:]]


# END
