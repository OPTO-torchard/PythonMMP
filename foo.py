import O22SIOMM
import sys

from timeit import default_timer as timer
start = timer()

offset = '0xF0350000'
size = 17 
data_type = 'c'
value = float(sys.argv[1]) if(len(sys.argv) > 1) else 0

grvEpic = O22SIOMM.O22MMP()
print '\nTerry`s groov EPIC:'
print 'writing ' + str(value) + ' to analog at mod1 ch0 . . .'
print 'initial value  = ' + str(grvEpic.GetAnalogPointValue(1,0))
print 'write success -> ' + str(grvEpic.SetAnalogPointValue(1, 0, value))
print 'updated value  = ' + str(grvEpic.GetAnalogPointValue(1,0))
print 'ETH 0 MAC addr.: ' + str(grvEpic.MACAddressE0())
print 'ETH 0 IP addr. : ' + str(grvEpic.IPAddressE0())
print 'ETH 1 MAC addr.: ' + str(grvEpic.MACAddressE1())
print 'ETH 1 IP addr. : ' + str(grvEpic.IPAddressE1())
print 'FirmwareVersion: ' + str(grvEpic.FirmwareVersion())
print 'UnitDescription: ' + str(grvEpic.UnitDescription())
print 'LastError      : ' + str(grvEpic.LastError())
print 'digPt  mod0 ch5= ' + str(grvEpic.GetHDDigitalPointState(0, 5))
print 'analog mod2 ch0= ' + str(grvEpic.GetAnalogPointValue(2, 0))
print 'analog min val = ' + str(grvEpic.GetAnalogPointMin(2, 0))
print 'analog max val = ' + str(grvEpic.GetAnalogPointMax(2, 0))
#print 'Raw read result: ' + str(grvEpic.ReadRawOffset(offset, size, data_type)) + '\n'
grvEpic.close()

benEpic = O22SIOMM.O22MMP('10.192.0.152')
print '\nBen`s groov EPIC:'
print 'ETH 0 MAC addr.: ' + str(benEpic.MACAddressE0())
print 'ETH 0 IP addr. : ' + str(benEpic.IPAddressE0())
print 'ETH 1 MAC addr.: ' + str(benEpic.MACAddressE1())
print 'ETH 1 IP addr. : ' + str(benEpic.IPAddressE1())
print 'FirmwareVersion: ' + str(benEpic.FirmwareVersion())
print 'UnitDescription: ' + str(benEpic.UnitDescription())
print 'LastError      : ' + str(benEpic.LastError())
print 'digPt  mod0 ch5= ' + str(benEpic.GetHDDigitalPointState(0, 5))
print 'analog mod2 ch0= ' + str(benEpic.GetAnalogPointValue(2, 0))
print 'analog min val = ' + str(benEpic.GetAnalogPointMin(2, 0))
print 'analog max val = ' + str(benEpic.GetAnalogPointMax(2, 0))
#print 'Raw read result: ' + str(benEpic.ReadRawOffset(offset, size, data_type)) + '\n'
benEpic.close()

end = timer()
print '\ntime elapsed = ' + str(end-start) + 's\n'
