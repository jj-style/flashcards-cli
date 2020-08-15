# flashcards-cli
Command line program to learn sets of flash cards.

Useful for learning vocabulary of a new language.

## Installation
From [pypi](https://pypi.org/project/python-flashcards/): `pip install python-flashcards`

## Usage
```bash
usage: flashcards_cli [-h] [-s] [-r] [-v] path [path ...]

positional arguments:
  path           path to flashcard csv file(s)

optional arguments:
  -h, --help     show this help message and exit
  -s, --shuffle  shuffle order of flashcards in the set
  -r, --reverse  reverse answering, answer with term rather than definition
  -v, --version  show program's version number and exit
  ```
  
  ### Flashcard Sets
  Currently only loads flashcards stored in a CSV file with the format:
  |Term|Description|
  |----|-----------|
  |我|I|
  |你|You|
  |我们|We;us|
  
  Note, the first row of the CSV file is skipped so make sure you have a term/definition header otherwise a flashcard will go missing!  

  Validation is case **insensitive** and if there are multiple possible answers like above, separate them with a semi-colon and if the answer provided matches
  just one of the options it will be counted as correct.  
  If the answer is incorrect the correct answer is shown.  

  Multiple files can be given and they will all be combined.  
  The wildcard (*) symbol can also be used for the argument.
  
  I will implement some other formats to load flashcard sets from if I find there is a universal standard or more common format.
  However, if you have a flashcard set in Quizlet it can be exported and you can choose it to export in the format above (csv).
