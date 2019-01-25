import optommp
import sys

# Default to setting scratchpad int #0 to the value 22 if arguements are not provided:
index = int(sys.argv[1]) if(len(sys.argv) > 2) else 0
value = int(sys.argv[2]) if(len(sys.argv) > 2) else 22

#Create the controller object:
grvEpic = optommp.O22MMP()

# Read and print the current scratch pad value:
print 'old value: ' + str(grvEpic.GetScratchPadIntegerArea(index))
# Write the new value and print whether or not it succeeded:
print 'writing ' + str(value) + ' -> ' + str(grvEpic.SetScratchPadIntegerArea(index, value))

# Close the controller when you're finished:
grvEpic.close()
