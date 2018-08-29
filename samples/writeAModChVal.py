import optommp
import sys

channel = int(sys.argv[1])
module = int(sys.argv[2])
value = float(sys.argv[3])

grvEpic = optommp.O22MMP()
print 'old value: ' + str(grvEpic.GetAnalogPointValue(module, channel)
print 'writing' + str(value) + ' -> ' + str(grvEpic.SetAnalogPointValue(module, channel, value))
grvEpic.close()
