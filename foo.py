import O22SIOMM
import sys

grvEpic = O22SIOMM.O22MMP()
print 'devEPIC, 0:5 =   ' + str(grvEpic.GetHDDigitalPointState(0, 5))
print 'devEPIC, 2:0 =   ' + str(grvEpic.GetAnalogPointValue(2, 0))
print 'grvEPIC, 1:0 =   ' + str(grvEpic.GetAnalogPointValue(1,0))
print 'success if = 0 : ' + str(grvEpic.SetAnalogPointValue(1, 0, float(sys.argv[1])))
print 'devEPIC, 1:0 =   ' + str(grvEpic.GetAnalogPointValue(1,0))
print '\nTerry, MAC addr: ' + str(grvEpic.MACAddress())
print 'Terry, firmware: ' + str(grvEpic.FirmwareVersion())
print 'Terry, unit des: ' + str(grvEpic.UnitDescription())
print 'Terry, IP addr.: ' + str(grvEpic.IPAddress())
offset = '0xF0380154'
size = 12
data_type = '$'
print 'Raw read:\t' + str(grvEpic.ReadRawOffset(offset, size, data_type)) + '\n'
grvEpic.close()

benEpic = O22SIOMM.O22MMP('10.192.0.201')
print '\nBen, MAC addr. : ' + str(benEpic.MACAddress())
print 'Ben, firmware v: ' + str(benEpic.FirmwareVersion())
print 'Ben, unit descr: ' + str(benEpic.UnitDescription())
print 'Ben, IP address: ' + str(benEpic.IPAddress())

print 'Raw read:\t' + str(benEpic.ReadRawOffset(offset, size, data_type)) + '\n'
benEpic.close()
