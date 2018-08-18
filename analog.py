import O22SIOMM
import sys

value = float(sys.argv[1])

grvEpic = O22SIOMM.O22MMP()
grvEpic.SetAnalogPointValue(1, 0, value)
grvEpic.close()
