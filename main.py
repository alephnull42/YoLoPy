 # main.py -- put your code here!
import time
seconds = 0
while(1):
	f=open("data.txt","w")
	f.write(str(seconds))
	f.close()
	time.sleep(60)
	seconds = seconds + 60
