from flask import Flask, escape, request, render_template, jsonify
import random
import json
from flask_socketio import SocketIO, send, emit



app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/', methods=['GET', 'POST'])
def get_tasks():
    if request.method == 'POST':
        data = json.loads(request.data)
        print(data)
        return jsonify({'tasks': data})
    else:
        return jsonify({'tasks': tasks})

    
if __name__ == '__main__':
    app.run(debug=True)

