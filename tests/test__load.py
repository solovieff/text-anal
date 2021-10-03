from unittest import TestCase

from tubetone.db import save_video_data
from tubetone.loader import tone_playlist

default_playlists = {
    "galopom_po_evropam_semin": "PLrULWNBdKzUiC95qca-DVXBIQaEofNtll",
    "samie_chestnie_novosti_lebedev": "PLmlTp5uCBYk7w6pryTr-Bd4SUZUvG4fQj",
    "solovyev_live": "PLjxhi6qCzOky8dcV38caGem46goU7hQnB",
    "lifehacks_double_bubble": "PLL5fTqvjKv3JaH8SofJ89geu2VwJL5R04",
    "goblin_news": "PLQCYG6lKBuTZkLKg-F6wKKqWh1iq1eJb2",
    "minaev_live": "PLosWRcTJZf2qVMzr4rUqPbjrSg75lGtpa",
    "minaev_news_rus": "PLosWRcTJZf2qFwMeDb2doe2u5TQTESxOs",
    "interview_rbk": "PL8KkwRBLSol3E-BXr0fNdcU4oddkGgHkj",
    "ipo_review": "PLagcXWyrpiY6PUPlI-gx7w1uto_cXbzCI",
    "svetov_peredachi": "PLs_UHPP0bWJSIdQIXrXScsJ9bcxdVP716",
    "finansi_investicii": "PLjh-iJP12ptuMW4Y5ap5jrup5Fgg6KYhd",
}


class TestLoad(TestCase):
    def test_process_playlist(self):
        toned_vides = tone_playlist(default_playlists['minaev_news_rus'], amount=-1)

        for toned_video in toned_vides:
            save_video_data(toned_video)

    def test_load_new(self):
        for key, value in default_playlists:
            toned_videos = tone_playlist(value, amount=3)

            for toned_video in toned_videos:
                save_video_data(toned_video)
