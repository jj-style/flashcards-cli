# flashcards-cli
Command line program to learn sets of flash cards

Useful for learning vocabulary of a new language.

# Usage
```bash
usage: flashcards [-h] [-s] [-r] path [path ...]

positional arguments:
  path           path(s) to flashcard csv file(s)

optional arguments:
  -h, --help     show this help message and exit
  -s, --shuffle  shuffle order of flashcards in the set
  -r, --reverse  reverse answering, answer with term rather than definition
  ```
  
  ## Flashcard Sets
  Currently only loads flashcards stored in a CSV file with the format:
  |Term|Description|
  |----|-----------|
  |我|I|
  |你|You|
  |我们|We;us|
  
  Validation is case **insensitive** and if there are multiple possible answers like above, separate them with a semi-colon and if the answer provided matches
  just one of the options it will be counted as correct.  
  If the answer is incorrect the correct answer is shown.
  
  I will implement some other formats to load flashcard sets from if I find there is a universal standard or more common format.
  However, if you have a flashcard set in Quizlet it can be exported and you can choose it to export in the format above.
