import requests
import json
import os

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()

data = []
for post in posts:
    aux_data = {
        'id': post['id'],
        'title': post['title'],
        'body': post['body']
    }
    data.append(aux_data)

json_data = json.dumps(data)
file = os.path.join('Descargas', 'publicasiones.json')
file = open(file, 'w')
file.write(json_data)

print("informasion guardada")
