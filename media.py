import webbrowser

class Movie():
    def __init__(self, name, story, trailer, image):
        self.title = name
        self.storyline = story
        self.trailer_youtube_url = trailer
        self.poster_image_url = image

    def show_trailer():
    	#open youtube video
    	webbrowser.open(yt_trailer)
