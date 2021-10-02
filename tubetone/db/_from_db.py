import pymongo

from tubetone import constants
from tubetone.models import ToneTube

__mongo_client = pymongo.MongoClient(
    constants.DB_URL,
    connectTimeoutMS=5000, socketTimeoutMS=3000, tlsInsecure=True)


def get_playlist_videos(playlist_id: str, projection=None):
    db = __mongo_client.get_database(constants.DB_NAME)
    videos_collection = db[constants.COLLECTION_VIDEOS]

    if not projection:
        projection = dict(_id=0, full_text=0, transcripts=0)

    vids = videos_collection.find({"playlist_id": playlist_id}, projection).sort([("publish_date", pymongo.ASCENDING)])

    return map(ToneTube, vids)
