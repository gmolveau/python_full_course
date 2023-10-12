import datetime


class Airport:
    def __init__(self, name: str) -> None:
        self.name: str = name


class Stopover:
    def __init__(
        self,
        landing_date: datetime.datetime,
        takeoff_date: datetime.datetime,
        airport: Airport,
    ) -> None:
        self.takeoff_date: datetime.datetime = takeoff_date
        self.landing_date: datetime.datetime = landing_date
        self.airport: Airport = airport


class Flight:
    def __init__(
        self,
        takeoff_date: datetime.datetime,
        landing_date: datetime.datetime,
        takeoff_airport: Airport,
        landing_airport: Airport,
    ) -> None:
        self.takeoff_date: datetime.datetime = takeoff_date
        self.landing_date: datetime.datetime = landing_date
        self.takeoff_airport: Airport = takeoff_airport
        self.landing_airport: Airport = landing_airport
        self.stopovers: list(Stopover) = []
        self.bookable: bool = True

    def print_travel(self):
        print(f"Flight from {self.takeoff_airport.name} to {self.landing_airport.name}")
        print(f"- {self.takeoff_airport.name} : {self.takeoff_date}")
        for stopover in self.stopovers:
            print(
                f"- {stopover.airport.name} : {stopover.landing_date} -> {stopover.takeoff_date}"
            )
        print(f"- {self.landing_airport.name} : {self.landing_date}")


cdg = Airport("Paris CDG")
amsterdam = Airport("Amsterdam")
oslo = Airport("Oslo")
helsinki = Airport("Helsinki")

flight_49 = Flight(
    datetime.datetime(2022, 8, 20, 19, 43),
    datetime.datetime(2022, 8, 21, 8, 57),
    cdg,
    helsinki,
)

flight_49.stopovers.append(
    Stopover(
        datetime.datetime(2022, 8, 20, 22, 22),
        datetime.datetime(2022, 8, 20, 23, 23),
        amsterdam,
    )
)

flight_49.stopovers.append(
    Stopover(
        datetime.datetime(2022, 8, 21, 5, 5), datetime.datetime(2022, 8, 21, 6, 6), oslo
    )
)

flight_49.print_travel()
