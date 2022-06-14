
from flask import Flask, render_template,request, redirect, url_for
from flask_login import LoginManager
from flask_socketio import SocketIO, join_room 
login_manager = LoginManager()
app = Flask(__name__)
socketio = SocketIO(app)
@app.route('/')
def main():
    return render_template("index.html")

@app.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')
    if username and room:
        
        return render_template('czat.html', username=username,room=room)
        
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
