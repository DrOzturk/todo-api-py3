# todo-api-py3

Restful API for a sample todo app using Flask in Python 3.
run this
`python app.py`

Send POST request in postman:   
http://localhost:5000/todo/api/v1.0/add   
setting these in Body/x-www-form-urlencoded   
title   Buy Bananas   
description   Buy them from Kroger    

it should return you JSON with status "201 Created":   
```JSON
{
  "task": {
    "description": "Buy them from Kroger ",
    "done": false,
    "id": 8,
    "title": "Buy Bananas"
  }
}
```

Access this one in browser, or do a GET request in Postman:
http://localhost:5000/todo/api/v1.0/tasks
It should give you:
```JSON
{
  "tasks": [
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done": false,
      "id": 1,
      "title": "Buy groceries"
    },
    {
      "description": "Need to find a good Python tutorial on the web",
      "done": false,
      "id": 2,
      "title": "Learn Python"
    },
    {
      "description": "Buy them from Kroger ",
      "done": false,
      "id": 3,
      "title": "Buy Bananas"
    }
  ]
}
```
