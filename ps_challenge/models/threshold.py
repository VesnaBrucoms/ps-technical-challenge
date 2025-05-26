class Threshold:
    """An achievement level's criteria thresholds and associated name."""

    def __init__(
        self,
        games: int,
        percentage: float,
        over_100: bool,
        over_80: bool,
        over_75: bool,
        name: str,
    ):
        self.games = games
        self.percentage = percentage
        self.over_100 = over_100
        self.over_80 = over_80
        self.over_75 = over_75
        self.name = name
