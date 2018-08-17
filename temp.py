import O22SIOMM

grvEpic = O22SIOMM.O22MMP()
print 'Terry, 0:5 = ' + str(grvEpic.GetHDDigitalPointState(0, 5))
grvEpic.close()

benEpic = O22SIOMM.O22MMP('10.192.0.152')
print 'Ben`s, 2:0 = ' + str(benEpic.GetAnalogPointValue(2, 0))
benEpic.close()


