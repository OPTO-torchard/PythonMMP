import O22SIOMM
from time import sleep
grvEpic = O22SIOMM.O22MMP('10.192.0.152')

print '0, 6 = ' + str(grvEpic.GetHDDigitalPointState(0,6))

print '0, 5 = ' + str(grvEpic.GetHDDigitalPointState(0, 5))

print '2, 0 = ' + str(grvEpic.GetAnalogPointValue(2, 0))

grvEpic.close()
