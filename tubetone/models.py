import pprint
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class ToneTube:
    video_id: str
    title: str
    playlist_id: str
    playlist_name: str
    url: str
    views: int
    description: str
    publish_date: str
    author: str
    transcript: List[dict]
    full_text: str
    tone_analysis: dict
    morph_analysis: dict
    rating: float
    keywords: List[str]
    lang: str

    def view_main(self):
        dict_to_view = asdict(self)
        dict_to_view.pop("full_text")
        dict_to_view.pop("transcript")
        dict_to_view.pop("description")
        pprint.pprint(dict_to_view)
