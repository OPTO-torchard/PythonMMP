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


## HD DIGITAL POINTS
##
    def GetHDDigitalPointState(self, module, channel):
        destinationOffset = O22SIOUT.BASE_HDDPOINT_READ + (module * O22SIOUT.OFFSET_HDDPOINT_MOD) + (channel * O22SIOUT.OFFSET_HDDPOINT)
        data = self.ReadBlock(destinationOffset)
        return self.UnpackReadResponse(data, 'i')

    def SetHDDigitalPointState(self, module, channel, state):
        destinationOffset = O22SIOUT.BASE_HDDPOINT_WRITE + (module * O22SIOUT.OFFSET_HDDPOINT_MOD) + (channel * O22SIOUT.OFFSET_HDDPOINT)
        data = self.WriteBlock(destinationOffset, state)
        return self.UnpackWriteResponse(data)


## ANALOG POINTS
##
    def GetAnalogPointValue(self, module, channel):
        destinationOffset = O22SIOUT.BASE_APOINT_READ + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel)
        data = self.ReadBlock(destinationOffset)
        return self.UnpackReadResponse(data, 'f')

    def SetAnalogPointValue(self, module, channel, value):
        destinationOffset = O22SIOUT.BASE_APOINT_READ + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel)
        data = self.WriteBlock(destinationOffset, value)
        return self.UnpackWriteResponse(data)


## MEMORY ACCESS FUNCTIONS
##
    def ReadBlock(self, address):
        block = self.BuildReadBlockRequest(address)
        nSent = self.sock.send(block)
        return self.sock.recv(O22SIOUT.SIZE_READ_BLOCK_RESPONSE + 12) 

    def WriteBlock(self, address, value):
        block = self.BuildWriteBlockRequest(address, value)
        nSent = self.sock.send(block)
        return self.sock.recv(O22SIOUT.SIZE_WRITE_RESPONSE)


## BLOCK REQUEST BYTE ARRAY CONSTRUCTORS
##
    def BuildReadBlockRequest(self, dest):
        tcode = O22SIOUT.TCODE_READ_BLOCK_REQUEST
        block = [0, 0, (self.tlabel << 2), (tcode << 4), 0, 0, 255, 255, int(str(hex(dest))[2:4],16), int(str(hex(dest))[4:6],16), int(str(hex(dest))[6:8],16), int(str(hex(dest))[8:10],16), 0,16, 0,0]
        return bytearray(block)

    def BuildWriteBlockRequest(self, dest, value):
        tcode = O22SIOUT.TCODE_WRITE_BLOCK_REQUEST
        block = [0, 0, (self.tlabel << 2), (tcode << 4), 0, 0, 255, 255, int(str(hex(dest))[2:4],16), int(str(hex(dest))[4:6],16), int(str(hex(dest))[6:8],16), int(str(hex(dest))[8:10],16), 0,4, 0,0, 0,0,0,value]
        return bytearray(block)



## UNPACK BLOCK RESPONSE DATA
##
    def UnpackReadResponse(self, data, data_type):
        data_block = data[16:]
        #print str(len(data))
        #print str(len(data_block))
        output = struct.unpack_from('>'+data_type, bytearray(data_block))
        return str(output)[1:-2]

    def UnpackWriteResponse(self, data):
        data_block = data[4:8]
        status = struct.unpack_from('>i', bytearray(data_block))
        return int(str(status)[1:-2])

## CLOSE SOCKET / END SESSION
##
    def close(self):
        self.sock.close()
