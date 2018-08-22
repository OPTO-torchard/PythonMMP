import O22SIOMM
import O22SIOUT
import sys

destinationOffset = '0xF0D83001'
size = 1
index = 0

grvEpic = O22SIOMM.O22MMP()
print '\nTerry`s groov EPIC @ OPTO' + str(grvEpic.MACAddressE0())[8:]

print 'result = ' + str(grvEpic.GetScratchPadIntegerArea(int(sys.argv[1])))
print 'writing ' + str(sys.argv[2]) + ' ... ' + str(grvEpic.SetScratchPadIntegerArea(int(sys.argv[1]), int(sys.argv[2])))

grvEpic.close()
