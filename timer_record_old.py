
# This is a basic program to create audio recordings on a schedule. 

# import functions to interact with the operating system. 
import subprocess
import os
import time
import matplotlib.pylab as plt
import numpy as np

# This is special, this is a script for the raspberry pi with a Cirrus Logic Wolfam audio card This sets up
# the card for recording. the interface is really broken. It required massive patching of system to run.
subprocess.call(['./Record_from_Headset.sh'])


# this next section uses the alsa audio system to record data. 
# arecord -- main alsa audio recording program
#         -d duration to record in seconds
#         -Dhw: the sound card that is going to be used. 'sndrpiwsp' is selected 
#         -r  is the sample rate
#         -c is the number of channels
#         -f is the format, (Signed 32bit Little Endian) 
#         followed by the filename
# filename format
# record_start(date_time)_duration_format.wav
# example: record_2015_Nov1
timestr = time.strftime("%Y_%m_%d-%H_%M_%S_d")
print timestr

debug = True

RATE = 44100
RATE = str(RATE)

CHANNELS = 2 
CHANNELS = str(CHANNELS)

FORMAT = 'S32_LE'
DURATION = 5
DURATION = str(DURATION) 

# control flow variables. 
total = 5
count = 0


#---------------------------------------------------------------------
# Main loop
#---------------------------------------------------------------------

while count < total:
	i = 0
	timestr = time.strftime("%Y_%m_%d-%H_%M_%S_d")
	os.system('arecord'  
				' -d' +DURATION+ 
				' -Dhw:sndrpiwsp ' +
				'-r '+ RATE +
				' -c ' + CHANNELS +
				' -f '+ FORMAT +
				'  '+ timestr + 
				'_' + DURATION + 'secs.wav')
	count += 1
	print count
	

print "finished"











