from settings.twitter import api
from crawlers.bfs_crawler import BFSCrawler

if __name__ == '__main__':
    crawler = BFSCrawler()
    crawler.crawl("ibtkm", 5000)
    crawler.dump("/root/run/graph.csv")
