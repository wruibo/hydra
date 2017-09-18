"""
    spider base class
"""
import time, threading


class Config:
    """
        configure of spider
    """
    def __init__(self):
        self.interval = 0


class Spider(threading.Thread):
    def __init__(self):
        # spider tasks
        self._tasks = []

        # stop command for spider
        self._bstop = True

        # stop status for spider
        self._stopped = True

        # configure for spider
        self._config = Config()

        # initialize thread
        threading.Thread.__init__(self)

    def start(self):
        """
            start the spider, use @stop methond to stop the spider after it's started
        :return:
        """
        # check if the spider has been started
        if not self._stopped:
            return

        # reset the stop flag to start spider thread
        self._bstop = False

        # start the spider thread
        threading.Thread.start(self)

    def prepare(self):
        """
            initialize the spider, relate with @destroy.
        subclass need realize this method
        :return:
        """
        pass

    def process(self, resp):
        """

        :param resp:
        :return:
        """
        pass

    def limit_interval(self, interval):
        """

        :param interval:
        :return:
        """
        self._config.interval = interval

    def feed(self, task):
        """
            feed a spider task
        :param task:
        :return:
        """
        self._tasks.append(task)

    def stop(self):
        """
            stop the spider, relate with the @start method
        :return:
        """
        # check if the spider has been stopped
        if self._stopped:
            return

        # set the stop flag to stop spider thread
        self._bstop = True

        # wait until the spider thread exit
        self.join()

    def run(self):
        """
            running the spider until all the urls has crawled
        :return:
        """
        # set the stopped flag first
        self._stopped = False

        # prepare for running spider task
        self.prepare()

        # process all urls waiting crawled
        while not self._bstop and len(self._tasks)>0:
            # get next task
            task = self._tasks.pop(0)

            # run the task
            resp = task.run()

            # process response
            self.process(resp)

            # wait interval for next task
            time.sleep(self._config.interval)

        self._stopped = True


class HttpSpider(Spider):
    def __init__(self):
        self._client = None

    def feed(self, url, *params, **kwargs):
        pass
