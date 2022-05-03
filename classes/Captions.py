from classes.GoogleAPIConnection import GoogleAPIConnection

class Captions:
    GAC = GoogleAPIConnection()
    youtube = GAC.connection()
    
    def __init__(self) -> None:
        pass
    
    
    @classmethod
    def get_captions(self, videos_id : str) -> dict:
        request = self.youtube.captions().list(
                part='snippet',
                videoId = videos_id,
            )
        response = request.execute()
        
        return response['items']