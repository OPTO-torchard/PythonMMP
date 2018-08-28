from timeit import default_timer as timer
import O22SIOMM
grvEpic = O22SIOMM.O22MMP()
start = timer()

for i in range(101):
    grvEpic.SetDigitalPointState(0, 5, (i%2))
grvEpic.close()

end = timer()
print(end-start)
