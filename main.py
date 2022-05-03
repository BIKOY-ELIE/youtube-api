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

list_domains = ["cybersecurity", "deep learning"]

for key in keys_list:
    i = 0
    try:
        GAC = GoogleAPIConnection()
        txt = NextPageTokenWrite()
        for domain in list_domains:
            i = i + 1
            print(f"{domain} \n\n")
            videos = vds.fetch_videos(domain, GAC.connection(key))
            print(len(videos))
            print('\n\n')
            print(f" \n\n\{domain} \n\n")
            txt.write_last_domain(domain)
            
            if i >= 100:
                list_domains.remove(domain)
        break
    except googleapiclient.errors.HttpError:
        pass
