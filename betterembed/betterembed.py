from typing import List, Optional

from discord import Embed

from .exceptions import MissingArguments


class BetterEmbed(Embed):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def create(cls, fields: Optional[List] = None, **kwargs):
        if not kwargs.get("title") or kwargs.get("description"):
            raise MissingArguments

        self = cls.__new__(cls)
        self.__init__(**kwargs)

        if fields:
            for field in fields:
                self.add_field(name=field[0], value=field[1], inline=field[3])

        return self
