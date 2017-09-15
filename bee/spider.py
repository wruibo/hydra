"""
    spider base class
"""
import threading
from . import job


class _SpiderThread(threading.Thread):
    def __init__(self):
        # spider tasks
        self._tasks = []

        # stop command for spider
        self._stop = True

        # stop status for spider
        self._stopped = True

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
        self._stop = False

        # start the spider thread
        threading.Thread.start(self)

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
        self._stop = True

        # wait until the spider thread exit
        self.join()

    def run(self):
        """
            running the spider until all the urls has crawled
        :return:
        """
        # set the stopped flag first
        self._stopped = False

        # process all urls waiting crawled
        while not self._stop and len(self._tasks)>0:
            # get next task
            task = self._tasks.pop(0)

            # run the task
            resp = task.run()

            # process response
            self.process(resp)

        self._stopped = True


class Spider(_SpiderThread):
    """
        base class for spider
    """
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
