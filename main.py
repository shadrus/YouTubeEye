__author__ = 'Yury Krylov'
from subprocess import call
from models.api_req import ApiReq
import urllib2
import json
import shelve
from models.result import Result
from os import path

result = []


def get_youtube_json(uri):
    req = urllib2.Request(uri)
    try:
        response = urllib2.urlopen(req, timeout=1000)
        return response.read()
    except urllib2.URLError:
        return None


def parceChannelinfo(dic, wanted_keys):
    for k, v in dic.items():
        if isinstance(v, dict):
            parceChannelinfo(v, wanted_keys)
        elif isinstance(v, list):
            for item in v:
                parceChannelinfo(item, wanted_keys)
        else:
            if k in wanted_keys:
                result.append({k: v})


def result_counter(result):
    final = Result()
    for item in result:
        for key, value in item.items():
            if key == 'viewCount':
                final.view_count += int(value)
            elif key == 'subscriberCount':
                final.subscribers = int(value)
            elif key == 'commentCount':
                final.comments += int(value)
            elif key == 'dislikeCount':
                final.dislikes_count += int(value)
            elif key == 'likeCount':
                final.likes_count += int(value)
    return final


def show_notif(data, channel_id):
    """
    https://github.com/alloy/terminal-notifier
    $ terminal-notifier -[message|group|list] [VALUE|ID|ID] [options]
    """
    call(["terminal-notifier", "-title", "Youtube Eye", "-message", data.__str__(), "-open",
          "http://www.youtube.com/channel/%s" % channel_id['id']])


def get_Youtube_data(uri, wanted_keys):
    channel_stat = get_youtube_json(uri)
    if channel_stat != None:
        dic = json.loads(channel_stat)
        parceChannelinfo(dic, wanted_keys)
        return dic
    else:
        return False


def save_data_to_file(youtube_data):
    d = shelve.open('eyedb')
    d['data'] = youtube_data
    d.close()


def get_data_from_file():
    d = shelve.open('eyedb')
    data = d['data']
    d.close()
    return data


def cmp_data(youtube_data):
    cmped_result = Result()
    db_data = get_data_from_file()
    cmped_result.likes_count = youtube_data.likes_count - db_data.likes_count
    cmped_result.dislikes_count = youtube_data.dislikes_count - db_data.dislikes_count
    cmped_result.comments = youtube_data.comments - db_data.comments
    cmped_result.subscribers = youtube_data.subscribers - db_data.subscribers
    cmped_result.view_count = youtube_data.view_count - db_data.view_count
    return cmped_result


def main():
    data = ApiReq()
    data.set_channel_uri()
    wanted_keys = ['subscriberCount', 'id']  # The keys you want
    returned = get_Youtube_data(data.channel_uri, wanted_keys)
    if not returned:
        return
    channel_id = result[1]
    data.set_search_uri(channel_id)
    wanted_keys = ['videoId', 'nextPageToken']  # The keys you want
    #First search
    def without_next_token():
        return get_Youtube_data(data.search_uri, wanted_keys)

    returned = without_next_token()
    print returned
    if not returned:
        return
    while type(returned) == dict:
        if 'nextPageToken' in returned.keys():
            data.set_search_uri(channel_id, returned['nextPageToken'])
            returned = get_Youtube_data(data.search_uri, wanted_keys)
            print "in while", returned
        else:
            break

    else:
            print "the end"


    wanted_keys = ['viewCount', 'likeCount', 'dislikeCount', 'commentCount']  # The keys you want

    for item in result:
        print "in item", item
        for key, value in item.items():
            if key == 'videoId':
                data.set_video_uri(value)
                returned = get_Youtube_data(data.video_uri, wanted_keys)
                print returned
                if not returned:
                    print "no return"
                    return
    data_from_youtube = result_counter(result)
    print data_from_youtube

    if path.isfile('eyedb.db'):
        notif_data = cmp_data(data_from_youtube)
        if notif_data.__str__() != "":
            show_notif(notif_data, channel_id)
    else:
        show_notif(data_from_youtube, channel_id)
    save_data_to_file(data_from_youtube)


if __name__ == '__main__':
    main()
