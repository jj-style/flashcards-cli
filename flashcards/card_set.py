from flashcards.flashcard import Flashcard
import random
import os

class Set:
    def __init__(self, name, cards=[]):
        self.current = 0
        self.cards = cards
        self.name = name

    @classmethod
    def create_empty_set(cls):
        return cls("empty set",[])

    @classmethod
    def load_from_csv(cls, filename):
        cards = []
        with open(filename, "r") as file:
            next(file)
            for line in file:
                term, definition = line.split(",")
                cards.append(Flashcard(term.strip(), definition.strip()))
        return cls(os.path.basename(filename),cards)

    @property
    def number_of_terms(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.cards):
            self.current += 1
            return self.cards[self.current - 1]
        raise StopIteration

def learn_set(card_set, shuffle=False, answer_reverse=False):
    print(f"Learning {card_set.number_of_terms} terms in {card_set.name}, good luck!\n")
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