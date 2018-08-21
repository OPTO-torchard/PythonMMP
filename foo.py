import O22SIOMM
import sys

offset = '0xF0D83002'
size = 17 
data_type = 'c'

grvEpic = O22SIOMM.O22MMP()
print '\nTerry`s groov EPIC @ OPTO' + str(grvEpic.MACAddressE0())[8:]
print 'raw: ' + str(grvEpic.ReadRawOffset(offset, size, 'NONE'))
print 'str: ' + str(grvEpic.ReadRawOffset(offset, size, 's'))
print ' --> ' + str(grvEpic.ReadRawOffset(offset, size, data_type))
print ''
grvEpic.close()
