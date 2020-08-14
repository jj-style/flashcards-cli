from flashcards_cli.flashcard import Flashcard
import random
import os
import reprlib
from itertools import chain

class Set:
    def __init__(self, name, cards=None):
        self.__current = 0
        self.cards = list(cards) if cards is not None else []
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
    
    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        """shuffles the order of the flashcards"""
        random.shuffle(self.cards)

    def __iter__(self):
        return iter(self.cards)

    def __getitem__(self, index):
        result = self.cards[index]
        return Set(result) if isinstance(index, slice) else result

    def __eq__(self, rhs):
        if not isinstance(rhs, Set):
            return NotImplemented
        return self.cards == rhs.cards
    
    def __ne__(self, rhs):
        if not isinstance(rhs, Set):
            return NotImplemented
        return self.cards != rhs.cards

    def __add__(self, rhs):
        return Set(f"{self.name},{rhs.name}", chain(self.cards, rhs.cards))
    
    def __str__(self):
        return f"{self.name} containing {len(self)} terms"
    
    def __repr__(self):
        return f"Set({reprlib.repr(self.cards)})"

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