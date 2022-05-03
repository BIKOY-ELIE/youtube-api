from numpy import char


class NextPageTokenWrite:
    
    def __init__(self):
        pass
    
    
    """
        # write the token of the next page of video fetcher in the file next_page_token.txt
        #
        # @param token : str
    """
    def write_the_next_page_token(self, token : str):
        with open('files/next_page_token.txt', 'w') as file:
           file.write(token)
    
    """
        # write the last domain search in the file in last_domain_search.txt
        #
        # @param token : str
    """
    def write_last_domain(self, token : str):
        with open('files/last_domain_search.txt', 'w') as file:
           file.write(token)
        
        
    """
        # read the token of the next page of video fetcher in the file next_page_token.txt
        #
        # @return token : str
    """   
    def read_the_token(self):
        with open('files/next_page_token.txt', 'r') as file:
            token = file.read()
            return token