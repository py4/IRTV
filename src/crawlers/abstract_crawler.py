import abc


class AbstractUserCrawler(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def crawl(self):
        """ Fetch connectivities data from Twitter. """
        return

    @abc.abstractmethod
    def dump(self):
        """ Dumps fetched data. """
        return
