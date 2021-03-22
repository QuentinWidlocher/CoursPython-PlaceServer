from controller import Action, get_grid, place_pixel
from flask import Flask
from flask import request
from json import dumps as stringify
from json import loads as parse
from flask.helpers import make_response
from flask_socketio import SocketIO

from flask.wrappers import Response
flask = Flask(__name__)
socketio = SocketIO(flask)

@socketio.on('place')
def place(body):
    try:
        action = Action(parse(body))
        place_pixel(action)
        socketio.emit('place', action.as_dict())
        return ''
    except KeyError as e:
        return make_response(f"Il manque {e}", 400)
    except ValueError as e:
        return make_response(f"Une valeur est du mauvais type", 400)

@flask.route('/full')
def full():
    return get_grid()

if __name__ == '__main__':
    socketio.run(flask)
