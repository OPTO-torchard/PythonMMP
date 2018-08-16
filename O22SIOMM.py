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
        baseAddress = O22SIOUT.BASE_HDDPOINT_WRITE_OFF if state == 0 else O22SIOUT.BASE_HDDPOINT_WRITE_ON
        point = 4 if channel < 32 else 0
        nResult = self.WriteBlock(baseAddress + point + (O22SIOUT.SIZE_HDDPOINT * module), (1 << (channel % 32)))
        return nResult

    def GetHDDigitalPointState(self, module, channel):
        point = 4 if channel < 32 else 0
        nResult = self.ReadBlock(O22SIOUT.BASE_HDDPOINT_READ + point + (O22SIOUT.SIZE_HDDPOINT * module))
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
        print block
        return bytearray(block)

    def BuildReadBlockRequest(self, dest):
        tcode = O22SIOUT.TCODE_READ_BLOCK_REQUEST
        block = [0, 0, (self.tlabel << 2), (tcode << 4), 0, 0, 255, 255, int(str(hex(dest))[2:4],16), int(str(hex(dest))[4:6],16), int(str(hex(dest))[6:8],16), int(str(hex(dest))[8:10],16), 0,4, 0,0]
        print block
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
