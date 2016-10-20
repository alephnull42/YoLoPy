# YoLoPy
A LoPy device being polled by a Raspberry Pi, which in turn tweets the Lopy's Uptime every 8 hours

# Architecure
## Device: LoPy https://www.pycom.io/solutions/py-boards/lopy/
- Running on a noname PowerBank, nominal rating 2200 mAh
- Connected to home wifi router via changed "boot.py"
- Runs a simple script in "main.py" that increments a counter every 60 seconds and writes current value to local file "data.txt"

## Device: Raspberry Pi
- Kludge of Cron Jobs & Python scripts to: 
- FTP-pull latest "data.txt" from LoPy
- Compare to previous version and check if there was a change
- Crontab every 8 hours to run a Twitterbot to Tweet the latest If there was a change http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/

# Installation
## Device: LoPy 
- Recommended to have serial UART working in case the WLAN connect in "boot.py" fails and leaves you without IP access.
(with serial UART shell you can then just Factory reset the filesystem https://docs.pycom.io/lopy/lopy/tutorial/reset.html#factory-reset-the-filesystem - without you will have to fiddle with the firware reset pins)
- FTP transfer "boot.py" to /flash folder (overwrite) = WLAN connect - I had to use filezilla and force passive/PASV mode
- ONCE the WLAN to your home router works - FTP transfer "main.py" to /flash folder (overwrite) = loop to write the file every 60 seconds
- Reboot

## Device: Raspberry Pi
- Test with "wget -t 1 --user=micro --password='python' ftp://192.168.2.140/flash/data.txt" TODO: use  curl instead
- http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/
- Upload Python script TODO
- Add Cron Job in CRONTAB TODO

# Why?
- First experiment with LoPy
- See how long it lasts - assumption is that devices will get smaller, so a coin sized assembly in a few years should have uptimes in the same order of magnitude
- DISCLAIMER: This project completely ignores the LoRa technology, could be done with any other 'duino or similar

# References
- The LoPy is a Wifi and LoRa enabled programmable device https://www.pycom.io/solutions/py-boards/lopy/
- If you don't know what a Raspberry Pi is, you probably shouldn't be reading this.
- http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/
