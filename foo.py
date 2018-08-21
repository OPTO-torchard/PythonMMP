import O22SIOMM
import sys

from timeit import default_timer as timer
start = timer()

offset = '0xF0350000'
size = 17 
data_type = 'c'
value = float(sys.argv[1]) if(len(sys.argv) > 1) else 0

grvEpic = O22SIOMM.O22MMP()
print 'Terry,  initial = ' + str(grvEpic.GetAnalogPointValue(1,0))
print 'success if zero   ' + str(grvEpic.SetAnalogPointValue(1, 0, value))
print 'Terry,   after =  ' + str(grvEpic.GetAnalogPointValue(1,0))
print ''
print 'Terry, MAC addr: ' + str(grvEpic.MACAddress())
print 'Terry, IP addr.: ' + str(grvEpic.IPAddress())
print 'Terry, firmware: ' + str(grvEpic.FirmwareVersion())
print 'Terry, unit des: ' + str(grvEpic.UnitDescription())
print 'Terry,    error: ' + str(grvEpic.LastError())
print 'Terry, mod0 ch5= ' + str(grvEpic.GetAnalogPointValue(2, 0))
print 'Terry, min val = ' + str(grvEpic.GetAnalogPointMin(2, 0))
print 'Terry, max val = ' + str(grvEpic.GetAnalogPointMax(2, 0))
#print 'Raw read:\t' + str(grvEpic.ReadRawOffset(offset, size, data_type)) + '\n'
grvEpic.close()

benEpic = O22SIOMM.O22MMP('10.192.0.152')
print ''
print 'Ben, MAC addr. : ' + str(benEpic.MACAddress())
print 'Ben, IP address: ' + str(benEpic.IPAddress())
print 'Ben, firmware v: ' + str(benEpic.FirmwareVersion())
print 'Ben, unit descr: ' + str(benEpic.UnitDescription())
print 'Ben, last error: ' + str(benEpic.LastError())
print 'Ben, 2:0 val =   ' + str(benEpic.GetAnalogPointValue(2, 0))
print 'Ben, min val =   ' + str(benEpic.GetAnalogPointMin(2, 0))
print 'Ben, max val =   ' + str(benEpic.GetAnalogPointMax(2, 0))
#print 'Raw read:\t' + str(benEpic.ReadRawOffset(offset, size, data_type)) + '\n'
benEpic.close()

end = timer()
print 'time = ' + str(end-start)
