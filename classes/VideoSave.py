from fastapi import FastAPI
from py2neo.ogm import GraphObject, Property,RelatedFrom
from classes.db_graph import graph

class Video(GraphObject):

    video_id = Property()
    title = Property()
    viewCount = Property()
    channel_name = Property()
    published_at = Property()
    description = Property()
    subtitles = Property()
    thumbnail = Property()

    gathered_by = RelatedFrom("Lesson","GATHER")
    watched_by = RelatedFrom("User","WATCH")

    def store(self):
        graph.push(self)


app = FastAPI()

@app.post("/save/video")
def save_video(video : dict):
    vid = Video(
        video_id = video['video_id'],
        title = video['title'],
        viewCount = video['view_count'],
        channel_name = video['channel_name'],
        published_at = video['published_at'],
        description = video['description'],
        # subtitles = video['subtitles'],
        thumbnail = video['thumbnails']
    )
    vid.store()