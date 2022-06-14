# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 18:12:42 2022

@author: gorgi
"""

import sqlite3
conn = sqlite3.connect('database.db')
print("BD otwarta")
conn.execute('CREATE TABLE pracownicy (imieinazwisko TEXT, nrpracownika TEXT,adres TEXT)')
print("Tabela utworzona")
conn.close()
