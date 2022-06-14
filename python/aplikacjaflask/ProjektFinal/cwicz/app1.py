from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)
@app.route("/")
def main():
 return render_template('index.html')
@app.route("/dodaj")
def new_student():
 return render_template('studentadd.html')
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
 if request.method == 'POST':
     try:
         nazwisko = request.form['imienazwisko']
         adres = request.form['adres']
         miasto = request.form['miasto']
         nrindeksu = request.form['indeks']

         with sql.connect("database.db") as con:
             cur = con.cursor()
             cur.execute("INSERT INTO studenci (nazwisko,adres,miasto,nrindeksu) VALUES(?,?,?,?)",(nazwisko,adres,miasto,nrindeksu) )
             con.commit()
             msg = "Rekord zapisany"
             
        except:
            con.rollback()
            msg = "Blad przy dodawaniu rekordu"

        finally:
            return render_template("rezultat.html",msg = msg)
            con.close()
