from unittest import TestCase

import matplotlib.pyplot as plt
import pandas
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
        vids_gob = get_playlist_tones(default_playlists["goblin_news"])

        df_leb: DataFrame = DataFrame(vids_leb, columns=("publish_date", "tone"))
        df_leb = df_leb.set_index('publish_date')
        df_sem: DataFrame = DataFrame(vids_sem, columns=("publish_date", "tone"))
        df_sem = df_sem.set_index('publish_date')

        df_gob: DataFrame = DataFrame(vids_gob, columns=("publish_date", "tone"))
        df_gob = df_gob.set_index('publish_date')

        dfs = [df_leb, df_sem, df_gob]
        summary_df = pandas.concat(dfs, join='outer', axis=1)

        hd1_from = '2019-01-01 15:30:00'
        summary_df = summary_df[summary_df.index > hd1_from]
        summary_df.plot(use_index=True)
        plt.show()
        # normalized_df=(summary_df-summary_df.mean())/summary_df.std()
        normalized_df = (summary_df - summary_df.min()) / (summary_df.max() - summary_df.min())
        normalized_df.plot(use_index=True)
        plt.show()

        # pprint.pprint(vids)
