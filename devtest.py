import os
import vlc
import time

from evdev import InputDevice, categorize, ecodes
from select import select

#device = InputDevice('/dev/input/event1')
device = InputDevice('/dev/input/by-id/usb-13ba_Barcode_Reader-event-kbd')

print(device)

keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

TITLES={}

def read_titles():
    f = open('/home/pi/workspace/kartofon/config.txt', 'r')
    TITLES = {}
    for line in f:
        line = line.replace('\n','')
        if len(line)>0:
            k, v = line.strip().split(' ')
            #if k.strip() not in TITLES :
            TITLES[k.strip()] = v.strip()
            #else :
                #TITLES[k.strip()].append(v.strip())

    f.close()
    return TITLES



instance = vlc.Instance()

#Create a MediaPlayer with the default instance
player = instance.media_player_new()

#Load the media file
def play_file(player, filename):
    filename = ''.join(['/home/pi/workspace/kartofon/media/',filename,'.mp3'])
    media = instance.media_new(filename)
    print(f'file to play {filename}')
#Add the media to the player
    player.set_media(media)


    print("start playing", filename)
    player.play()
    #time.sleep(1.5)
    #duration = player.get_length() / 1000
    #time.sleep(duration) 

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
print(f'Titles : {TITLES}')

while True :
    RFID = read_rfid(device)
    if player:
        player.stop()
    if (RFID in TITLES.keys()):
        print(TITLES[RFID])
        #for file in TITLES[RFID]:
        play_file(player, TITLES[RFID])

