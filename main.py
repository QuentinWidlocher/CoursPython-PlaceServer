from controller import Action, get_grid, place_pixel
from flask import Flask, request
from json import dumps as stringify
from flask.helpers import make_response

app = Flask(__name__)

@app.route('/place', methods=['POST'])
def place():
    try:
        action = Action(request.get_json())
        place_pixel(action)
        return ''
    except KeyError as e:
        return make_response(f"Il manque {e}", 400)
    except ValueError as e:
        return make_response(f"Une valeur est du mauvais type", 400)

@app.route('/full')
def full():
    return stringify(get_grid())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
