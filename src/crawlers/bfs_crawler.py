from collections import deque

import tweepy

from crawlers.abstract_crawler import AbstractUserCrawler
from settings.twitter import api


class BFSCrawler(AbstractUserCrawler):

    def crawl(self, initial_user, num_of_users):

        self.queue = deque()

        current_user = api.get_user(initial_user)
        self.queue.append(current_user)

        self.seen = {current_user.id: True}
        self.graph = {}

        while len(self.queue) > 0 and len(self.graph) < num_of_users:
            
            print "Has stored {} users so far".format(len(self.graph))

            current_user = self.queue.popleft()
            self.graph[current_user.screen_name] = []

            ids = []
            for page in tweepy.Cursor(api.friends_ids, id=current_user.id).pages():
                ids.extend(page)

            def chunks(l, n):
                for i in range(0, len(l), n):
                    yield l[i:i + n]

            for chunked_ids in chunks(ids, 100):
                for user in api.lookup_users(user_ids = chunked_ids):

                    if self.should_check(user):
                        self.graph[current_user.screen_name].append(user.screen_name)
                        self.queue.append(user)
                        self.seen[user.id] = True

            
    def should_check(self, twitter_user):

        if twitter_user.id in self.seen:
            return False

        if twitter_user.time_zone == 'Tehran':
            return True

        if twitter_user.lang == 'fa':
            return True

        if hasattr(twitter_user, 'status') and twitter_user.status.lang == 'fa':
            return True

        if twitter_user.default_profile_image:
            return False

        if twitter_user.favourites_count < 100:
            return False

        if twitter_user.followers_count < 200:
            return False

        if twitter_user.friends_count < 100:
            return False

        if twitter_user.statuses_count < 500:
            return False

        return False
       
    def dump(self, file_path):
        with open(file_path, 'w') as f:
            for user, friends in self.graph.items():
                for friend in friends:
                    f.write("{},{}\n".format(user, friend))
