import requests, time, thread

# Define a function for the thread
def send_postrequest():
    global widthtag, heighttag, posxtag, posytag
    global width, height, posx, posy

    widthtag = 'width'
    heighttag = 'height'
    posxtag = 'posx'
    posytag = 'posy'
    width=0
    height=0
    posx = 0
    posy = 0

    while(1):
       face = {widthtag: width, heighttag: height ,posxtag: posx, posytag:posy}
       r = requests.post('http://requestb.in/1bbag281', params=face)
       print r.status_code
       print r.content

try:
   thread.start_new_thread( send_postrequest, () )
except:
   print "Error: unable to start thread"

while 1:
    width = 10
    height = 10
    posx = 10
    posy = 10
