import O22SIOMM
import sys

index = int(sys.argv[1]) if(len(sys.argv) > 2) else 0
value = int(sys.argv[2]) if(len(sys.argv) > 2) else 22

grvEpic = O22SIOMM.O22MMP()
print 'old value: ' + str(grvEpic.GetScratchPadIntegerArea(index))
print 'writing ' + str(value) + ' -> ' + str(grvEpic.SetScratchPadIntegerArea(index, value))
grvEpic.close()
