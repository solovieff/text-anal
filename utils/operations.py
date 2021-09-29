import json


def eyesore(string_to_check):
    eyesores = ['музыка', 'апплодисменты']
    for text in eyesores:
        if (string_to_check.find(text) == True):
            return True
    return False


def concatText(video_id, transcripts_folder_path, texts_folder_path):
    with open(transcripts_folder_path + video_id + '_transcript.json', 'r') as f:
        all_data = json.load(f)
    all_text = ""
    for text_chunk in all_data:
        if eyesore(text_chunk['text']) == False:
            # print(text_chunk['text'])
            all_text = all_text + " " + text_chunk['text']
    with open(texts_folder_path + video_id + '_full_text.txt', 'bw') as f:
        f.write(all_text.encode())
    return all_text
