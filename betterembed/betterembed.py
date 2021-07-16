from discord import Embed

from .exceptions import MissingArguments


class BetterEmbed(Embed):
    def __init__(self, **kwargs):
        if not kwargs.get("title") or kwargs.get("description"):
            raise MissingArguments

        if kwargs.get("fields"):
            for field in kwargs.get("fields"):
                self.add_field(name=field[0], value=field[1], inline=field[3])

            del kwargs["fields"]

        if kwargs.get("author"):
            author = kwargs.get("author")
            self.set_author(name=author[0], url=author[1], icon_url=author[2])

            del kwargs["author"]

        if kwargs.get("footer"):
            footer = kwargs.get("footer")
            self.set_footer(text=footer[0], icon_url=footer[1])

            del kwargs["footer"]

        if kwargs.get("thumbnail"):
            self.set_thumbnail(kwargs.get("thumbnail"))

            del kwargs["thumbnail"]

        if kwargs.get("image"):
            self.set_image(kwargs.get("image"))

            del kwargs["image"]

        super().__init__(**kwargs)

    def apply_template(self, style: str):
        if style.lower() == "warn":
            self.title = f"⚠ {self.title}"
            self.color = 0xD8EF56

        if style.lower() == "error":
            self.title = f"❌  {self.title}"
            self.color = 0xFF0909
