import pprint
from dataclasses import asdict
from unittest import TestCase

from db import save_video_data
from tubetone.loader import tone_playlist

default_playlists = {
    "galopom_po_evropam_semin": "PLrULWNBdKzUiC95qca-DVXBIQaEofNtll",
    "samie_chestnie_novosti_lebedev": "PLmlTp5uCBYk7w6pryTr-Bd4SUZUvG4fQj",
    "rossiya_ukraina_solovyev": "PL0vZ0dCMJuU1Zo3oq4s5g3kAM1NT1Kno4",
    "lifehacks_double_bubble": "PLL5fTqvjKv3JaH8SofJ89geu2VwJL5R04"
}


class TestLoad(TestCase):
    def test_process_playlist(self):
        toned_vides = tone_playlist(default_playlists['galopom_po_evropam_semin'], amount=1)

        first_toned = toned_vides[0]

        pprint.pprint(asdict(first_toned))

        save_video_data(first_toned)
