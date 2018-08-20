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

    def IPAddress(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_IP_ADDRESS, 4), 'IP')

    def UnitDescription(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_UNIT_DESCRIPTION, 12), 'none')

    def FirmwareVersion(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_FIRMWARE_VERSION, 4), '$')

    def MACAddress(self):
        return self.UnpackReadResponse(self.ReadBlock(O22SIOUT.BASE_MAC_ADDRESS, 6), 'MAC')
 

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
    def GetAnalogPointValue(self, module, channel):
        destinationOffset = O22SIOUT.BASE_APOINT_READ + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel)
        data = self.ReadBlock(destinationOffset, 4)
        return self.UnpackReadResponse(data, 'f')

    def SetAnalogPointValue(self, module, channel, value):
        destinationOffset = O22SIOUT.BASE_APOINT_WRITE + (O22SIOUT.OFFSET_APOINT_MOD * module) + (O22SIOUT.OFFSET_APOINT * channel)
        valueToWrite = hex(struct.unpack('L', struct.pack('<f', value))[0])
        hexvals = []
        if(value != 0):
            for i in range(4):
                hexvals.append(int(str(valueToWrite)[(2*i)+2:(2*i)+4], 16))
        else: hexvals = [0, 0, 0, 0]
        data = self.WriteBlock(destinationOffset, hexvals)
        return self.UnpackWriteResponse(data)


## MEMORY ACCESS FUNCTIONS
##
    def ReadBlock(self, address, size):
        block = self.BuildReadBlockRequest(address, size)
        nSent = self.sock.send(block)
        return self.sock.recv(O22SIOUT.SIZE_READ_BLOCK_RESPONSE + size)

    def WriteBlock(self, address, value):
        block = self.BuildWriteBlockRequest(address, value)
        nSent = self.sock.send(block)
        return self.sock.recv(O22SIOUT.SIZE_WRITE_RESPONSE)


## BLOCK REQUEST BYTE ARRAY CONSTRUCTORS
##
    def BuildReadBlockRequest(self, dest, size):
        tcode = O22SIOUT.TCODE_READ_BLOCK_REQUEST
        block = [0, 0, (self.tlabel << 2), (tcode << 4), 0, 0, 255, 255, int(str(hex(dest))[2:4],16), int(str(hex(dest))[4:6],16), int(str(hex(dest))[6:8],16), int(str(hex(dest))[8:10],16), 0,size, 0,0]
        return bytearray(block)

    def BuildWriteBlockRequest(self, dest, data):
        tcode = O22SIOUT.TCODE_WRITE_BLOCK_REQUEST
        block = [0, 0, (self.tlabel << 2), (tcode << 4), 0, 0, 255, 255, int(str(hex(dest))[2:4],16), int(str(hex(dest))[4:6],16), int(str(hex(dest))[6:8],16), int(str(hex(dest))[8:10],16), 0,4, 0,0]
        block = block + data
        return bytearray(block)


## UNPACK BLOCK RESPONSE DATA
##
    def UnpackReadResponse(self, data, data_type):
        data_block = data[16:]
        output = ''

        if data_type == '$': # experimental data unpack / format loop
            for i in range(len(data_block)):
                nextChar = str(struct.unpack_from('>c', bytearray(data_block[i])))#[1:-2]
#                print nextChar
                output += nextChar

        elif data_type == 'IP': # unpack data and format as an IP address
            for i in range(len(data_block)): # trim first 3 and last 3 around <data>: ('/<data>',)
                nextChar = str(struct.unpack_from('>c', bytearray(data_block[i])))[3:-3]
                if(nextChar == 'n'): nextChar = 10 # catch 10 = 0x0A = \n (line feed)
                else: nextChar = int('0'+nextChar, 16) # convert hex to decimal
                output += str(nextChar) + '.'
            output = output[:-1] # trim trailing .

        elif data_type == 'MAC': # unpack data formatted as a MAC address
            for i in range(len(data_block)): # trim first 2 last 3 around <data>: ('<data>',)
                nextChar = str(struct.unpack_from('>c', bytearray(data_block[i])))[2:-3]
                if(len(nextChar) == 1): nextChar = hex(ord(nextChar)) # force valid ascii back into hex
                output += nextChar[2:] + '-' # trim 0x, and dash
            output = output[:-1].upper() # trim out trailing dash, force upper case
        
        elif data_type == 'none': # unpack data that has no formatting
            output = data_block
        else: # unpack data of a specific given data_type (c, i, f, l, q, etc...)
            output = str(struct.unpack_from('>'+data_type, bytearray(data_block)))[1:-2]
        return output

    def UnpackWriteResponse(self, data):
        data_block = data[4:8]
        status = struct.unpack_from('>i', bytearray(data_block))
        return int(str(status)[1:-2])


## CLOSE SOCKET / END SESSION
##
    def close(self):
        self.sock.close()
