# MamaduConverter
A single-purpose program made as a learning project for a friend who wanted to make an Anki deck from a text file.
You can do whatever you feel like doing with it.

Usage:
Use it from Windows' CMD and providing the source text file name or path. It will output an Anki package named
<sourcefilename>.apkg and a text file named NotAdded-<sourcefilename>.txt where wrongly formatted data will be outputted.

The program takes each line in the source text file as a card template, taking the first string as the question and the second
as the answer, divided by one or more tabs. 
Any string containing a dash is assumed to be wrongly formatted. The same applies to strings without tabs.

Add the -h flag to see help in the program.
