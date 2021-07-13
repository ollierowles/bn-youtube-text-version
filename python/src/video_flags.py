"""A video playlist class."""


class Flagged:
    """A class used to represent a Playlist."""

    def __init__(self, name):
        self.name = name
        self.status = True
        self.reason = ''