class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def check(self, answer, reverse=False):
        """validate an answer against the flashcard
            arguments:
                answer: answer given by user to validate against (required)
                reverse: boolean representing whether answering with definition or term, defaults to False (optional)
        """
        correct_answer = self.definition if not reverse else self.term
        if correct_answer.lower() == answer.lower():
            return True
        for possible_answer in correct_answer.split(";"):
            if possible_answer.lower() == answer.lower():
                return True
        return False

    def __eq__(self, rhs):
        if not isinstance(rhs, Flashcard):
            return NotImplemented
        return (self.term == rhs.term) and (self.definition == rhs.definition)
    
    def __ne__(self, rhs):
        if not isinstance(rhs, Flashcard):
            return NotImplemented
        return (self.term != rhs.term) or (self.definition != rhs.definition)

    def __str__(self):
        return f"{self.term}:{self.definition}"

    def __repr__(self):
        return f"Flashcard=(term={self.term}, definition={self.definition})"