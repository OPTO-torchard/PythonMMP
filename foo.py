import O22SIOMM

grvEpic = O22SIOMM.O22MMP()
print 'Terry, 0:5 = ' + str(grvEpic.GetHDDigitalPointState(0, 5))
print str(grvEpic.SetAnalogPointValue(1, 0, 1.11)
#print 'Terry, MAC addr: ' + str(grvEpic.MACAddress())
#print 'Terry, firmware: ' + str(grvEpic.FirmwareVersion())
#print 'Terry, unit des: ' + str(grvEpic.UnitDescription())
grvEpic.close()

benEpic = O22SIOMM.O22MMP('10.192.0.152')
print 'Ben`s, 2:0 = ' + str(benEpic.GetAnalogPointValue(2, 0))
benEpic.close()


