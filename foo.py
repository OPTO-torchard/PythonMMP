import O22SIOMM
import O22SIOUT
import sys

destinationOffset = '0xF0D83001'
size = 1
index = 0

grvEpic = O22SIOMM.O22MMP()
print '\nTerry`s groov EPIC @ OPTO' + str(grvEpic.MACAddressE0())[8:]
#print 'raw: ' + str(int('0'+grvEpic.ReadRawOffset(destinationOffset+1, 1, 'c')[2:-1],16))


#destinationOffset = O22SIOUT.BASE_SCRATCHPAD_STRING + (index * O22SIOUT.OFFSET_SCRATCHPAD_STRING)

#print grvEpic.UnpackReadResponse(grvEpic.ReadBlock(destinationOffset+0x01, 1), 'c')


char = grvEpic.ReadRawOffset(destinationOffset, 1, 'c')[1:-1]
print char
if len(char) == 1:
    char = ord(char)
else:
    char = int('0'+char[1:], 16)
print char


#if ((index * O22SIOUT.OFFSET_SCRATCHPAD_STRING) < O22SIOUT.MAX_BYTES_SCRATCHPAD_STRING):
#    size = grvEpic.ReadRawOffset(hex(destinationOffset), 2, 'NONE')#[2:-1])#,16)
#    print 'size = ' + str(size)
#    print grvEpic.UnpackReadResponse(grvEpic.ReadBlock(destinationOffset+2, size), 'NONE')
#else: print 'ScratchPad string index out of range.'





print 'output: ' + str(grvEpic.GetScratchPadStringArea(0))
print ''
grvEpic.close()
