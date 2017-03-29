import requests
import json

todourl="http://localhost:5000/todo/api/v1.0/add"

def todo_post(titlein=u'Title', descin=u'Desc'):
  # payload = {
	# "title":title,
	# "description":desc
  # }
  # payload = dict(title=titlein,
	# description=descin)

  payload = (('title',titlein),('description',descin))

  r=requests.post(todourl,files = payload)
  #create the dict corresponding to json received
  return r

r = todo_post("Buy Bananas","From Kroger")
