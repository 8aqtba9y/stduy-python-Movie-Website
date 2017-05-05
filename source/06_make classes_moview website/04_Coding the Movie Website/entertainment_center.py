import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


scent_of_a_woman = media.Movie("Scent of a Woman", "Whoo-ah!",
                               "https://upload.wikimedia.org/wikipedia/en/9/91/Scent_of_a_Woman.jpg",
                               "https://www.youtube.com/watch?v=ebDO0C-RTpU")


doctor_strange = media.Movie("Doctor Strange", "I had a fun",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")


despicable_me = media.Movie("Despicable Me", "",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=TZkAcKCFIVo")


edge_of_tomorrow = media.Movie("Edge of Tomorrow", "",
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=vw61gCe2oqI")


movies = [toy_story, avatar, scent_of_a_woman,
          doctor_strange, despicable_me, edge_of_tomorrow]
fresh_tomatoes.open_movies_page(movies)
