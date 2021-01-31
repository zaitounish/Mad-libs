a = r"""Today I went to the zoo. I saw a(n)
___________(adjective)
_____________(Noun) jumping up and down in its tree.
He _____________(verb, past tense) __________(adverb)
through the large tunnel that led to its _______(adjective)
__________(noun). I got some peanuts and passed
them through the cage to a gigantic gray _______(noun)
towering above my head. Feeding that animal made
me hungry. I went to get a __________(adjective) scoop
of ice cream. It filled my stomach. Afterwards I had to
__________(verb) __________ (adverb) to catch our bus.
When I got home I __________(verb, past tense) my
mom for a __________(adjective) day at the zoo"""

print(a)

import json
import os


class MadLibs:
    path = "./template"
    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions
        self.user_input = []
        self.story = None

    @classmethod
    def from_json(cls, name, path=None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib

    def get_words_from_user(self):
        print("Please provide the following words: ")
        for desc in self.word_descriptions:
            ui = input(desc + " ")
            self.user_input.append(ui)
        return self.user_input

    def build_story(self):
        self.story = self.template.format(*self.user_input)
        return self.story

    def show_story(self):
        print(story)


def select_template():
    print("Select a Mad Lib from the following list:")
    templates = os.listdir(MadLibs.path)
    template = input(str(templates) + " ")
    return template


temp_name = select_template()
# temp_name = "day_at_the_zoo.json"
mad_lib = MadLibs.from_json(temp_name)
words = mad_lib.get_words_from_user()
story = mad_lib.build_story()
mad_lib.show_story()