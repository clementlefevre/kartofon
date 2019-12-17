# Kartophon for Raspberry PI

Using KKmoon IC  14443A Card Reader USB 13.56MHZ RFID build a small mp3 player that play tunes when a rfid card is read.


### USB Sound card settings
- `sudo nano /etc/modprobe.d/alsa-base.conf`
- `defaults.ctl.card 1`
- `defaults.pcm.card 1`

- `sudo nano /boot/config.txt`
- `dtparam=audio=off` # disable the internal PCM Audio Jack output


### RFID USB Card reader 
- check the output of our folder content `/dev/input/by-id` and note the complete name of your RFID USB device
- in `devtest.py` , replace the `device = InputDevice('/dev/input/by-id/usb-13ba_Barcode_Reader-event-kbd')` with the value found before


### Start Kartofon on Boot :
- make the `kartofon.sh` script executable, from the project folder : `chmod +x kartofon.sh`

- then add this script in the cron jobs : `crontab -e`
- add the following line (adjust the path according to your project location) : `@reboot cd /home/pi/workspace/kartofon && /home/pi/workspace/kartofon/kartofon.sh`

