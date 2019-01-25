import optommp
import sys

if(len(sys.argv) != 4): # If the module, channel, and/or value are not provided.
        print 'Please provide module #, channel #, and value [1|0].'
        print 'Exiting script . . .'
        exit() # Inform the user and exit the script.

# Save the provided arguements:
module = int(sys.argv[1])
channel = int(sys.argv[2])
value = float(sys.argv[3])

# Create the controller object:
grvEpic = optommp.O22MMP()

# Read and print current analog point value:
print 'old value: ' + str(grvEpic.GetAnalogPointValue(module, channel)
# Write the new value and print if there were any errors:
print 'writing' + str(value) + ' -> ' + str(grvEpic.SetAnalogPointValue(module, channel, value))

# Close the controller when you're finished:
grvEpic.close()
