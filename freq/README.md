# freq (in progress)

A simple script written in python to do frequency analysis. It usually comes handy in cryptography.

It's not complete yet. 

## Usage

```
usage: freq.py [-h] [-n [NGRAM]] [-a] [-d] [-s] [-k]

optional arguments:
  -h, --help            show this help message and exit
  -n [NGRAM], --ngram [NGRAM]  no of steps (default=1)
  -a, --alphabets       only analyses the frequency of alphabets(A-Z,a-z)
  -d, --digit           only analyses the frequency of digits
  -s, --symbols         only analyses the frequency of special characters
  -k, --suggest         only analyses the frequency and suggests possible cypher  
```

## How to pass a file content as input?

```bash
cat file1 | ./freq.py
```
and you the output

## How to input manually?

```bash
./freq.py
```

and then start providing input and it will process each line as input.



