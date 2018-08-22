import O22SIOUT
import sys
import struct
import socket

class O22MMP:
    def __init__(self, host=None):
        if(host is None): host = '127.0.0.1'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,2001))
        self.tlabel = 0 # transaction label is unused.


## MISC MMP ACCESS FUNCTIONS
##
    def ReadRawOffset(self, offset, size, data_type):
        return self.UnpackReadResponse(self.ReadBlock(int(offset, 16), size), data_type)

    def LastError(self):
        return str(hex(int(self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_LAST_ERROR, 4), 'i')))).upper()[2:]

    def IPAddressE0(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_IP_ADDRESS_ETH0, 4), 'IP')
    def MACAddressE0(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_MAC_ADDRESS_ETH0, 6), 'MAC')

    def IPAddressE1(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_IP_ADDRESS_ETH1, 4), 'IP')
    def MACAddressE1(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_MAC_ADDRESS_ETH1, 6), 'MAC')

    def UnitDescription(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_UNIT_DESCRIPTION, 12), 'NONE')

    def FirmwareVersion(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_FIRMWARE_VERSION, 4), 'FIRMWARE')



## HD DIGITAL POINTS
##
    def GetHDDigitalPointState(self, module, channel):
        destinationOffset = O22SIOUT.BASE_HDDPOINT_READ + (module * O22SIOUT.OFFSET_HDDPOINT_MOD) + (channel * O22SIOUT.OFFSET_HDDPOINT)
        data = self.ReadBlock(destinationOffset, 4)
        return self.UnpackReadResponse(data, 'i')

    def SetHDDigitalPointState(self, module, channel, state):
        destinationOffset = O22SIOUT.BASE_HDDPOINT_WRITE + (module * O22SIOUT.OFFSET_HDDPOINT_MOD) + (channel * O22SIOUT.OFFSET_HDDPOINT)
        data = self.WriteBlock(destinationOffset, [0,0,0,state])
        return self.UnpackWriteResponse(data)


## ANALOG POINTS
##
    def GetAnalogPointMin(self, module, channel):
        destinationOffset = O22SIOUT.BASE_APOINT_READ + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel) + 8
        return self.UnpackReadResponse(self.ReadBlock(destinationOffset, 4), 'f')

    def GetAnalogPointMax(self, module, channel):
        destinationOffset = O22SIOUT.BASE_APOINT_READ + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel) + 12
        return self.UnpackReadResponse(self.ReadBlock(destinationOffset, 4), 'f')

    def GetAnalogPointValue(self, module, channel):
        destinationOffset = O22SIOUT.BASE_APOINT_READ + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel)
        return self.UnpackReadResponse(self.ReadBlock(destinationOffset, 4), 'f')

    def SetAnalogPointValue(self, module, channel, value):
        destinationOffset = O22SIOUT.BASE_APOINT_WRITE + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel)
        valueToWrite = hex(struct.unpack('L', struct.pack('<f', value))[0])
        hexvals = []
        if(value != 0):
            for i in range(4):
                hexvals.append(int(str(valueToWrite)[(2*i)+2:(2*i)+4], 16))
        else: hexvals = [0, 0, 0, 0]
        return self.UnpackWriteResponse(self.WriteBlock(destinationOffset, hexvals))

## SCRATCHPAD ACCESS FUNCTIONS
##
    def GetScratchPadStringArea(self, index):
        destinationOffset = O22SIOUT.BASE_SCRATCHPAD_STRING + (index * O22SIOUT.OFFSET_SCRATCHPAD_STRING)

                char = grvEpic.ReadRawOffset(destinationOffset, 1, 'c')[1:-1]
                print char
                char = ord(char) if len(char)==1 else int('0'+char[1:], 16)
        print char
        


        if (index * O22SIOUT.OFFSET_SCRATCHPAD_STRING) < O22SIOUT.MAX_BYTES_SCRATCHPAD_STRING:
    def GetAnalogPointMax(self, module, channel):
        destinationOffset = O22SIOUT.BASE_APOINT_READ + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel) + 12
        return self.UnpackReadResponse(self.ReadBlock(destinationOffset, 4), 'f')

    def GetAnalogPointValue(self, module, channel):
        destinationOffset = O22SIOUT.BASE_APOINT_READ + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel)
        return self.UnpackReadResponse(self.ReadBlock(destinationOffset, 4), 'f')

        status = struct.unpack_from('>i', bytearray(data_block))
        return int(str(status)[1:-2])


## CLOSE SOCKET / END SESSION
##
    def close(self):
        self.sock.close()

import O22SIOUT
import sys
import struct
import socket

class O22MMP:
    def __init__(self, host=None):
        if(host is None): host = '127.0.0.1'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,2001))
        self.tlabel = 0 # transaction label is unused.


## MISC MMP ACCESS FUNCTIONS
##
    def ReadRawOffset(self, offset, size, data_type):
        return self.UnpackReadResponse(self.ReadBlock(int(offset, 16), size), data_type)

    def LastError(self):
        return str(hex(int(self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_LAST_ERROR, 4), 'i')))).upper()[2:]

    def IPAddressE0(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_IP_ADDRESS_ETH0, 4), 'IP')
    def MACAddressE0(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_MAC_ADDRESS_ETH0, 6), 'MAC')

    def IPAddressE1(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_IP_ADDRESS_ETH1, 4), 'IP')
    def MACAddressE1(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_MAC_ADDRESS_ETH1, 6), 'MAC')

    def UnitDescription(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_UNIT_DESCRIPTION, 12), 'NONE')

    def FirmwareVersion(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_FIRMWARE_VERSION, 4), 'FIRMWARE')



## HD DIGITAL POINTS
##
    def GetHDDigitalPointState(self, module, channel):
        destinationOffset = O22SIOUT.BASE_HDDPOINT_READ + (module * O22SIOUT.OFFSET_HDDPOINT_MOD) + (channel * O22SIOUT.OFFSET_HDDPOINT)
        data = self.ReadBlock(destinationOffset, 4)
        return self.UnpackReadResponse(data, 'i')

    def SetHDDigitalPointState(self, module, channel, state):
        destinationOffset = O22SIOUT.BASE_HDDPOINT_WRITE + (module * O22SIOUT.OFFSET_HDDPOINT_MOD) + (channel * O22SIOUT.OFFSET_HDDPOINT)
        data = self.WriteBlock(destinationOffset, [0,0,0,state])
        return self.UnpackWriteResponse(data)


## ANALOG POINTS
##
    def GetAnalogPointMin(self, module, channel):
        destinationOffset = O22SIOUT.BASE_APOINT_READ + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel) + 8
        return self.UnpackReadResponse(self.ReadBlock(destinationOffset, 4), 'f')

        status = struct.unpack_from('>i', bytearray(data_block))
        return int(str(status)[1:-2])


## CLOSE SOCKET / END SESSION
##
    def close(self):
        self.sock.close()

