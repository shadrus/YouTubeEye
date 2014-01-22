class ApiReq():
    APP_KEY = 'AIzaSyDp-PcpZl6OaQQeRQ9tLggmL3x_Fw0-i80'
    USER_NAME = 'shadrus'
    def __init__(self):
        self.channel_uri = None
        self.search_uri = None
        self.video_uri = None

    def set_channel_uri(self):
        self.channel_uri = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=%s&fields=items&key=%s' % (self.USER_NAME, self.APP_KEY)

    def set_search_uri(self, channel_id):
        self.search_uri = 'https://www.googleapis.com/youtube/v3/search?part=id&channelId=%s&maxResults=50&fields=items/id,nextPageToken&key=%s' % (channel_id['id'], self.APP_KEY)

    def set_video_uri(self, video_id):
        self.video_uri = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=%s&key=%s' % (video_id, self.APP_KEY)