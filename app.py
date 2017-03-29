#!flask/bin/python
# source: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask 

from flask import Flask,jsonify,request

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

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/add', methods=['GET','POST'])
def create_task():
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.values.get('title'),
        'description': request.values.get('description'),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)
