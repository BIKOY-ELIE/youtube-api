import os
from classes.GoogleAPIConnection import GoogleAPIConnection
import googleapiclient.errors
from classes.VideoSave import save_video
from classes.VideoFormat import VideoFormat
from py2neo.ogm import GraphObject
from classes.NextPageTokenWrite import NextPageTokenWrite

class VideoFetcher:
    
    
    
    vd_fmt = VideoFormat()
    

    def __init__(self) -> None:
        pass
    
    
    @classmethod
    def fetch_videos(self, title: str, youtube, type:str):
        next_page_token = None
        video_lists = []
        i = 0
        while True:
            video_ids = []
            playlist_ids = []
            
            # get the videos id
            request_search = youtube.search().list(
                part="snippet",
                q="getting start " + title,
                maxResults=50,
                pageToken=next_page_token,
                relevanceLanguage = "en",
                type=type,
            )
            response_search = request_search.execute()

            if type == 'video':
                # add the list of ids in video_ids
                for video in response_search['items']:
                    videoId = video['id']['videoId']
                    video_ids.append(videoId)

                # save the next page token in a variable
                next_page_token = response_search.get('nextPageToken')
                

                # get videos
                request_video = youtube.videos().list(
                    part='statistics, snippet',
                    id=','.join(video_ids)
                )
                response_video = request_video.execute()

                # Format and save each videos
                for video in response_video['items']:
                    i = i + 1
                    video_lists.append(video)
                    try:
                        save_video(self.vd_fmt.video_format(video))
                        print(f"{i}'->' ,{self.vd_fmt.video_format(video)}")
                        print('\n\n')
                    except KeyError:
                        pass

                # break the loop
                if not next_page_token:
                    break

            else:
                # add the list of ids in playlist_ids
                for playlist in response_search['items']:
                    playlistId = playlist['id']['playlistId']
                    playlist_ids.append(playlistId)

                # save the next page token in a variable
                next_page_token = response_search.get('nextPageToken')

                # get video of each playlist
                for playlistId in playlist_ids:

                    # get playlist videos id
                    request_playlist = youtube.playlistItems().list(
                        part='contentDetails',
                        playlistId=playlistId
                    )
                    response_playlist = request_playlist.execute()

                    # add the list of ids in video_ids
                    for video in response_playlist['items']:
                        videoId = video['contentDetails']['videoId']
                        video_ids.append(videoId)


                    # get videos
                    request_video = youtube.videos().list(
                        part='statistics, snippet',
                        id=','.join(video_ids)
                    )
                    response_video = request_video.execute()

                    # Format and save each videos
                    for video in response_video['items']:
                        i = i + 1
                        video_lists.append(video)
                        try:
                            save_video(self.vd_fmt.video_format(video))
                            print(f"{i}'->' ,{self.vd_fmt.video_format(video)}")
                            print('\n\n')
                        except KeyError:
                            pass

                # break the loop
                if not next_page_token:
                    break

        return video_lists
