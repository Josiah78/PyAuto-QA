import time

print(time.time())

def calculate():
    for i in range(0,10000):
        pass

def timeFunc():
    startTime = time.time()
    calculate()
    endTime = time.time()
    print(endTime-startTime)

timeFunc()

print('Tick')
time.sleep(1)
print('Tock')
time.sleep(1)
print('Tick')
time.sleep(1)
print('Tock')
time.sleep(1)