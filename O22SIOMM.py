import O22SIOUT
import sys
import array
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
    def UnitDescription(self):
        #return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_FIRMWARE_VERSION), 'c')
        destinationOffset = O22SIOUT.BASE_UNIT_DESCRIPTION
        data = self.ReadBlock(destinationOffset)
        return self.UnpackReadResponse(data, '$')

    def FirmwareVersion(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_FIRMWARE_VERSION), '$')
        #destinationOffset = O22SIOUT.BASE_UNIT_DESCRIPTION
        #data = self.ReadBlock(destinationOffset)
        #return self.UnpackReadResponse(data, '$')

    def MACAddress(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_MAC_ADDRESS), '$')
 

## HD DIGITAL POINTS
##
    def GetHDDigitalPointState(self, module, channel):
        destinationOffset = O22SIOUT.BASE_HDDPOINT_READ + (module * O22SIOUT.OFFSET_HDDPOINT_MOD) + (channel * O22SIOUT.OFFSET_HDDPOINT)
        data = self.ReadBlock(destinationOffset)
        return self.UnpackReadResponse(data, 'i')

    def SetHDDigitalPointState(self, module, channel, state):
        destinationOffset = O22SIOUT.BASE_HDDPOINT_WRITE + (module * O22SIOUT.OFFSET_HDDPOINT_MOD) + (channel * O22SIOUT.OFFSET_HDDPOINT)
        data = self.WriteBlock(destinationOffset, [0,0,0,state])
        return self.UnpackWriteResponse(data)


## ANALOG POINTS
##
    def GetAnalogPointValue(self, module, channel):
        destinationOffset = O22SIOUT.BASE_APOINT_READ + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel)
        data = self.ReadBlock(destinationOffset)
        return self.UnpackReadResponse(data, 'f')

    def SetAnalogPointValue(self, module, channel, value):
        destinationOffset = O22SIOUT.BASE_APOINT_WRITE + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel)
        hexvalue = hex(struct.unpack('L', struct.pack('<f', value))[0])
        hexval = []
        for i in range(4):
            hexval.append(int(str(hexvalue)[(2*i)+2:(2*i)+4], 16))
        print hexval
        data = self.WriteBlock(destinationOffset, hexval) 
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

    def BuildWriteBlockRequest(self, dest, data):
        tcode = O22SIOUT.TCODE_WRITE_BLOCK_REQUEST
        block = [0, 0, (self.tlabel << 2), (tcode << 4), 0, 0, 255, 255, int(str(hex(dest))[2:4],16), int(str(hex(dest))[4:6],16), int(str(hex(dest))[6:8],16), int(str(hex(dest))[8:10],16), 0,4, 0,0]
        block = block + data
        print block
        return bytearray(block)



## UNPACK BLOCK RESPONSE DATA
##
    def UnpackReadResponse(self, data, data_type):
        data_block = data[16:]
        output = ''
        #prin str(len(data))
        #print str(len(data_block))
        if(data_type == '$'):
            for i in range(len(data_block)):
                nextChar = str(struct.unpack_from('>c', bytearray(data_block[i])))[2:-2]
                #print nextChar
                output += nextChar
        else: output = struct.unpack_from(''+data_type, bytearray(data_block))
        #output = struct.unpack_from('>'+data_type, bytearray(data_block))
        return str(output)[1:-2]

    def UnpackWriteResponse(self, data):
        data_block = data[4:8]
        status = struct.unpack_from('>i', bytearray(data_block))
        return int(str(status)[1:-2])

## CLOSE SOCKET / END SESSION
##
    def close(self):
        self.sock.close()
