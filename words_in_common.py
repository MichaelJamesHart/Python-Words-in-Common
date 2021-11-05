#Michael Hart

"""
The function find_words_in_common receives as arguments two strings.
The first string is the name of a directory where text files to be processed are located.
The second string is the name of a file containing stop words (i.e., common words in the English language).
The function returns a set of words (strings) that all the text files found in the directory passed as a first argument
have in common.
These common words should not include any of the stop words in the filename passed as a second argument.

The folder "texts" contains .txt files of famous writings in American history and a stop words file.
When testing the function using the three documents in the text directory, the set returned should be:
{'liberty', 'god', 'lives', 'people', 'civil', 'created', 'nation', 'equal'}

"""

# This function returns a version of string full_str without remove_chars characters.
def remove_characters(full_str, remove_chars):

    # Set up string to return that will eventually not have the remove_chars.
    clean_str = full_str

    # Go through each of the characters in remove_chars and remove them from clean_str.
    for no_char in remove_chars:
        clean_str = clean_str.replace(no_char, '')

    return clean_str
    

# This function returns a version of word_list without words in stop_words.
def remove_stop_words(word_list, stop_words):

    # Make a copy of word_list so the original isn't modified.
    clean_list = word_list.copy()
    
    # Open the stop_words.txt file.
    stop_words_file = open(stop_words)
    
    # Create a list stop_words from the text of stop_words_file.
    stop_words = stop_words_file.read().lower()
    
    # Close the stop_words.txt. file.
    stop_words_file.close()
    
    # Split stop_words into a list.
    stop_words_list = stop_words.split()

    # Go through each stop word.
    for stop_word in stop_words_list:

        # Remove the stop word from list, as long as there are words left to remove.
        words_left_to_remove = True
        while words_left_to_remove:

            try:

                # rstrip() removes new line characters that can show up in text files.
                clean_list.remove(stop_word.rstrip())

            except:
                words_left_to_remove = False

    # Return the clean word_list with the stop_words removed.
    return clean_list


# Import OS for use in find_words_in_common.
import os

# This function returns a set of words in common for all text files in text_files_dir excluding words in stop_words_file.
def find_words_in_common(text_files_dir, stop_words_file):
    
    # Create a list of the file names in the text_files_dir.
    list_of_files = os.listdir(text_files_dir)

    # Iterate through each filename in the list of files.
    for filename in list_of_files:
        
        # Open the filename.
        curr_file = open(text_files_dir + "/" + filename)
        
        # Read the filename's content, and change all letters to lower-case.
        curr_file_content = curr_file.read().lower()
        
        # Close the filename.
        curr_file.close()
        
        # Call remove_characters to remove unwanted characters from the text.
        curr_file_content = remove_characters(curr_file_content, '.,;!?:-\'"$0123456789')
           
        # Use split to create a list of the words from curr_file_content.
        curr_file_content = curr_file_content.split()

        # Remove the stop words from curr_file_content, and change it into a set.
        clean_curr_file_content = set(remove_stop_words(curr_file_content, stop_words_file))
        
        # On the first iteration of looping through list_of_files,
        # the common_words will be set as the clean_curr_file_content.
        if filename == list_of_files[0]:
            common_words = set(clean_curr_file_content)
        
        # Use the intersection (&) to keep only words that are common between 
        # the current file and previous files in the common_words set.
        common_words = common_words & clean_curr_file_content

    
    # Return the common_words.
    return common_words
