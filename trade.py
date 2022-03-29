from util import Scheduler

class Trade:
    def __init__(self):
        self.__scheduler = Scheduler(every=5, exact=False)
        self.__scheduler.setTask(self.__trade)

    def __trade(self):
        print ('Get market info')
        print ('trade something')
        print ('waiting..')

    def run(self):
        print ('Trade is started')
        self.__scheduler.start()

if __name__=='__main__':
    trade = Trade()
    trade.run()
