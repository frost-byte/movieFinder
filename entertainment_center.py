'''
entertainment_center
The main module which starts the Server and Opens the Movie Finder
site in a browser.
'''
import media
import movieFinder
import webbrowser
import threading

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://ia.media-imdb.com/images/M/"
                        "MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@"
                        "._V1_SX300.jpg",
                        "http://v.traileraddict.com/1463",
                        movie_year=1995,
                        isFavorite=True)

media.movieList.append(toy_story)

avatar = media.Movie("Avatar",
                     "A marine takes the place of his dead brother on a "
                     "mission to a remote planet",
                     "http://ia.media-imdb.com/images/M/"
                     "MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@"
                     "._V1_SX300.jpg",
                     "http://v.traileraddict.com/13413",
                     movie_year=2009,
                     isFavorite=True)
media.movieList.append(avatar)

gotg = media.Movie("Guardians of the Galaxy",
                   "A young boy is abducted by Aliens after his mother dies",
                   "http://ia.media-imdb.com/images/M/"
                   "MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx"
                   "._V1_SX300.jpg",
                   "http://v.traileraddict.com/86922",
                   movie_year=2014,
                   isFavorite=True)
media.movieList.append(gotg)

# The full title of Birdman causes issues with Trailer Addict;
# It is identified as "Birdman".
# In addition, it only has an international trailer.
birdman = media.Movie("Birdman: Or (The Unexpected Virtue of Ignorance)",
                      "An aging actor tries to escape a past role and redefine"
                      "his legacy by writing, directing and starring in a play"
                      " on Broadway",
                      "http://cdn.traileraddict.com/content/fox-searchlight/"
                      "birdman.jpg",
                      "http://v.traileraddict.com/93139",
                      movie_year=2014,
                      isFavorite=True)
media.movieList.append(birdman)


if __name__ == '__main__':
    # Create a delay before the web browser opens the index page for
    # the Fresh Tomatoes Movie Trailers
    threading.Timer(1.25,
                    lambda: webbrowser.open('http://localhost:5000')).start()

    # Run the flask application, which starts the server
    movieFinder.app.run(debug=False)
