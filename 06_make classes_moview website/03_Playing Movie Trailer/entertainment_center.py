import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print toy_story.storyline


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
print avatar.storyline
# avatar.show_trailer()


scent_of_a_woman = media.Movie("Scent of a Woman",
                               "Whoo-ah!",
                               "https://upload.wikimedia.org/wikipedia/en/9/91/Scent_of_a_Woman.jpg",
                               "https://www.youtube.com/watch?v=ebDO0C-RTpU")

print scent_of_a_woman.storyline
scent_of_a_woman.show_trailer()
