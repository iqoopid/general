# SuperFastPython.com
# example of returning multiple value from a thread
from time import sleep
from threading import Thread
 
# custom thread
class CustomThread(Thread):
    # constructor
    def __init__(self, good):
        # execute the base constructor
        Thread.__init__(self)
        # set a default values
        self.value1 = None
        self.value2 = good
        self.value3 = None
 
    # function executed in a new thread
    def run(self):
        # block for a moment
        sleep(1)
        # store data in an instance variable
        self.value1 = 'Hello from a new thread'
        # self.value2 = 99
        self.value3 = False

# create a new thread
thread = CustomThread(98)
# start the thread
thread.start()
# wait for the thread to finish
thread.join()
# report all values returned from a thread
print(thread.value1)
print(thread.value2)
print(thread.value3)