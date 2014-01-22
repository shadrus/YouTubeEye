__author__ = 'macpro'
class Result():
    def __init__(self, view_count=0, subscribers=0, likes_count=0, dislikes_count=0, comments=0):
        self.view_count = view_count
        self.subscribers = subscribers
        self.likes_count = likes_count
        self.dislikes_count = dislikes_count
        self.comments = comments

    def __str__(self):
        result_str = ""
        if self.view_count > 0:
            result_str += 'Views: %s ' % self.view_count
        if self.subscribers > 0:
            result_str += 'Subscribers: %s. ' % self.subscribers
        if self.likes_count > 0:
            result_str += 'Likes: %s. ' % self.likes_count
        if self.dislikes_count > 0:
            result_str += 'Dislikes: %s. ' % self.dislikes_count
        if self.comments > 0:
            result_str += 'Comments: %s. ' % self.comments
        return result_str
