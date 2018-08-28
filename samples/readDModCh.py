import O22SIOMM
import sys

grvEpic = O22SIOMM.O22MMP()

result = grvEpic.GetHDDigitalPointState(int(sys.argv[1]), int(sys.argv[2]))
print result

grvEpic.close()

