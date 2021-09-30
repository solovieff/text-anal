from unittest import TestCase

from tubetone.playlist._load import process_playlist


class TestLoad(TestCase):
    def test_process_playlist(self):
        # process_playlist(playlist_name="galopom_po_evropam_semin",
        # playlist_id="PLrULWNBdKzUiC95qca-DVXBIQaEofNtll")

        # process_playlist(playlist_name="samie_chestnie_novosti_lebedev",
        # playlist_id="PLmlTp5uCBYk7w6pryTr-Bd4SUZUvG4fQj")

        # process_playlist(playlist_name="rossiya_ukraina_solovyev",
        # playlist_id="PL0vZ0dCMJuU1Zo3oq4s5g3kAM1NT1Kno4")

        process_playlist(playlist_name="lifehacks_double_bubble",
                         playlist_id="PLL5fTqvjKv3JaH8SofJ89geu2VwJL5R04")
