import optommp
import sys

grvEpic = optommp.O22MMP()

result = grvEpic.GetDigitalPointState(int(sys.argv[1]), int(sys.argv[2]))
print result

grvEpic.close()

