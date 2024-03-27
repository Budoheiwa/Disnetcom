#!/usr/bin/python3
from functions import *

if __name__ == "__main__":
    # Call create_keygroups to get the list of keywords
    keyword_group = create_keygroups("users.txt") # text file will be our dictionnary

    # Now call copy_lines with the obtained keyword_group
    input_file_name = './testread.txt' # Path folder of the input file
    output_file_name = './credentials.txt' # Path folder of the output file

    copy_lines(input_file_name, output_file_name, keyword_group)

# Need to create dictionnaries for all types of secret information