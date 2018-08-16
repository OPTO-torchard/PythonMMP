import O22SIOMM
import sys

grvEpic = O22SIOMM.O22MMP(sys.argv[1])

grvEpic.SetHDDigitalPointState(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

grvEpic.close()
