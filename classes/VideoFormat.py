class VideoFormat:
    
    def __init__(self):
        pass    
    
    
    @classmethod
    def video_format(self, video : dict) -> dict:
        vid_fmt = {
            "video_id" : video["id"],
            "title" : video["snippet"]["title"],
            "view_count" : video["statistics"]["viewCount"],
            "description" : video["snippet"]["description"],
            "published_at" : video["snippet"]["publishedAt"],
            "thumbnails" : video["snippet"]["thumbnails"]["medium"]["url"],
            "channel_id" : video["snippet"]["channelId"],
            "channel_name" : video["snippet"]["channelTitle"],
        }
        
        return vid_fmt