from config.config import Conf
class ApiReq():
    def __init__(self):
        self.conf = Conf()
        self.channel_uri = None
        self.search_uri = None
        self.video_uri = None

    def set_channel_uri(self):
        print self.conf.USER_NAME, self.conf.APP_KEY
        self.channel_uri = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=%s&fields=items&key=%s' % (self.conf.USER_NAME, self.conf.APP_KEY)

    def set_search_uri(self, channel_id, pageToken=None):
        if pageToken:
            self.search_uri = 'https://www.googleapis.com/youtube/v3/search?part=id&channelId=%s&pageToken=%s&maxResults=50&type=video&fields=items/id,nextPageToken&key=%s' % (channel_id['id'], pageToken, self.conf.APP_KEY)
        else:
            self.search_uri = 'https://www.googleapis.com/youtube/v3/search?part=id&channelId=%s&maxResults=50&type=video&fields=items/id,nextPageToken&key=%s' % (channel_id['id'], self.conf.APP_KEY)


    def set_video_uri(self, video_id):
        self.video_uri = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=%s&key=%s' % (video_id, self.conf.APP_KEY)