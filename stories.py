"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def __repr__(self):
        return f"Story(prompts: {self.prompts}, template: {self.template})"

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )

# answers = {"noun": "banana", "adjective": "sleepy", "verb": "walk", "place": "couch", "plural_noun": "ice cubes"}

once_upon = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

mad_bunch = Story(
    ["noun", "verb", "plural_noun", "noun", "adjective", "noun", "adjective", "noun"],
    """Here's the story of a lovely {noun} who was {verb} up three very lovely {plural_noun}. All of them had {noun} of {adjective}, like their {noun}, the {adjective} one in {noun}."""
)

mad_island = Story(
    ["noun", "place", "name", "profession", "noun", "noun", "profession", "noun", "name", "name"], """The {houn} set ground on the shore of this uncharted desert {place} with {name}, the {profession} too, the {noun} and his {noun}, the {profession}, the {noun} and {name}, here on {name}'s Isle."""
)

mad_turtle = Story(
    ["adjective", "adjective", "noun", "noun", "adjective", "noun", "adjective", "name" "noun", "noun", "verb"], """They're the world's most {adjective} fighting team (We're really {adjective}!). They're {noun} in a half-{noun} and they're {adjective} (Hey - get a {noun}!). When the {adjective} {name} attacks, these {noun} {noun} don't {verb} him no slack!"""
)

mad_busters = Story(
    ["adjective", "place", "verb", "noun", "adjective", "verb", "noun", "noun"], """If there's somethin' {adjective} in the {place}, who ya gonna {verb}? {noun}! There's somethin' {adjective} and it don't {verb} good, who ya gonna call {noun}! I ain't afraid a no {noun}!"""
)