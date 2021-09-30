import os

COLLECTION_VIDEOS = "video"
DB_NAME = "tubetune"
YOUTUBE_TOKEN = os.getenv('TUBETONE_YOUTUBE_TOKEN', 'UCgxTPTFbIbCWfTR9I2-5SeQ')
YOUTUBE_PLAYLIST_PRE_URL = os.getenv('TUBETONE_YOUTUBE_PLAYLIST_PRE_URL', 'https://www.youtube.com/playlist?list=')
TRANSCRIPTS_FOLDER_PATH = os.getenv('TUBETONE_TRANSCRIPTS_FOLDER_PATH', os.getcwd() + '/transcripts/')
TEXTS_FOLDER_PATH = os.getenv('TUBETONE_TEXTS_FOLDER_PATH', os.getcwd() + '/texts/')
META_FOLDER_PATH = os.getenv('TUBETONE_META_FOLDER_PATH', os.getcwd() + '/meta/')
RESULTS_FOLDER_PATH = os.getenv('TUBETONE_RESULTS_FOLDER_PATH', os.getcwd() + '/results/')

if not os.path.exists(TRANSCRIPTS_FOLDER_PATH):
    os.mkdir(TRANSCRIPTS_FOLDER_PATH)

if not os.path.exists(TEXTS_FOLDER_PATH):
    os.mkdir(TEXTS_FOLDER_PATH)

if not os.path.exists(META_FOLDER_PATH):
    os.mkdir(META_FOLDER_PATH)

if not os.path.exists(RESULTS_FOLDER_PATH):
    os.mkdir(RESULTS_FOLDER_PATH)
