import json
import urllib.request

import certifi
from pytube import Playlist, YouTube
from youtube_transcript_api import YouTubeTranscriptApi


def get_video_transcript(video_id, folder_path):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    with open(folder_path + video_id + '_transcript.json', 'w', encoding='utf8') as outfile:
        json.dump(transcript, outfile, indent=4, ensure_ascii=False)
    return transcript

def get_video_info(video_url, video_id):
    movie = YouTube(video_url)
    # todo: no date info );
    movie_data = {}
    movie_data['title'] = movie.title
    movie_data['id'] = video_id
    movie_data['url'] = video_url
    movie_data['rating'] = movie.rating
    movie_data['views'] = movie.views
    movie_data['description'] = movie.description
    return movie_data

def get_playlist_links(playlist_url):
    playlist = Playlist(playlist_url)
    # get more video details later
    links = playlist.parse_links()
    print('Number of videos in playlist: %s' % len(links))
    return links

def get_all_videos_in_channel_from_official_api(channel_id):
    api_key = "AIzaSyDLcXZghtIgi74qyjpEPLnyIvhRsWCKalU"

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    base_captions_url = 'https://www.googleapis.com/youtube/v3/captions?'

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                        channel_id)

    video_links = []
    url = first_url
    while True:
        print(url)
        inp = urllib.request.urlopen(url, cafile=certifi.where())
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                print(base_video_url + i['id']['videoId'])
                video_links.append(base_video_url + i['id']['videoId'])
                captions_url = base_captions_url + 'videoId=' + i["id"]['videoId'] + '&part=snippet&key=' + api_key
                print(captions_url)
                captions_resp = urllib.request.urlopen(captions_url, cafile=certifi.where())
                print(captions_resp)
            break
        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except (RuntimeError, IndexError) as err:
            print(err)
            break

    return video_links

