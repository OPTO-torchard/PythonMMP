import optommp
import sys

# Default to setting scratchpad float #0 to 22.22 if arguements are not provided:
index = int(sys.argv[1]) if(len(sys.argv) > 2) else 0
value = float(sys.argv[2]) if(len(sys.argv) > 2) else 22.22

# Create the controller object:
grvEpic = optommp.O22MMP()

# Read and print th ecurrent scratch pad value:
print 'old value: ' + str(grvEpic.GetScratchPadFloatArea(index))
# Write the new value and print if there were any errors:
print 'writing ' + str(value) + ' -> ' + str(grvEpic.SetScratchPadFloatArea(index, value))

# Close the controller when you're finished:
grvEpic.close()
