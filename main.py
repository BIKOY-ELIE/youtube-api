from classes.VideoSave import save_video
from classes.VideoFetcher import VideoFetcher
from classes.VideoFormat import VideoFormat
from classes.NextPageTokenWrite import NextPageTokenWrite
import os
from classes.GoogleAPIConnection import GoogleAPIConnection
import googleapiclient.errors


vds = VideoFetcher()
vd_fmt = VideoFormat()

keys_list = [os.getenv("API_KEY"), os.getenv("API_KEY1"), os.getenv(
    "API_KEY2"), os.getenv("API_KEY3")]

list_domains = ["getting started with Coding","getting started with algorithm", "Data Structure", "getting started with Data Structure"]

for key in keys_list:
    i = 0
    try:
        GAC = GoogleAPIConnection()
        txt = NextPageTokenWrite()
        for domain in list_domains:
            print(f"{domain} \n\n")
            videos = vds.fetch_videos(domain, GAC.connection(key))
            print(len(videos))
            print('\n\n')
            print(f" \n\n\{domain} \n\n")
            txt.write_last_domain(domain)
            if len(videos) > 0: i = i + 1
        break
    except googleapiclient.errors.HttpError:
        pass
    finally:
        del list_domains[0:i+1]