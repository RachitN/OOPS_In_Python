import threading

class RachitMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x= RachitMessenger(name='SEND')
y= RachitMessenger(name='Recieve')
x.start()
y.start()