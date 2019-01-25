import optommp
import sys

if(len(sys.argv) != 4): # If the module, channel, and/or value are not provided.
        print 'Please provide module #, channel #, and value [1|0].'
        print 'Exiting script . . .'
        exit() # Inform the user and exit the script.

# Create the controller object:
grvEpic = optommp.O22MMP()

# Use the provided arguements to toggle the digital point:
grvEpic.SetDigitalPointState(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

# Close the controller when you're finished:
grvEpic.close()
