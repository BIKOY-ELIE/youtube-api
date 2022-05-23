import csv

class WriteVideoData:
	filename = 'files/video_data.csv'

	def __init__(self) -> None:
		pass

	@classmethod
	def storeVideoData(self, *video_list):
		with open(self.filename, 'a') as csvfile: 
	    	# creating a csv writer object 
		    csvwriter = csv.writer(csvfile) 
	        
		    # writing data rows 
		    writer.writerows(video_list)
		printf('\n\n-------------------------videos bien store !----------------------\n\n')