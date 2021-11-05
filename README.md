# Python-Words-in-Common
 Python script to find words in common between different texts.

The function find_words_in_common receives as arguments two strings.
The first string is the name of a directory where text files to be processed are located.
The second string is the name of a file containing stop words (i.e., common words in the English language).
The function returns a set of words (strings) that all the text files found in the directory passed as a first argument
have in common.
These common words should not include any of the stop words in the filename passed as a second argument.

The folder "texts" contains .txt files of famous writings in American history and a stop words file.
When testing the function using the three documents in the text directory, the set returned should be:
{'liberty', 'god', 'lives', 'people', 'civil', 'created', 'nation', 'equal'}
