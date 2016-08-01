import requests, time
face = {'width': 80, 'height': 80 ,'posx': 10, 'posy':50}
r = requests.post('http://requestb.in/1bbag281', params=face)
print r.status_code
print r.content
