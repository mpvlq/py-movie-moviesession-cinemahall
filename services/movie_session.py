from django.db.models import QuerySet

from db.models import Movie, MovieSession, CinemaHall


def get_movies_sessions() -> QuerySet[MovieSession]:
    return MovieSession.objects.all()


def create_movie_session(
        show_time: str,
        cinema_hall: CinemaHall,
        movie: Movie
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=show_time,
        cinema_hall=cinema_hall,
        movie=movie,
    )
