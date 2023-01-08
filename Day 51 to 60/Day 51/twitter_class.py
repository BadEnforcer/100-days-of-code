import speedtest
import tweepy
from datetime import datetime

time = datetime.now()


class Twitter:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.ping = 0

    def get_speed(self):
        # speedtest
        # servers = []
        # If you want to test against a specific server
        # servers = [1234]

        threads = 4
        # If you want to use a single threaded test
        # threads = 1

        s = speedtest.Speedtest()
        # s.get_servers(servers)
        s.get_best_server()
        s.download(threads=threads)
        s.upload(pre_allocate=False, threads=threads)
        s.results.share()

        results_dict = s.results.dict()
        self.up = results_dict["upload"]
        self.down = results_dict["download"]
        # self.ping = results_dict['ping']
        # print(results_dict)
        self.post_on_twitter()

    def post_on_twitter(self):
        client = tweepy.Client(
            consumer_key="",
            consumer_secret="",
            access_token="",
            access_token_secret=""
        )

        tw = client.create_tweet(text=f"Upload Speed: {self.up}\nDownload Speed: {self.down}\nChecked on {time}\n")
        print(tw)
