import time
import threading
from datetime import datetime, timedelta

class Scheduler:
    RUNNING = 0
    PAUSED = 1

    def __init__(self, every, exact=False):
        self.__every = every
        self.__exact = exact
        self.__thread = threading.Thread(target=self.__run)
        self.__task = None
        self.__status = self.PAUSED

    def setTask(self, task):
        self.__task = task

    def start(self):
        if self.__status == self.PAUSED:
            self.__status = self.RUNNING
            self.__thread.start()

    def stop(self):
        self.__status = self.PAUSED

    def __run(self):
        while self.__status == self.RUNNING:
            startTime = datetime.now()
            self.__task()
            endTime = datetime.now()
            elapsedTime = endTime-startTime
            suspendTime = timedelta(seconds=self.__every)-elapsedTime
            suspendTimeAsSecond = suspendTime.seconds + suspendTime.microseconds/1000000
            time.sleep(suspendTimeAsSecond)
            
        
