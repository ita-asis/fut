from .core import Core, cookies_file
import random
from time import time, sleep

class Delayed(Core):
    def __init__(self, email, passwd, secret_answer, platform='pc', code=None, emulate=None, debug=False, cookies=cookies_file):
        # Set initial delay
        self.delayInterval = 1.3
        self.delay = time()
        super(Delayed, self).__init__(email, passwd, secret_answer, platform, code, emulate, debug, cookies)

    def setRequestDelay(self, delay):
        self.delayInterval = delay

    def __request__(self, method, url, *args, **kwargs):
        """Prepares headers and sends request. Returns response as a json object."""
        # Rate Limit requests based on delay interval
        print('sending request...')
        if self.delay > time():
            sleep(self.delay - time())
        self.delay = time() + (self.delayInterval * random.uniform(0.75, 2))
        return super(Delayed, self).__request__(method, url, *args, **kwargs)

    def bid(self, trade_id, bid):
        # no delay between getting trade info and bidding
        delayInterval = self.delayInterval
        self.delayInterval = 0
        result = super(Delayed, self).bid(trade_id, bid)
        self.delayInterval = delayInterval
        return result