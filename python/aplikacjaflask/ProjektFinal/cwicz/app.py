from flask import Flask, render_template, request , redirect, url_for, Response, session,abort
from flask_socketio import SocketIO, join_room 
from flask_login import LoginManager, UserMixin,login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import sqlite3 as sql
app = Flask(__name__)
socketio = SocketIO(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseacc.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False , unique=True)
    password = db.Column(db.String(80), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'Użytkownik istnieje, zaloguj sie lub stwórz konto z inną nazwa')

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

@app.route("/")
def main():
    dane= {'tytul':'Strona główna','tresc':'Witaj na stronie glownej.'}
    return render_template('index.html',tytul=dane['tytul'],tresc=dane['tresc'])

@app.route("/about")
def about_me():
    dane = {'tytul':'O mnie', 'tresc':'Strona o mnie.','ja':'Konrad Wycka'}
    return render_template('omnie.html',tytul=dane['tytul'],tresc=dane['tresc'])

@app.route("/dodaj")
@login_required
def new_student():
    dane = {'tytul':'Dodaj pracownika','tresc':'Formularz dodawania pracownika'}
    return render_template('dodaj.html',tytul=dane['tytul'],tresc=dane['tresc'],)

@app.route("/info")
def info():
    dane = {'tytul':'Informacje','tresc':'Strona Informacyjna'}
    posty = [
        {
            'author': {'username':'Konrad'},
            'body': 'Witam na mojej stronie Flask!'
            }]
    return render_template('informacje.html',tytul=dane['tytul'],tresc=dane['tresc'],posty=posty)

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nazwisko = request.form['imienazwisko']
            nrprac = request.form['nrprac']
            adres = request.form['adres']
            
            with sql.connect("database.db") as con:
                cur=con.cursor()
                cur.execute("INSERT INTO pracownicy (imieinazwisko,nrpracownika ,adres) VALUES (?,?,?)",(nazwisko,nrprac,adres))
                wiadomosc = "dodano"
                con.commit()
                
        except:
            wiadomosc = "niedodano"
            con.rollback()
            
            
            
            
        finally:
            return render_template('rezultat.html', wiadomosc=wiadomosc,user=current_user.username)
            con.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main'))
    return render_template('formularz_logowania.html', form=form,)

@app.route('/rejestr', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('rejestracja.html', form=form)       

@app.route("/lista")
@login_required
def lista():
    dane =  dane = {'tytul':'Lista','tresc':'Lista pracowników'}
    con = sql.connect("database.db")
    con.row_factory=sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM pracownicy ORDER BY imieinazwisko')
    rekordy = cur.fetchall();
    return render_template('lista.html',tytul=dane['tytul'],tresc=dane['tresc'],rekordy=rekordy )


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main'))

@app.route('/czatlog')
@login_required
def m():
    return render_template("czatlog.html" )
@app.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')
    if username and room:
        
        return render_template('czat.html', username=username,room=room )
        
    else:
       
        return redirect(url_for('main'))

@socketio.on('wyslij_wiadomosc')
def han_wyslij_wiadomosc(data):
    app.logger.info("{} wyslał do pokoju  {} wiadomość : {}".format(data['username'],data['room'],data['message']))
    socketio.emit('otrzymaj_wiadomosc',data, room=data['room'])

@socketio.on('dol_pokoj')
def han_dol_pokoj_event(data):
    app.logger.info("{} dołączył do pokoju {}".format(data['username'],data['room']))
    join_room(data['room'])
    socketio.emit('Ogl_dol_room',data )


if __name__ == '__main__':
    socketio.run(app,debug=True)