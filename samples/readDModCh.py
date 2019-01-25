import optommp
import sys

if(len(sys.argv) != 4): # If the module and/or channel are not provided.
        print 'Please provide module # and channel #'
        print 'Exiting script . . .'
        exit() # Inform the user and exit the script.

# Create the controller object:
grvEpic = optommp.O22MMP()

# Read the digital point state:
result = grvEpic.GetDigitalPointState(int(sys.argv[1]), int(sys.argv[2]))
# Print the value to the console:
print result

#Close the controller when you're finished:
grvEpic.close()
