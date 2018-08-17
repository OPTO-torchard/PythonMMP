import O22SIOUT
import sys
import struct
import socket

class O22MMP:
    def __init__(self, host=None):
        if(host is None): host = '127.0.0.1'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,2001))
        self.tlabel = 1

    def SetHDDigitalPointState(self, module, channel, state):
        destinationOffset = O22SIOUT.BASE_HDDPOINT_WRITE + (module * 0x1000) + (channel * O22SIOUT.SIZE_HDDPOINT)
        nResult = self.WriteBlock(destinationOffset, state)
        return nResult

    def GetHDDigitalPointState(self, module, channel):
        destinationOffset = O22SIOUT.BASE_HDDPOINT_READ + (module * 0x1000) + (channel * O22SIOUT.SIZE_HDDPOINT)
        nResult = self.ReadBlock(destinationOffset)
        return nResult

    def WriteBlock(self, address, value):
        block = self.BuildWriteBlockRequest(address, value)
        nSent = self.sock.send(block)
        self.tlabel += 1
        data = self.sock.recv(O22SIOUT.SIZE_WRITE_RESPONSE)
        status = self.UnpackWriteResponse(data)
        if (status == 0):
            print 'Write success, status: ' + str(status)
        else: print 'Write failure, status: ' + str(status)
        return status

    def ReadBlock(self, address):
        block = self.BuildReadBlockRequest(address)
        nSent = self.sock.send(block)
        self.tlabel += 1
        data = self.sock.recv(O22SIOUT.SIZE_READ_BLOCK_RESPONSE + 4)
        output = self.UnpackReadResponse(data)
        return output

    def BuildWriteBlockRequest(self, dest, value):
        tcode = O22SIOUT.TCODE_WRITE_BLOCK_REQUEST
        block = [0, 0, (self.tlabel << 2), (tcode << 4), 0, 0, 255, 255, int(str(hex(dest))[2:4],16), int(str(hex(dest))[4:6],16), int(str(hex(dest))[6:8],16), int(str(hex(dest))[8:10],16), 0,4, 0,0, 0,0,0,value]
        return bytearray(block)

    def BuildReadBlockRequest(self, dest):
        tcode = O22SIOUT.TCODE_READ_BLOCK_REQUEST
        block = [0, 0, (self.tlabel << 2), (tcode << 4), 0, 0, 255, 255, int(str(hex(dest))[2:4],16), int(str(hex(dest))[4:6],16), int(str(hex(dest))[6:8],16), int(str(hex(dest))[8:10],16), 0,4, 0,0]
        return bytearray(block)

    def UnpackWriteResponse(self, data):
        data_block = data[4:8]
        status = struct.unpack_from('>i', bytearray(data_block))
        return int(str(status)[1:-2])

    def UnpackReadResponse(self, data):
        data_block = data[16:20]
        print str(struct.unpack_from('>i', bytearray(data)))
        output = struct.unpack_from('>i', bytearray(data_block))
        return str(output)[1:-2]

    def close(self):
        self.sock.close()
