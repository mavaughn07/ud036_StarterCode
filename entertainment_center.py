import media
import fresh_tomatoes

#Six movies created below following the structure (title, storyline, youtube_url, poster_image_url)
silver_linigs_playbook = media.Movie("Silver Linings Playbook", "After a stint "
                                     "in a mental institution, former teacher "
                                     "Pat Solitano moves back in with his "
                                     "parents and tries to reconcile with his "
                                     "ex-wife. Things get more challenging when"
                                     " Pat meets Tiffany, a mysterious girl "
                                     "with problems of her own.",
                                     "https://www.youtube.com/watch?v=Lj5_FhLaaQQ",
                                     "https://upload.wikimedia.org/wikipedia/en/9/9a/Silver_Linings_Playbook_Poster.jpg")

the_dark_knight = media.Movie("The Dark Knight", "When the menace known as the "
                              "Joker wreaks havoc and chaos on the people of "
                              "Gotham, the Dark Knight must come to terms with "
                              "one of the greatest psychological tests of his "
                              "ability to fight injustice.",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg")

interstellar = media.Movie("Interstellar", "A team of explorers travel through "
                           "a wormhole in space in an attempt to ensure "
                           "humanity's survival.",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg")

back_to_the_future = media.Movie("Back to the Future", "Marty McFly, a 17-"
                                 "year-old high school student, is accidentally"
                                 " sent 30 years into the past in a "
                                 "time-traveling DeLorean invented by his close"
                                 " friend, the maverick scientist Doc Brown.",
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs",
                                 "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg")

gladiator = media.Movie("Gladiator", "When a Roman general is betrayed and his "
                        "family murdered by an emperor's corrupt son, he comes "
                        "to Rome as a gladiator to seek revenge.",
                        "https://www.youtube.com/watch?v=0BLZbrLogTo",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg")

the_departed = media.Movie("The Departed", "An undercover cop and a mole in the"
                           " police attempt to identify each other while "
                           "infiltrating an Irish gang in South Boston.",
                           "https://www.youtube.com/watch?v=iojhqm0JTW4",
                           "https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg")

#array created below to send to webpage generation
movies = [silver_linigs_playbook, the_dark_knight, interstellar,
          back_to_the_future, gladiator, the_departed]

fresh_tomatoes.open_movies_page(movies)
