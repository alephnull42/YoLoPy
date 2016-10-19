# YoLoPy
A LoPy device being polled by a Raspberry Pi, which in turn tweets the Lopy's Uptime every 8 hours

# Architecure
[Device]: LoPy 
- Running on a noname PowerBank, nominal rating 2200 mAh
- Connected to home wifi router via changed "boot.py"
- Runs a simple script in "main.py" that increments a counter every 60 seconds and writes current value to local file "data.txt"
[Device]: Raspberry Pi
Kludge of Cron Jobs & Python scripts to 
- FTP-pull latest "data.txt" from LoPy
- Compare to previous version and check if there was a change
- Crontab every 8 hours to run a Twitterbot to Tweet the latest If there was a change

# Why?
- First experiment with LoPy
- See how long it lasts - assumption is that devices will get smaller, so a coin sized assembly in a few years should have uptimes in the same order of magnitude
- DISCLAIMER: This project completely ignores the LoRa technology, could be done with any other *duino or similar


# References
The LoPy is a Wifi and LoRa enabled programmable device https://www.pycom.io/solutions/py-boards/lopy/
If you don't know what a Raspberry Pi is, you probably shouldn't be reading this.

