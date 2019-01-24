import optommp
import sys

grvEpic = optommp.O22MMP()

grvEpic.SetDigitalPointState(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

grvEpic.close()

