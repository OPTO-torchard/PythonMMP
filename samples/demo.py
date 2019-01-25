import sys
import optommp

from timeit import default_timer as timer
start = timer()

# Get some misc. values to write:
integer = 22
value = float(sys.argv[1]) if(len(sys.argv) == 2) else 0
index = int(sys.argv[1]) if (len(sys.argv) == 3) else 0
data = sys.argv[2] if (len(sys.argv) ==3) else 'NULL'

grvEpic = optommp.O22MMP()
print 'Writing ' + str(value) + ' to analog at mod1 ch0'
print 'Initial value  = ' + str(grvEpic.GetAnalogPointValue(1,0))
print 'Write success -> ' + str(grvEpic.SetAnalogPointValue(1, 0, value))
print 'Updated value  = ' + str(grvEpic.GetAnalogPointValue(1,0))
print ''
print 'ScratchPad string old value:\t' + grvEpic.GetScratchPadStringArea(index)
print 'Writing "' + data + '" to ScratchPad string area #' + str(index) + ' ->' + str(grvEpic.SetScratchPadStringArea(index, data))
print 'ScratchPad string new value:\t' + grvEpic.GetScratchPadStringArea(index)
print ''
print 'ScratchPad integer at index 0:\t' + str(grvEpic.GetScratchPadIntegerArea(0))
print 'Writing `' + str(integer) + '` to ScratchPad integer #0 ->' + str(grvEpic.SetScratchPadIntegerArea(0, integer))
print 'ScratchPad integer at index 0:\t' + str(grvEpic.GetScratchPadIntegerArea(0)) + '\n'

print 'ETH 0 MAC addr.: ' + str(grvEpic.MACAddressE0())
print 'ETH 0 IP addr. : ' + str(grvEpic.IPAddressE0())
print 'ETH 1 MAC addr.: ' + str(grvEpic.MACAddressE1())
print 'ETH 1 IP addr. : ' + str(grvEpic.IPAddressE1())
print 'FirmwareVersion: ' + str(grvEpic.FirmwareVersion())
print 'UnitDescription: ' + str(grvEpic.UnitDescription())
print 'LastError      : ' + str(grvEpic.LastError())
print 'digPt  mod0 ch5= ' + str(grvEpic.GetDigitalPointState(0, 5))
print 'analog mod2 ch0= ' + str(grvEpic.GetAnalogPointValue(2, 0))
print 'analog min val = ' + str(grvEpic.GetAnalogPointMin(2, 0))
print 'analog max val = ' + str(grvEpic.GetAnalogPointMax(2, 0))
#print 'Raw read result: ' + str(grvEpic.ReadRawOffset(offset, size, data_type)) + '\n'
grvEpic.close()

end = timer()
print '\ntime elapsed = ' + str(end-start) + 's\n'
