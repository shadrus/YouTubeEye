from project.config.config import Conf
class ApiReq():
    def __init__(self):
        self.channel_uri = None
        self.search_uri = None
        self.video_uri = None

    def set_channel_uri(self):
        self.channel_uri = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=%s&fields=items&key=%s' % (Conf.USER_NAME, Conf.APP_KEY)

    def set_search_uri(self, channel_id):
        self.search_uri = 'https://www.googleapis.com/youtube/v3/search?part=id&channelId=%s&maxResults=50&fields=items/id,nextPageToken&key=%s' % (channel_id['id'], Conf.APP_KEY)

    def set_video_uri(self, video_id):
        self.video_uri = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=%s&key=%s' % (video_id, Conf.APP_KEY)