import fresh_tomatoes
import movie
import drama

toy_story = movie.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc", 3)


avatar = movie.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ", 2)


scent_of_a_woman = movie.Movie("Scent of a Woman", "Whoo-ah!",
                               "https://upload.wikimedia.org/wikipedia/en/9/91/Scent_of_a_Woman.jpg",
                               "https://www.youtube.com/watch?v=ebDO0C-RTpU", 1)


doctor_strange = movie.Movie("Doctor Strange", "I had a fun",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM", 1)


despicable_me = movie.Movie("Despicable Me", "",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=TZkAcKCFIVo", 3)


edge_of_tomorrow = movie.Movie("Edge of Tomorrow", "",
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=vw61gCe2oqI", 1)


two_and_a_half_men = drama.Drama("Two and a Half Men", "",
                                 "https://upload.wikimedia.org/wikipedia/en/5/51/Two_and_a_Half_Men-title.png",
                                 "https://www.youtube.com/watch?v=097pUW0L_Xc", 12)


game_of_thrones = drama.Drama("Game of Thrones", "",
                              "https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg",
                              "https://www.youtube.com/watch?v=mg2xtVYgQhI", 7)


media = [toy_story, avatar, scent_of_a_woman,
         doctor_strange, despicable_me, edge_of_tomorrow,
         two_and_a_half_men, game_of_thrones]
fresh_tomatoes.open_movies_page(media)
