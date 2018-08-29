import optommp
import sys

index = int(sys.argv[1]) if(len(sys.argv) > 2) else 0
value = float(sys.argv[2]) if(len(sys.argv) > 2) else 22.22
grvEpic = optommp.O22MMP()
print '\nTerry`s groov EPIC @ OPTO' + str(grvEpic.MACAddressE0())[8:]

print 'old value: ' + str(grvEpic.GetScratchPadFloatArea(index))
print 'writing ' + str(value) + ' -> ' + str(grvEpic.SetScratchPadFloatArea(index, value))

grvEpic.close()
