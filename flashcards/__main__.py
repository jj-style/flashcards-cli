import sys
import argparse
from flashcards.card_set import Set, learn_set

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--shuffle", help="shuffle order of flashcards in the set", action="store_true")
    parser.add_argument("-r", "--reverse", help="reverse answering, answer with term rather than definition", action="store_true")
    parser.add_argument("path", help="path to flashcard csv file")
    
    args = parser.parse_args()

    card_set = Set.load_from_csv(args.path)
    learn_set(card_set, shuffle=args.shuffle, answer_reverse=args.reverse)