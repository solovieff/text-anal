import json
import os
from utils import youtube, operations, analysis
from collections import Counter

youtube_token = 'UCgxTPTFbIbCWfTR9I2-5SeQ'

# change this values only!
links = youtube.get_playlist_links('https://www.youtube.com/playlist?list=PLY8fdk-3N0jC7JM_PCjHqZRTxr8KB41YA')
playlist_name = 'soloviev_polniy_kontakt'

transcripts_folder_path = 'transcripts/' + playlist_name + '/'
texts_folder_path = 'texts/' + playlist_name + '/'

meta_file_name = 'meta/' + playlist_name + '_meta.json'
result_file_name = 'results/' + playlist_name + '_result.json'

if not os.path.exists(transcripts_folder_path):
    os.mkdir(transcripts_folder_path)

if not os.path.exists(texts_folder_path):
    os.mkdir(texts_folder_path)

meta_list = []
for link in links:
    video_id = link.split("=")[1]
    print(video_id)
    try:
        youtube.get_video_transcript(video_id, transcripts_folder_path)
        meta = youtube.get_video_info(link, video_id)
        meta_list.append(meta)
    except:
        print('was unable to handle the url ' + link)

with open(meta_file_name, 'w', encoding='utf8') as fp:
    json.dump(meta_list, fp, indent=4, ensure_ascii=False)

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

print(counter.__sizeof__())
percent_counter = [(i, (count / counter.__sizeof__()) * 100.0) for i, count in counter.most_common()]
print(percent_counter[:30])

with open(result_file_name, 'w', encoding='utf8') as fp:
    json.dump(percent_counter[:200], fp, indent=4, ensure_ascii=False)
