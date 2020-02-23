from __future__ import unicode_literals

from googleapiclient import discovery

url = 'https://www.youtube.com/watch?v=M7FIvfx5J10'
video_id = url.split('=')[1]

"""""Функция, которая достает основную информацию о видеоролике:
 Лайки, дизлайки, просмотры, языки, длительность, айди, описание,превью,количество комментов, канал,время, тэги. 
 Данные хранятся в словаре с соответствующими ключами"""


def video_information(videoid):
    api_key = 'AIzaSyC4BEjvtzErw6kbErLw8x2bhikb1DM2F1w'
    youtube = discovery.build('youtube', 'v3', developerKey=api_key)
    data = youtube.videos().list(part='snippet,contentDetails,statistics', id=videoid).execute()
    sub = youtube.captions().list(part='snippet', videoId=videoid).execute()
    keys = 'id', 'title', 'description', 'preview', 'channelTitle', 'likes', 'dislikes', 'comments', 'views', 'duration', 'language', 'tag', 'time','subs'
    for item in data.get('items'):
        id = item.get('id')
        title = item.get('snippet').get('title')
        channelTitle = item.get('snippet').get('channelTitle')
        description = item.get('snippet').get('description')
        preview = item.get('snippet').get('thumbnails').get('high').get('url')
        likes = item.get('statistics').get('likeCount')
        dislikes = item.get('statistics').get('dislikeCount')
        comments = item.get('statistics').get('commentCount')
        views = item.get('statistics').get('viewCount')
        duration = item.get("contentDetails").get('duration')
        language = item.get('snippet').get('language')
        tags = item.get('snippet').get('tags')
        time = item.get('snippet').get('publishedAt')
        subs = [item.get('snippet').get('language') for item in sub.get('items')]

        values = id, title, description, preview, channelTitle, likes, dislikes, comments, views, duration, language, tags, time,subs

    video_item = dict(zip(keys, values))
    return (video_item)


""" Функция, которая достает комментарии ( пока что не очень понятно, по какому принципу)"""


def get_comments(video_id):
    api_key = 'AIzaSyC4BEjvtzErw6kbErLw8x2bhikb1DM2F1w'
    youtube = discovery.build('youtube', 'v3', developerKey=api_key)
    results = youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=100).execute()
    # keys = 'author', 'comment', 'likes'

    for item in results["items"]:
        comment = item.get("snippet").get("topLevelComment")
        author = comment.get("snippet").get("authorDisplayName")
        text = comment.get("snippet").get("textDisplay")
        likes = comment.get("snippet").get("likeCount")
        print((author, text, likes))
        # values = author, text, likes
    return results['items']


"""Функция выводит number первых трендов и информацию о них"""


def popular(youtube, number):
    data = youtube.videos().list(part='snippet,contentDetails,statistics', chart='mostPopular', regionCode='RU',
                                 maxResults=number).execute()
    keys = 'id', 'title', 'description', 'preview', 'channelTitle', 'likes', 'dislikes', 'comments', 'views', 'duration', 'language', 'tag', 'time'
    for item in data.get('items'):
        id = item.get('id')
        title = item.get('snippet').get('title')
        channelTitle = item.get('snippet').get('channelTitle')
        description = item.get('snippet').get('description')
        preview = item.get('snippet').get('thumbnails').get('high').get('url')
        likes = item.get('statistics').get('likeCount')
        dislikes = item.get('statistics').get('dislikeCount')
        comments = item.get('statistics').get('commentCount')
        views = item.get('statistics').get('viewCount')
        duration = item.get("contentDetails").get('duration')
        language = item.get('snippet').get('language')
        tags = item.get('snippet').get('tags')
        time = item.get('snippet').get('publishedAt')
        values = id, title, description, preview, channelTitle, likes, dislikes, comments, views, duration, language, tags, time
        video_item = dict(zip(keys, values))
        print(video_item)
    return data['items']



api_key = 'AIzaSyC4BEjvtzErw6kbErLw8x2bhikb1DM2F1w'
youtube = discovery.build('youtube', 'v3', developerKey=api_key)
print(video_information(video_id))
