# BookBot

BookBot is a command-line Python tool that analyzes a text file (like a book) and prints a report with:

- the total word count
- how many times each letter appears, sorted from most to least common

It's my first [Boot.dev](https://www.boot.dev) project, built on WSL while working through the Python course.

## Usage

```bash
python3 main.py <path_to_book>
```

Example:

```bash
python3 main.py books/frankenstein.txt
```

## Example output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============
```

## Project structure

```
BookBot/
├── main.py        # entry point, handles arguments and prints the report
├── stats.py       # word counting, character counting and sorting
├── books/         # sample books to analyze
└── README.md
```

## Books

The sample books in `books/` are public domain texts from [Project Gutenberg](https://www.gutenberg.org):

- *Frankenstein* by Mary Shelley
- *Moby Dick* by Herman Melville
- *Pride and Prejudice* by Jane Austen

## Requirements

- Python 3.8+
- No external libraries needed

## What I learned

- Reading files and working with strings
- Using dictionaries to count characters
- Sorting with a custom key function
- Reading command-line arguments with `sys.argv`
- Splitting code across multiple modules
