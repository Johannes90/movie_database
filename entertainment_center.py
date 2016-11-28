import media
import fresh_tomatoes

#Creating Movie Class Instances

fight_club = media.Movie("Fight Club",
                         "Fight Club is a 1999 American film based on the 1996 novel of the same name by Chuck Palahniuk. The film was directed by David Fincher, and stars Brad Pitt, Edward Norton and Helena Bonham Carter.",
                         "http://vignette1.wikia.nocookie.net/fightclub/images/6/6a/Fight-club-dvd.jpg/revision/latest?cb=20081116042426",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

ten_days = media.Movie("How to Lose a Guy in 10 Days",
                       "How to Lose a Guy in 10 Days is a 2003 romantic comedy film directed by Donald Petrie, starring Kate Hudson and Matthew McConaughey. It is based on a short cartoon book of the same name by Michele Alexander and Jeannie Long.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/0/07/HowToLoseAGuyimp.jpg/220px-HowToLoseAGuyimp.jpg",
                       "https://www.youtube.com/watch?v=EFGr2_cOOTk")

james_bond = media.Movie("James Bond: Spectre",
                         "Spectre is the twenty-fourth James Bond film produced by Eon Productions. It features Daniel Craig in his fourth performance as James Bond, and Christoph Waltz as Ernst Stavro Blofeld, with the film marking the character's re-introduction into the series. It was directed by Sam Mendes as his second James Bond film following Skyfall, with a screenplay written by John Logan, Neal Purvis, Robert Wade and Jez Butterworth. It is distributed by Metro-Goldwyn-Mayer and Columbia Pictures. With a budget around $245 million, it is the most expensive Bond film and one of the most expensive films ever made.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2Nzg4MzkwOF5BMl5BanBnXkFtZTgwNzA0OTE3NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                         "https://www.youtube.com/watch?v=LTDaET-JweU")

#Creating list from previous movies.

movies = [fight_club, ten_days, james_bond]

#Calling the fresh_tomatoes script with the created movie list.
fresh_tomatoes.open_movies_page(movies)