from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_hall_by_id(cinema_hall_id: int) -> CinemaHall:
    return CinemaHall.objects.get(pk=cinema_hall_id)


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
        name: str,
        rows: int,
        seats_in_row: int
) -> CinemaHall:
    return CinemaHall.objects.create(
        name=name,
        rows=rows,
        seats_in_row=seats_in_row,
    )
