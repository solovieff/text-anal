import json
import os
import ssl
from collections import Counter
from dataclasses import dataclass

import pymongo as pymongo
from bson import json_util
from dostoevsky.models import FastTextSocialNetworkModel
from dostoevsky.tokenization import RegexTokenizer
from pytube import Playlist, YouTube
from youtube_transcript_api import TranscriptsDisabled

from utils.operations import eyesore
from .. import constants
from ..utils import youtube, analysis, operations


@dataclass
class ToneTube:
    transcript_text: str
    publish_date: str
    meta: dict


def process_playlist(playlist_name="soloviev_polniy_kontakt", playlist_id="PLY8fdk-3N0jC7JM_PCjHqZRTxr8KB41YA"):
    """

    :param playlist_name: how the resulting files will be named
    :param playlist_id: youtube playlist id
    """
    youtube_token = constants.YOUTUBE_TOKEN
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    ssl._create_default_https_context = ssl._create_unverified_context
    playlist = Playlist(f'{constants.YOUTUBE_PLAYLIST_PRE_URL}{playlist_id}')
    _clear_playlist_data(playlist_id=playlist.playlist_id)
    videos = playlist.videos

    transcripts_folder_path = constants.TRANSCRIPTS_FOLDER_PATH + playlist_name + '/'
    texts_folder_path = constants.TEXTS_FOLDER_PATH + playlist_name + '/'

    meta_file_name = constants.META_FOLDER_PATH + playlist_name + '_meta.json'

    result_file_name = constants.RESULTS_FOLDER_PATH + playlist_name + '_result.json'

    if not os.path.exists(transcripts_folder_path):
        os.mkdir(transcripts_folder_path)

    if not os.path.exists(texts_folder_path):
        os.mkdir(texts_folder_path)
    meta_list = []
    for video in videos[:5]:
        meta = _process_video(playlist, video, lang='ru', transcripts_folder_path=transcripts_folder_path)
        meta_list.append(meta)

    with open(meta_file_name, 'w', encoding='utf8') as fp:
        json.dump(meta_list, fp, indent=4, ensure_ascii=False, default=str)
    return

    for filename in os.listdir(transcripts_folder_path):
        if filename.endswith(".json") and filename.find("_transcript"):
            video_id = filename.split("_transcript")[0]
            operations.concatText(video_id, transcripts_folder_path, texts_folder_path)
        else:
            os.remove(transcripts_folder_path + filename)
    counter = Counter([])

    for filename in os.listdir(texts_folder_path):
        with open(texts_folder_path + filename, 'r') as text_file:
            data = text_file.read().replace('\n', '')
            a_data = analysis.frequency(data)
            counter = counter + a_data

    percent_counter = [(i, (count / counter.__sizeof__()) * 100.0) for i, count in counter.most_common()]
    print(percent_counter[:30])

    with open(result_file_name, 'w', encoding='utf8') as fp:
        json.dump(percent_counter[:200], fp, indent=4, ensure_ascii=False, default=json_util.default)


def _process_video(playlist: Playlist, video: YouTube, lang: str = 'ru', transcripts_folder_path: str = ''):
    video_id = video.video_id
    captions = video.caption_tracks

    for cap in captions:
        print(cap)

    try:
        transcript = youtube.get_video_transcript(video_id, lang, transcripts_folder_path)

        meta = youtube.get_video_info(video)
        video_data = dict(meta)
        video_data['transcript'] = transcript
        video_data['channel_name'] = playlist.title
        video_data['playlist_id'] = playlist.playlist_id
        video_data['owner'] = playlist.owner
        video_data['lang'] = lang

        all_text = ""
        for text_chunk in transcript:
            if eyesore(text_chunk['text']) == False:
                all_text = all_text + " " + text_chunk['text']
        video_data['all_text'] = all_text
        video_data['analysis'] = _analyse_text(all_text)

        _save_video_data(video_data)
        return meta
    except TranscriptsDisabled as e:
        print('was unable to handle the url ' + video.video_id)
        print(e)
        # raise e


def _clear_playlist_data(playlist_id: str):
    client = pymongo.MongoClient(
        "mongodb+srv://aragorn:#aragorn#@cluster0.dlx9j.mongodb.net/tubetune?retryWrites=true&w=majority",
        connectTimeoutMS=5000, socketTimeoutMS=3000, tlsInsecure=True)
    db = client.get_database(constants.DB_NAME)
    videos_collection = db[constants.COLLECTION_VIDEOS]
    videos_collection.delete_many({"playlist_id": playlist_id})


def _save_video_data(data: dict):
    client = pymongo.MongoClient(
        "mongodb+srv://aragorn:#aragorn#@cluster0.dlx9j.mongodb.net/tubetune?retryWrites=true&w=majority",
        connectTimeoutMS=5000, socketTimeoutMS=3000, tlsInsecure=True)
    print(client.server_info())
    print(client.list_database_names())
    db = client.get_database(constants.DB_NAME)
    videos_collection = db[constants.COLLECTION_VIDEOS]

    print(f'saving {data["title"]}...')
    result = videos_collection.update_one({'video_id': data['video_id']},
                                          {'$set': data},
                                          upsert=True)
    # videos_collection.insert_one(data)
    print(f'done saving {data["title"]}...{result}')


def _analyse_text(text: str):
    tokenizer = RegexTokenizer()
    tokens = tokenizer.split(
        'хуй в залупе я люблю краков и его жителей')  # [('всё', None), ('очень', None), ('плохо', None)]

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    messages = [
        text
    ]

    results = model.predict(messages, k=2)

    for message, sentiment in zip(messages, results):
        print('------ ', sentiment)

    return results
