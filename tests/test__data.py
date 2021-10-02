from unittest import TestCase

import matplotlib.pyplot as plt
from pandas import DataFrame

from tubetone.db import get_playlist_tones

default_playlists = {
    "galopom_po_evropam_semin": "PLrULWNBdKzUiC95qca-DVXBIQaEofNtll",
    "samie_chestnie_novosti_lebedev": "PLmlTp5uCBYk7w6pryTr-Bd4SUZUvG4fQj",
    "rossiya_ukraina_solovyev": "PL0vZ0dCMJuU1Zo3oq4s5g3kAM1NT1Kno4",
    "lifehacks_double_bubble": "PLL5fTqvjKv3JaH8SofJ89geu2VwJL5R04",
    "goblin_news": "PLQCYG6lKBuTZkLKg-F6wKKqWh1iq1eJb2"
}


class TestData(TestCase):
    def test_basic_stats(self):
        vids_leb = get_playlist_tones(default_playlists["samie_chestnie_novosti_lebedev"])
        vids_sem = get_playlist_tones(default_playlists["galopom_po_evropam_semin"])

        df_leb: DataFrame = DataFrame(vids_leb, columns=("publish_date", "tone"))
        df_sem: DataFrame = DataFrame(vids_leb, columns=("publish_date", "tone"))

        df_leb.plot(x="publish_date", y="tone")
        df_sem.plot(x="publish_date", y="tone")
        plt.show()

        # pprint.pprint(vids)
