import threading
import time

def hello():
    time.sleep(5)
    print('Hello World')
print('this is the beginning')
threadObj = threading.Thread(target=hello)
threadObj.start()

print('This is the end')