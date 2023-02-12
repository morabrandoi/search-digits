# Search-Digits

## About
This a project done as a birthday present for a person who likes the number pi a little too much. In this code I use Pi but any huge text of digits can be used. The way this works is given a search string like "happy birthday", the algorithm looks for the general "pattern" of the word in the digit string. For example, the pattern of 'apple' is 'one unique letter followed by another unique letter followed by the same letter as the previous letter, followed by two more unique letters'. So examples of digits which could match this are '12234' or '82274' and so on. Because there are only 10 digits in our base 10 system then only strings with at most 10 unique characters can be searched. Once a match is found, a mapping is generated and the position is printed out to the console. For reasons of computational tractability, the string should be 14 or less characters long as well.

## The Maths
I wrote a small not-so-serious 'math paper' detailing how I analyzed the task of finding a string in the digitis of pi. I weighed the probabilites of different methods and explain the limitations of this one. The link to this (written in Latex) is : https://www.overleaf.com/read/jrfzmvznzsjs

## Digit Source
The pi-billion.txt file referenced in the code is raw text of the first billion digits of pi. It takes 10000002 Bytes (~1GB) and can be found at https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt

## Running
I wrote this somewhat hastily and did not setup a proper conda environment to track python version or any requirements used, but I do know that I used Python3.
