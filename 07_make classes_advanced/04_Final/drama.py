import media
import webbrowser as wb

class Drama(media.Media):
    def __init__(self, title, storyline, poster_image, trailer_youtube, seasons) :
        media.Media.__init__(self, title, storyline, poster_image, trailer_youtube)
        self.seasons = seasons

    def show_trailer(self) :
        wb.open(self.trailer_youtube_url)
