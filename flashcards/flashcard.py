class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def check(self, answer, reverse=False):
        correct_answer = self.definition if not reverse else self.term
        if correct_answer.lower() == answer.lower():
            return True
        for possible_answer in correct_answer.split(";"):
            if possible_answer.lower() == answer.lower():
                return True
        return False

    def __str__(self):
        return f"{self.term}:{self.definition}"

    def __repr__(self):
        return f"Flashcard=(term={self.term}, definition={self.definition})"