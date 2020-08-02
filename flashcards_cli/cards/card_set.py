<<<<<<< HEAD:flashcards_cli/cards/card_set.py
from .flashcard import Flashcard
=======
from flashcards_cli.flashcard import Flashcard
>>>>>>> tmp:flashcards_cli/card_set.py
import random
import os
import reprlib

class Set:
    def __init__(self, name, cards=[]):
        self.__current = 0
        self.cards = cards
        self.name = name

    @classmethod
    def create_empty_set(cls):
        """creates an empty set of flashcards"""
        return cls("Unnamed Set",[])

    @classmethod
    def load_from_csv(cls, filename, *filenames):
        """reads flashcards from csv file and returns a new set of flashcards
            can take more than one filename and combines all flashcards into one set
        """
        cards = []
        files = [filename]
        files.extend(filenames)
        files_read = 0
        for fname in files:
            try:
                with open(fname, "r") as file:
                    next(file) # skip header of csv file
                    for line in file:
                        term, definition = line.split(",")
                        cards.append(Flashcard(term.strip(), definition.strip()))
                files_read += 1
            except:
                print(f"error opening {fname}, skipping...")
                continue
        if files_read == 0:
            print("Unable to load any flashcards, please try again.")
            exit(1)
        return cls(",".join(list(map(os.path.basename,files))),cards)

    @property
    def number_of_terms(self):
        return len(self.cards)

    def shuffle(self):
        """shuffles the order of the flashcards"""
        random.shuffle(self.cards)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current < len(self.cards):
            self.__current += 1
            return self.cards[self.__current - 1]
        raise StopIteration
    
    def __str__(self):
        return f"{self.name} containing {self.number_of_terms} terms"
    
    def __repr__(self):
        return reprlib.repr(self.cards)

def learn_set(card_set, shuffle=False, answer_reverse=False):
    """Loop over set a set of flashcards"""

    print(f"Learning {card_set}, good luck!\n")
    if shuffle:
        card_set.shuffle()
    
    for card in card_set:
        if not answer_reverse:
            question, answer = card.term, card.definition
        else:
            question, answer = card.definition, card.term
        try:
            answer = input(f"{question} : ")
            if answer == "EXIT":
                return
            if not card.check(answer, reverse=answer_reverse):
                print("Incorrect:", card)
        except KeyboardInterrupt:
            print()
            return