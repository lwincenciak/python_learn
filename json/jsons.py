import json

with open('users.json') as f:
    d = json.load(f)

for record in d:
    print('Street: ' + record['address']['street'])
    print('Geo_lat: ' + record['address']['geo']['lat'])
    print('Geo_lng: ' + record['address']['geo']['lng'])

with open('distros.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    print(distro['Name'])
