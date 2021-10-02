from unittest import TestCase

default_playlists = {
    "galopom_po_evropam_semin": "PLrULWNBdKzUiC95qca-DVXBIQaEofNtll",
    "samie_chestnie_novosti_lebedev": "PLmlTp5uCBYk7w6pryTr-Bd4SUZUvG4fQj",
    "rossiya_ukraina_solovyev": "PL0vZ0dCMJuU1Zo3oq4s5g3kAM1NT1Kno4",
    "lifehacks_double_bubble": "PLL5fTqvjKv3JaH8SofJ89geu2VwJL5R04",
    "goblin_news": "PLQCYG6lKBuTZkLKg-F6wKKqWh1iq1eJb2"
}


class TestLoad(TestCase):
    def test_process_playlist(self):
        vids = get_playlist_videos
