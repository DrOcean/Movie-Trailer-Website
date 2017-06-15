import fresh_tomatoes
import media

# Create instances of the class "Movie" in the module "media"

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, "
                         "looking for a way to change his life",
                         "https://upload.wikimedia.org"
                         "/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_game = media.Movie("The Game",
                       "After a wealthy banker is given an opportunity to "
                       "participate in a mysterious game, "
                       "his life is turned upside down.",
                       "https://upload.wikimedia.org"
                       "/wikipedia/en/5/53/TheGame_poster323.jpg",
                       "https://www.youtube.com"
                       "/watch?v=0kqQNBR09Rc")

deadpool = media.Movie("Deadpool",
                       "A former special forces soldier "
                       "becomes a self-healing hero",
                       "https://upload.wikimedia.org"
                       "/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=sa-KE1SJ2As")

# Define a list/array for available movies and call the method to open a
# website

movies = [fight_club, the_game, deadpool]
fresh_tomatoes.open_movies_page(movies)
