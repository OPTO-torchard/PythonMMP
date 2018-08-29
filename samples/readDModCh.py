import optommp
import sys

grvEpic = optommp.O22MMP()

result = grvEpic.GetHDDigitalPointState(int(sys.argv[1]), int(sys.argv[2]))
print result

grvEpic.close()

