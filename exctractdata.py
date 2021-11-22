import json

with open('artworks.txt') as json_file:
    data = json.load(json_file)
    for p in data['creators']:
        print('role: ' + p['id'])
        print('role: ' + p['id'])
        print('role: ' + p['id'])
        print('')