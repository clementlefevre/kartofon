import os
import vlc
import time

from evdev import InputDevice, categorize, ecodes
from select import select

device = InputDevice('/dev/input/event1')
print(device)

keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

TITLES={}

def read_titles():
    f = open('/home/pi/kartofon/config.txt', 'r')
    TITLES = {}
    for line in f:
        line = line.replace('\n','')
        if len(line)>0:
            k, v = line.strip().split(' ')
            TITLES[k.strip()] = v.strip()

    f.close()
    return TITLES



instance = vlc.Instance()

#Create a MediaPlayer with the default instance
player = instance.media_player_new()

#Load the media file
def play_file(player, filename):
    filename = ''.join(['/home/pi/kartofon/media/',filename,'.mp3'])
    media = instance.media_new(filename)

#Add the media to the player
    player.set_media(media)

#Play for 10 seconds then exit
    print("start playing", filename)
    player.play()
    

def read_rfid(device):
	stri=''
	key = ''
	while key != 'KEY_ENTER':
	    r,w,x = select([device], [], [])
	    for event in device.read():
	        if event.type==1 and event.value==1:
	            stri+=keys[ event.code ]
	            key = ecodes.KEY[event.code]

	print ('ID found from reader : ', stri[:-1])
	return(stri[:-1])

TITLES = read_titles()


while True :
    RFID = read_rfid(device)
    if player:
        player.stop()
    if (RFID in TITLES.keys()):
        print(TITLES[RFID])
        play_file(player, TITLES[RFID])

