#!/usr/bin/python3
import functions

# Call create_keygroups to get the list of keywords
keyword_group = create_keygroups("users.txt") # text file will be our dictionnary

# Now call copy_lines with the obtained keyword_group
input_file_name = 'D:/dossier/Cours/INGE3/projet/ftp_rawdata.txt' # Path folder of the input file
output_file_name = 'D:/dossier/Cours/INGE3/projet/mdp.txt' # Path folder of the output file

copy_lines(input_file_name, output_file_name, keyword_group)

