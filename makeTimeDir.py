import os
import time

# This functions generates folders and sub folders 
# Options 
# Starting in the current working directory
# generate a timebased filename. 
# Actually working method would be for x min at a tim
# but for this test it will be for every few seconds. 


def makemydir(filepath, timestamp=None, prepend = None):
	# check input variables and set them

	if timestamp is not None:
   		timestr = time.strftime("%Y_%m_%d-%H_%M")
   	else: 
        	timestr = ""

	if prepend is None:
        	prepend = ""
	
	filepath = os.path.expanduser(filepath+ prepend + timestr )

  	try:
    		if not os.path.isdir(filepath):
        		os.makedirs(filepath)
			print ('Generated filepath : ' + filepath)

 	except OSError:
   		print "Error Creating directory"
    	pass
  	return(filepath)


if __name__ == '__main__':

    filepath = '~/output/'
    timestamp =True
    prepend ="myvar_"
    

    makemydir(filepath, timestamp, prepend)


