import media
import webbrowser as wb

class Movie(media.Media):
    def __init__(self, title, storyline, poster_image, trailer_youtube, series) :
        media.Media.__init__(self, title, storyline, poster_image, trailer_youtube)
        self.series = series

    def show_trailer(self) :
        wb.open(self.trailer_youtube_url)
