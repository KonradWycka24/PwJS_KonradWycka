import sqlite3
conn = sqlite3.connect('database.db')
print("BD otwarta")

conn.execute('CREATE TABLE uzytkownicy (login_ TEXT , haslo TEXT')
