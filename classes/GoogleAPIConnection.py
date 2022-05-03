import os
from googleapiclient.discovery import build

class GoogleAPIConnection():
        
    @classmethod
    def connection(self, API_KEY):
        Api = build(os.getenv("API_NAME"), os.getenv("API_VERSION"), developerKey=API_KEY)
        return Api