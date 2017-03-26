import media
import fresh_tomatoes

#Initialising movie variables
toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "A story of a boy and his toyts that came to life",)

beauty_beast = media.Movie("Beauty and the Beast",
                            "https://resizing.flixster.com/uXYL2kMVgKqV6XWD6FVTVhjixaU=/206x305/v1.bTsxMjMwMzAzMTtqOzE3Mjg3OzEyMDA7MTY4ODsyNTAw",
                            "https://www.youtube.com/watch?v=e3Nl_TCQXuw")

logan = media.Movie("Logan",
                    "https://resizing.flixster.com/P8AinsdI0XeV-AsyhgkcihWdhWs=/206x305/v1.bTsxMjMwNDQ4NDtqOzE3Mjg3OzEyMDA7NjI2OzkyNA",
                    "https://www.youtube.com/watch?v=gbug3zTm3Ws")

lego_batman = media.Movie("Lego Batman Movie",
                          "https://resizing.flixster.com/Q8EczrF-BwPFUdmvOLN1z3gq4xQ=/206x305/v1.bTsxMjI3NjU0NTtqOzE3Mjg3OzEyMDA7NDA1MDs2MDAw",
                          "https://www.youtube.com/watch?v=LZSQTVdF3QM")

fantastic_beasts = media.Movie("Fantastic Beasts and Where to Find Them",
                               "https://resizing.flixster.com/-SG0cfLkxqoY9YKh4zqP6c3vqp0=/206x305/v1.bTsxMjIzMjgwMDtqOzE3Mjg2OzEyMDA7NjI0OzkyNQ",
                               "https://www.youtube.com/watch?v=VYZ3U1inHA4")

justice_league = media.Movie("Justice League",
                             "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
                             "https://www.youtube.com/watch?v=GEvAFds7ZDk")

movies = [toy_story, lego_batman, justice_league, beauty_beast, logan, fantastic_beasts]
fresh_tomatoes.open_movies_page(movies)
